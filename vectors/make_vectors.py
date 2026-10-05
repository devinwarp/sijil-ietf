#!/usr/bin/env python3
"""Generate the test vectors in Appendix A of
draft-thaha-scitt-agent-execution-evidence-00.

Deterministic: seeds are fixed so the output is reproducible.
Requires: cbor2, pynacl.
"""
import hashlib
import cbor2
from nacl.signing import SigningKey

SHA256 = -16          # COSE algorithm identifier for SHA-256
EDDSA = -8            # COSE algorithm identifier for EdDSA
OKP, ED25519 = 1, 6   # COSE key type / curve

# ---------------------------------------------------------------- keys
harness_sk = SigningKey(bytes.fromhex("11" * 32))   # Issuer (Harness operator)
agent_sk = SigningKey(bytes.fromhex("22" * 32))     # Agent key (per-call signatures)
harness_pk = bytes(harness_sk.verify_key)
agent_pk = bytes(agent_sk.verify_key)

HARNESS_ISS = "https://harness.example/issuer"
AGENT_ID = "wimse://agents.example.com/agent/billing-assistant"
AGENT_COSE_KEY = {1: OKP, 3: EDDSA, -1: ED25519, -2: agent_pk}
HARNESS_KID = hashlib.sha256(harness_pk).digest()[:8]
AGENT_KID = hashlib.sha256(agent_pk).digest()[:8]


def enc(obj):
    """Deterministic CBOR (RFC 8949, Section 4.2.1)."""
    return cbor2.dumps(obj, canonical=True)


def digest(data: bytes):
    return [SHA256, hashlib.sha256(data).digest()]


def sign1(sk, kid, claims, content_type, payload):
    """COSE_Sign1 Signed Statement per RFC 9943 Section 6."""
    phdr = {1: EDDSA, 3: content_type, 4: kid, 15: claims}
    phdr_b = enc(phdr)
    sig_structure = ["Signature1", phdr_b, b"", payload]
    sig = sk.sign(enc(sig_structure)).signature
    return cbor2.CBORTag(18, [phdr_b, {}, payload, sig])


# ------------------------------------------------------ CBOR diagnostic
def diag(o, ind=0):
    pad = "  " * ind
    if isinstance(o, cbor2.CBORTag):
        return f"{o.tag}({diag(o.value, ind)})"
    if isinstance(o, dict):
        items = [f"{pad}  {diag(k, ind+1)}: {diag(v, ind+1)}" for k, v in o.items()]
        return "{\n" + ",\n".join(items) + f"\n{pad}}}"
    if isinstance(o, list):
        if all(not isinstance(x, (dict, list, cbor2.CBORTag)) for x in o) and len(enc(o)) < 48:
            return "[" + ", ".join(diag(x, ind) for x in o) + "]"
        items = [f"{pad}  {diag(x, ind+1)}" for x in o]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"
    if isinstance(o, bytes):
        return "h'" + o.hex() + "'"
    if isinstance(o, str):
        return '"' + o + '"'
    if o is None:
        return "null"
    return str(o)


out = []
def emit(title, obj):
    out.append(f"--- {title}\n{diag(obj)}\n")


# ------------------------------------------------- 1. Agent Credential
NBF, EXP = 1790000000, 1792592000  # 2026-09-21T13:33:20Z .. +30 days
pepper = b"operator-pepper-0001"
principal_hash = hashlib.sha256(pepper + b"user:alice@example.com").digest()

responsible_hash = hashlib.sha256(pepper + b"org:acme-finance.example").digest()
agent_cred = {
    1: 1,                       # aee-type = agent-credential
    2: AGENT_ID,                # agent_id (runtime identity at issuance)
    3: AGENT_COSE_KEY,
    4: {1: 1, 2: principal_hash},          # principal: natural person, hashed
    5: {1: "example-harness", 2: "3.2.0"},  # harness
    6: {1: 2, 3: "example-model-2026-06", 4: "model-provider.example"},  # api
    7: {1: NBF, 2: EXP},
    9: "did:web:agents.example.com:billing-assistant",   # logical_agent_id
    10: {1: 2, 2: "acme-finance.example"},               # responsible_entity (org)
    11: [                                                 # runtime_identities
        {1: AGENT_ID, 2: 1, 3: "agents.example.com", 4: NBF, 5: EXP},
        {1: "spiffe://prod.example.net/ns/finance/sa/billing", 2: 2,
         3: "prod.example.net", 4: NBF, 5: EXP},
    ],
    12: 2,                                                # lifecycle_class: persistent
}
agent_cred_payload = enc(agent_cred)
agent_cred_digest = digest(agent_cred_payload)
claims = {1: HARNESS_ISS, 2: AGENT_ID, "aee_type": 1}
agent_cred_ss = sign1(harness_sk, HARNESS_KID, claims,
                      "application/aee-statement+cbor", agent_cred_payload)

# ------------------------------------------------- 2. Policy pack / config
pack_bytes = b'{"pack":"example-deployment-pack","v":"1.0.0"}'
pack_digest = digest(pack_bytes)
parent_pack_digest = digest(b'{"pack":"example-sector-pack","v":"2.1.0"}')

entries = [
    ["SYSTEM_PROMPT", digest(b"You are a billing assistant.\n"), 1],
    ["CLAUDE.md", digest(b"# Instructions\nNever email externally.\n"), 2],
    ["tools/send_invoice.json", digest(b'{"name":"send_invoice"}'), 6],
]
entries.sort(key=lambda e: e[0].encode())
config_digest = digest(enc(entries))

# ------------------------------------------------- 3. Execution Receipts
GENESIS = b"\x00" * 32
T0 = 1790001000000  # milliseconds

def record(seq, prev, rtype, decision, task_seq, ts, parent=None, **opt):
    r = {
        1: 5, 2: seq, 3: prev, 4: rtype,
        6: decision, 7: pack_digest, 8: config_digest,
        9: AGENT_ID, 10: {1: 1, 2: principal_hash},
        11: task_seq, 14: ts,
    }
    if parent is not None:
        r[5] = parent
    r.update(opt)
    return r

recs = []
r0 = record(0, GENESIS, 1, 1, 0, T0)                       # task_start
h0 = hashlib.sha256(enc(r0)).digest()
r1 = record(1, h0, 3, 1, 1, T0 + 120)
r1[18] = 1                                                  # decision point: model
r1[16] = "example-model-2026-06"
r1[12] = digest(b"<prompt bytes>")
r1[13] = digest(b"<completion bytes>")
h1 = hashlib.sha256(enc(r1)).digest()
r2 = record(2, h1, 4, 3, 2, T0 + 350, parent=1)            # tool_call, confirm
r2[18] = 2
r2[16] = "send_invoice"
r2[12] = digest(b'{"to":"ap@customer.example","amount":"1200.00"}')
r2[17] = "api.customer.example"
# per-call agent signature (AIP-style): COSE_Sign1, detached payload = record bytes
r2_core = enc(r2)
# The agent signature is computed over the record WITHOUT key 15 (see spec).
agent_sig_structure = ["Signature1", enc({1: EDDSA, 3: "application/aee-statement+cbor", 4: AGENT_KID, 15: {1: AGENT_ID, 2: AGENT_ID}}), b"", r2_core]
agent_sig = agent_sk.sign(enc(agent_sig_structure)).signature
r2[15] = enc(cbor2.CBORTag(18, [enc({1: EDDSA, 3: "application/aee-statement+cbor", 4: AGENT_KID, 15: {1: AGENT_ID, 2: AGENT_ID}}), {}, None, agent_sig]))
h2 = hashlib.sha256(enc(r2)).digest()

# Epoch root over record hashes h0..h2 (RFC 9162 Merkle tree hash)
def mth(leaves):
    if len(leaves) == 1:
        return hashlib.sha256(b"\x00" + leaves[0]).digest()
    k = 1
    while k * 2 < len(leaves):
        k *= 2
    return hashlib.sha256(b"\x01" + mth(leaves[:k]) + mth(leaves[k:])).digest()

epoch = {1: 6, 2: AGENT_ID, 3: 0, 4: 2, 5: GENESIS, 6: h2, 7: mth([h0, h1, h2]), 8: 3}
epoch_ss = sign1(harness_sk, HARNESS_KID, {1: HARNESS_ISS, 2: AGENT_ID, "aee_type": 6},
                 "application/aee-statement+cbor", enc(epoch))
r2_ss = sign1(harness_sk, HARNESS_KID, {1: HARNESS_ISS, 2: AGENT_ID, "aee_type": 5},
              "application/aee-statement+cbor", enc(r2))

emit("A.1 Keys", {"harness_sk_seed": bytes.fromhex("11"*32), "harness_pk": harness_pk,
                  "agent_sk_seed": bytes.fromhex("22"*32), "agent_pk": agent_pk})
emit("A.2 Agent Credential Statement payload", agent_cred)
emit("A.2 Agent Credential Statement payload digest", agent_cred_digest)
emit("A.2 Agent Credential Signed Statement", agent_cred_ss)
emit("A.3 Configuration Integrity entries and digest", {"entries": entries, "config_digest": config_digest})
emit("A.4 Execution Receipt seq 0 (task_start)", r0)
emit("A.4 record-hash(0)", h0)
emit("A.4 Execution Receipt seq 1 (inference)", r1)
emit("A.4 record-hash(1)", h1)
emit("A.4 Execution Receipt seq 2 (tool_call, confirm, parent_seq=1)", r2)
emit("A.4 record-hash(2)", h2)
emit("A.4 Execution Receipt seq 2 Signed Statement", r2_ss)
emit("A.5 Execution Epoch Statement", epoch)
emit("A.5 Execution Epoch Signed Statement", epoch_ss)

# ------------------------------------------------- sanity: verify signatures
from nacl.signing import VerifyKey
def verify(ss, pk):
    phdr_b, _, payload, sig = ss.value
    VerifyKey(pk).verify(enc(["Signature1", phdr_b, b"", payload]), sig)
verify(agent_cred_ss, harness_pk); verify(r2_ss, harness_pk); verify(epoch_ss, harness_pk)
VerifyKey(agent_pk).verify(enc(agent_sig_structure), agent_sig)
assert hashlib.sha256(enc(r1)).digest() == h1 and r1[3] == h0 and r2[3] == h1

text = "\n".join(out)
open("vectors.txt", "w").write(text)
open("agent-credential.cose", "wb").write(enc(agent_cred_ss))
open("execution-receipt-2.cose", "wb").write(enc(r2_ss))
open("execution-epoch.cose", "wb").write(enc(epoch_ss))
print(text)
print("hex sizes:", len(enc(agent_cred_ss)), len(enc(r2_ss)), len(enc(epoch_ss)))
