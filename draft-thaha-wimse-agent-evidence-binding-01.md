---
v: 3
title: "Evidence Binding for AI Agent Credentials"
abbrev: "Agent Evidence Binding"
docname: draft-thaha-wimse-agent-evidence-binding-01
category: info
submissiontype: IETF
consensus: true
ipr: trust200902
area: "Security"
workgroup: "Workload Identity in Multi System Environments"
keyword:
  - WIMSE
  - AI agent
  - audit
  - evidence
  - SCITT
venue:
  group: "WIMSE"
  type: "Working Group"
  mail: "wimse@ietf.org"
  arch: "https://mailarchive.ietf.org/arch/browse/wimse/"
  repo: "https://github.com/devinwarp/sijil-ietf"
  latest: "https://github.com/devinwarp/sijil-ietf"
pi: [toc, sortrefs, symrefs]
date: 2026-10

author:
  - name: Shameer Thaha
    organization: Individual Contributor
    region: Dubai
    country: United Arab Emirates
    email: shameerthaha@gmail.com
  - name: Shaibi Shamsudeen
    organization: Individual Contributor
    country: United Arab Emirates
    email: shaibis@gmail.com

normative:
  RFC3553:
    title: An IETF URN Sub-namespace for Registered Protocol Parameters
    author:
      - ins: M. Mealling
      - ins: L. Masinter
      - ins: T. Hardie
      - ins: G. Klyne
    date: 2003-06
    seriesinfo:
      BCP: 73
      RFC: 3553
      DOI: 10.17487/RFC3553
  RFC7519:
    title: JSON Web Token (JWT)
    author:
      - ins: M. Jones
      - ins: J. Bradley
      - ins: N. Sakimura
    date: 2015-05
    seriesinfo:
      RFC: 7519
      DOI: 10.17487/RFC7519
  RFC8392:
    title: CBOR Web Token (CWT)
    author:
      - ins: M. Jones
      - ins: E. Wahlstroem
      - ins: S. Erdtman
      - ins: H. Tschofenig
    date: 2018-05
    seriesinfo:
      RFC: 8392
      DOI: 10.17487/RFC8392
  RFC8785:
    title: JSON Canonicalization Scheme (JCS)
    author:
      - ins: A. Rundgren
      - ins: B. Jordan
      - ins: S. Erdtman
    date: 2020-06
    seriesinfo:
      RFC: 8785
      DOI: 10.17487/RFC8785
  RFC9943:
    title: "An Architecture for Trustworthy and Transparent Digital Supply Chains"
    author:
      - ins: H. Birkholz
      - ins: A. Delignat-Lavaud
      - ins: C. Fournet
      - ins: Y. Deshpande
      - ins: S. Lasker
    date: 2026-06
    seriesinfo:
      RFC: 9943
      DOI: 10.17487/RFC9943
  RFC8693:
    title: OAuth 2.0 Token Exchange
    author:
      - ins: M. Jones
      - ins: A. Nadalin
      - ins: B. Campbell
      - ins: J. Bradley
      - ins: C. Mortimore
    date: 2020-01
    seriesinfo:
      RFC: 8693
      DOI: 10.17487/RFC8693
  RFC9110:
    title: HTTP Semantics
    author:
      - ins: R. Fielding
      - ins: M. Nottingham
      - ins: J. Reschke
    date: 2022-06
    seriesinfo:
      STD: 97
      RFC: 9110
      DOI: 10.17487/RFC9110
  RFC9651:
    title: Structured Field Values for HTTP
    author:
      - ins: M. Nottingham
      - ins: P-H. Kamp
    date: 2024-09
    seriesinfo:
      RFC: 9651
      DOI: 10.17487/RFC9651
  I-D.thaha-scitt-agent-execution-evidence:
    title: "Agent Execution Evidence: A SCITT Profile for Verifiable Records of AI Agent Runs"
    author:
      - ins: S. Thaha
      - ins: S. Shamsudeen
    date: 2026-10
    seriesinfo:
      Internet-Draft: draft-thaha-scitt-agent-execution-evidence-01
  I-D.ietf-wimse-aims:
    title: AI Identity Management System
    author:
      - ins: P. Kasselman
      - ins: J. Lombardo
      - ins: Y. Rosomakho
      - ins: B. Campbell
      - ins: N. Steele
      - ins: A. Parecki
    date: 2026-09
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-aims-00

informative:
  DID-WEB:
    title: "did:web Method Specification"
    author:
      - org: W3C Credentials Community Group
    date: 2023
    target: https://w3c-ccg.github.io/did-method-web/
  RFC9942:
    title: "CBOR Object Signing and Encryption (COSE) Receipts"
    author:
      - ins: O. Steele
      - ins: H. Birkholz
      - ins: A. Delignat-Lavaud
      - ins: C. Fournet
    date: 2026-06
    seriesinfo:
      RFC: 9942
      DOI: 10.17487/RFC9942
  I-D.ietf-wimse-workload-creds:
    title: WIMSE Workload Credentials
    author:
      - ins: B. Campbell
      - ins: J. Salowey
      - ins: A. Schwenkschuster
      - ins: Y. Sheffer
      - ins: Y. Rosomakho
    date: 2026-07
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-workload-creds-02
  I-D.ietf-wimse-arch:
    title: Workload Identity in a Multi System Environment (WIMSE) Architecture
    author:
      - ins: J. Salowey
      - ins: Y. Rosomakho
      - ins: H. Tschofenig
    date: 2026-07
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-arch-08
  I-D.ietf-oauth-transaction-tokens:
    title: Transaction Tokens
    author:
      - ins: A. Tulshibagwale
      - ins: G. Fletcher
      - ins: P. Kasselman
    date: 2026-07
    seriesinfo:
      Internet-Draft: draft-ietf-oauth-transaction-tokens-11
  I-D.gilda-audit-agent-audit-record:
    title: An Audit Record Format for AI Agent Authorization Decisions
    author:
      - ins: S. Gilda
    date: 2026-10
    seriesinfo:
      Internet-Draft: draft-gilda-audit-agent-audit-record-00
  I-D.kuehlewind-audit-architecture:
    title: An Architecture for Auditing Agent Delegation and Interactions
    author:
      - ins: M. Kuehlewind
      - ins: H. Birkholz
    date: 2026-09
    seriesinfo:
      Internet-Draft: draft-kuehlewind-audit-architecture-01
  I-D.ietf-scitt-scrapi:
    title: "Supply Chain Integrity, Transparency, and Trust (SCITT) Reference APIs"
    author:
      - ins: H. Birkholz
      - ins: J. Geater
      - ins: A. Delignat-Lavaud
    date: 2026-06
    seriesinfo:
      Internet-Draft: draft-ietf-scitt-scrapi-11
  IN-TOTO:
    title: in-toto Attestation Framework Specification
    author:
      - org: in-toto project
    date: 2024
    target: https://github.com/in-toto/attestation
  I-D.schrock-ep-authorization-evidence-chain:
    title: "Authorization Evidence Chains: Composing Heterogeneous Agent-Action Evidence (EP-AEC)"
    author:
      - ins: I. Schrock
    date: 2026-10
    seriesinfo:
      Internet-Draft: draft-schrock-ep-authorization-evidence-chain-08
  DSSE:
    title: Dead Simple Signing Envelope
    author:
      - org: secure-systems-lab
    date: 2023
    target: https://github.com/secure-systems-lab/dsse

--- abstract

The WIMSE AI Identity Management System (AIMS) requires tamper-evident agent audit logs but does not specify their format or discovery. This document maps the AIMS minimum fields to the SCITT Agent Execution Evidence profile, defines one claim that binds a workload credential to the persistent agent, governing policy, expected Evidence Service and optional Assurance Statement, and defines an in-toto predicate type for carrying Execution Receipts in the audit format proposed for WIMSE. It also describes how a service admits an agent's call by checking its assurance at the moment of the request, and defines an HTTP field that links each call to the caller's evidence. It is input to the AIMS work and makes no change to it.

--- middle

# Introduction

Section 11 of {{I-D.ietf-wimse-aims}} ("Agent Monitoring, Observability and Remediation") requires tamper-evident audit logs and lists the fields an audit event must record at a minimum. Section 8 does not require any particular posture assessment mechanism or evidence format, and Section 13 states that compliance criteria are out of scope. That is a reasonable division: an identity management framework should not pick a log format. It leaves four practical questions open for an implementer:

1. In what format are the seven minimum fields recorded so that a party other than the operator can verify them?
2. Given an agent's credential, how does a relying party learn which Evidence Service and policy to expect that evidence under, and which assurance statement applies?
3. Before acting on a call, how does a Serving Party decide, for that call, that the calling agent is registered, currently assured at the level the operation requires, and acting for a Principal entitled to it?
4. When a request passes through several agents, how are the principal of the transaction and the Actor Chain carried with it and recorded on each side?

{{I-D.thaha-scitt-agent-execution-evidence}} answers the first question with per-call Execution Receipts and Assurance Statements registered through SCITT {{RFC9943}}, and supplies the admission records and linking rules behind the third and fourth. This document answers the second with one claim, `aee_evidence`, that an identity server MAY place in a Workload Identity Token {{I-D.ietf-wimse-workload-creds}} or other agent token; the third with the admission procedure of {{admission}}; and the fourth with an HTTP field and the use of nested `act` claims {{RFC8693}} ({{carrying}}). It also maps the AIMS fields and defines an in-toto predicate so that the formats compose with {{I-D.gilda-audit-agent-audit-record}}.

The decision to act is made per call because what it depends on changes between calls: an agent's assurance can be suspended within minutes, one agent can act for many Principals with different permissions, and operations on one service differ in risk. Section 3.4.11 of {{I-D.ietf-wimse-arch}} requires that "each hop in the chain MUST explicitly scope and re-bind the security context"; recording that re-binding on both sides of every hop is what lets it be verified afterwards.

This document is short by design. It proposes one claim, one predicate type and one HTTP field, and defers everything else to the documents it cites.

## Conventions and Definitions

{::boilerplate bcp14-tagged}

The terms Agent, Agent Identity Management System and Workload are used as in {{I-D.ietf-wimse-aims}}. Actor and Delegation are used as in {{RFC8693}}, and Call Chain and Transaction as in {{I-D.ietf-oauth-transaction-tokens}}. Actor Chain, Admission, Agent Registration Authority, Agent Registration Statement, Assurance Statement, Bundle, Caller Reference, Calling Agent, Evidence Chain, Evidence Service, Execution Receipt, Linked Verification, Policy Pack, Principal Link, Serving Party and Supervisory Authority are used as defined in {{I-D.thaha-scitt-agent-execution-evidence}}, which states which of them have no equivalent in other IETF specifications. Issuer, Transparency Service, Signed Statement and Receipt are used as in {{RFC9943}}.

# Problem Statement

Section 11 of {{I-D.ietf-wimse-aims}} states that, at a minimum, audit events MUST record: the authenticated agent identifier; the delegated subject (user or system), when present; the resource or tool being accessed; the action requested and the authorization decision; a timestamp and a transaction or request correlation identifier; the posture assessment or risk state influencing the decision; and remediation or revocation events and their cause.

Five things are needed for a relying party to act on such a log, or on a call, that the framework does not supply:

Format:
: A field list is not a format. Two operators recording the same seven fields in their own schemas cannot be verified by one tool.

Discovery:
: A relying party presented with an agent credential has no standard way to learn which Evidence Service is expected to hold the agent's audit evidence, whether it is registered anywhere independent of the operator, or which policy was in force. Discovering and retrieving the evidence itself is a further step that requires deployment configuration or another protocol.

Binding:
: Even when the log is found, nothing in the credential ties the credential to the log. A log entry carrying an agent identifier is only as strong as the link between the identifier, the key, and the entries before and after it.

Admission:
: The claim lets a relying party find evidence after the fact, but a Serving Party needs to decide before acting, on every call, because assurance status and delegated authority can change between calls.

Chains:
: Correlating events across chains or systems needs additional context. Without it, each hop's evidence stands alone and cannot show who started a request, for which Principal, or whether authority widened along the way.

The remainder of this document addresses each in turn.

# Mapping of AIMS Minimum Fields to the Execution Receipt {#mapping}

The following list maps each minimum field of Section 11 of {{I-D.ietf-wimse-aims}} to the member of the Execution Receipt Statement defined in Section 6.7 of {{I-D.thaha-scitt-agent-execution-evidence}} that carries it. Integer keys are those of the CBOR form; names are those of the JSON form.

Authenticated agent identifier:
: `agent_id` (9), the runtime identity in force, which the Agent Credential Statement maps to a `logical_agent_id` issued by an Agent Registration Authority and binds to a key. On a Serving Party's `admission` receipt, `caller_agent_id` (20) is the calling agent's identifier as authenticated.

Delegated subject, when present:
: `principal` (10), with the Actor Chain `actor_chain` (23) when the agent acts for another agent's request, and `principal_link` (24) when two parties to a call must show they recorded the same Principal. Natural persons are carried as a peppered digest, not in clear.

Resource or tool being accessed:
: `target` (16) and `egress_host` (17). Tool name or model identifier; host for network egress.

Action requested and authorization decision:
: `record_type` (4), `decision` (6) and `request_digest` (12). `record_type` is an event category, not the requested operation; `decision` is one of allow, block, confirm or record as reported by the producer, and a confirm is followed by a receipt recording its allow or block outcome, which names it in `confirm_seq` (19); `request_digest` commits to the request bytes but does not disclose the requested action without a validated pre-image.

Timestamp and correlation identifier:
: `ts` (14), `seq` (2), `task_seq` (11) and `parent_seq` (5). `ts` is producer-declared. `seq` is unique within an Evidence Chain, and `parent_seq` links a tool call to the inference that requested it; both are interpreted inside one Evidence Chain, in which `task_seq` names the Task by the `seq` of its `task_start`. Across chains and systems, `txn` (25) is the transaction identifier of {{I-D.ietf-oauth-transaction-tokens}}, carried on both sides of every call, and an `admission` receipt's `caller_ref` (21) names the caller's receipt for the call. `txn` and `caller_ref` correlate the two sides; they do not show that both sides recorded the same request. `call_digest` (29) establishes that, as the two sides compute it over the same representation of the request. This follows the separation of correlation from matching in {{I-D.schrock-ep-authorization-evidence-chain}}. Equal sequence values in distinct chains do not identify the same event.

Posture or risk state influencing the decision:
: `policy_pack_digest` (7) and `config_integrity_digest` (8) commit to the policy and configuration the Evidence Service declares was in force. The applicable Assurance Statement records the assessed capability scope, risk assessment and monitoring summary; these are assessment-level values, not necessarily the per-event posture that influenced a decision. A richer per-event posture record can be carried by {{I-D.gilda-audit-agent-audit-record}}.

Remediation or revocation events and their cause:
: Revocation Statement (aee-type 8), Configuration Drift Statement (aee-type 4), an Assurance Statement disposition of reassess, suspend or withdraw, and a RESTRICTED or SUSPENDED status set by the Supervisory Authority, all registered on or referenced from the same Transparency Service. A refused call is recorded as `block`, at the caller's Decision Point or in the Serving Party's `admission` receipt. `reason_code` exists only on a Revocation Statement and carries a revocation cause; a Configuration Drift Statement carries `prev_config_digest`, `new_config_digest` and the changed entries instead. Recording drift, revocation or a disposition does not by itself prove that a remediation instruction was enforced; the enforcement outcome requires additional audit evidence.

The mapping is therefore partial: every AIMS minimum field has a carrier in a signed, hash-chained receipt or a registered statement referenced from it, but those carriers are commitments and producer-reported values rather than the underlying facts. A digest does not disclose its pre-image, a `decision` is what the producer recorded, policy and configuration digests commit to what the Evidence Service declares was in force, the Assurance Statement's risk state is assessment-level rather than per-event, and a recorded remediation event is not proof of enforcement. Missing decision context is disclosed by the format, not inferred from an event code or digest; deployments that need it SHOULD use the audit record of {{I-D.gilda-audit-agent-audit-record}}, linked as described in {{intoto}}.

# The aee_evidence Claim {#claim}

This section defines one claim. It MAY appear in a Workload Identity Token {{I-D.ietf-wimse-workload-creds}}, in a JWT or CWT access token issued to an agent under Section 10 of {{I-D.ietf-wimse-aims}}, or in any other JWT {{RFC7519}} or CWT {{RFC8392}} that identifies an agent. Recipients that do not understand it ignore it, as those specifications require.

~~~
Claim name: aee_evidence
JSON value: object
CBOR value: map
~~~

The value has the following members. `evidence_service`, `policy_pack_digest` and `logical_agent_id` are REQUIRED.

`evidence_service` (CBOR key 1), REQUIRED:
: A URI identifying the Evidence Service that issues Execution Epoch Statements, or individually registered Execution Receipt Statements, for this agent. The URI is the Issuer identifier that appears in the `iss` claim of those statements' CWT Claims header. It is an identifier, not necessarily a retrievable location.

`policy_pack_digest` (CBOR key 2), REQUIRED:
: The `pack_digest` of the Policy Pack Statement that governs this agent at the time the token is issued, in the digest form of {{I-D.thaha-scitt-agent-execution-evidence}}. In the JSON form, an object `{"alg": "sha-256", "value": "<base64url>"}`; in the CBOR form, the array `[alg, value]`.

`transparency_service` (CBOR key 3), OPTIONAL:
: The base URI of the Transparency Service with which the Evidence Service registers statements, and from which a relying party can resolve registration artifacts through {{I-D.ietf-scitt-scrapi}}. It identifies the service, not a particular Bundle or evidence period.

`agent_credential_digest` (CBOR key 4), OPTIONAL:
: The digest of the Agent Credential Statement payload that binds this agent's identifier to the key in the token's `cnf` claim. When present, the public key represented in the Agent Credential Statement MUST equal the key in `cnf`; equality is of the represented cryptographic public keys, not of the JWK or COSE_Key encodings, which can differ for the same key. Its presence enables the credential-key-bound result of {{rp}}; its absence leaves the claim as identity-and-policy correlation only.

`logical_agent_id` (CBOR key 5), REQUIRED:
: The persistent identifier of the agent across runtime environments, equal to the `logical_agent_id` of the Agent Credential and Agent Registration Statements: a `did:web` identifier {{DID-WEB}} in the domain of the Agent Registration Authority that issued it. Section 6 of {{I-D.ietf-wimse-aims}} requires that an agent be assigned exactly one WIMSE identifier; within any one such deployment, that identifier is the agent's runtime identity there, and `logical_agent_id` names the agent above the runtime identities of all its deployments.

`assurance_statement_digest` (CBOR key 6), OPTIONAL:
: The digest of the applicable Assurance Statement payload. The statement carries the authoritative `assurance_level`, assessed capability scope, risk assessment, monitoring summary, validity and status.

`assurance_level` (CBOR key 7) and `assurance_status` (CBOR key 8), OPTIONAL:
: The level of the Assurance Statement named by `assurance_statement_digest`, and the status value its token issuer observed in the statement's status list when issuing the token. They are a signed cache of the statement, for a fast admission decision, and MUST be present together and only with `assurance_statement_digest`. A token issuer MUST NOT include them unless it checked the status when issuing the token. A Serving Party MAY rely on them only if `status_checked_at` is present and well-formed, is not later than its clock plus its skew allowance, and is no older than the status freshness its policy requires for the operation; this is independent of the token's validity period. Otherwise it MUST NOT rely on them and obtains the status from the status list itself. If they disagree with the statement, the statement prevails.

`status_checked_at` (CBOR key 10), OPTIONAL:
: The time at which the token issuer observed `assurance_status` in an authenticated status list, in seconds since the Unix epoch (a NumericDate {{RFC7519}} in JSON). It is signed inside the token, and it MUST be present when `assurance_level` and `assurance_status` are present. The freshness rule above applies to the age of this observation, not to the remaining lifetime of the token: a token with 30 seconds left can carry an hour-old observation.

`registration_digest` (CBOR key 9), OPTIONAL:
: The digest of the Agent Registration Statement payload for `logical_agent_id`.

The claim identifies the expected Evidence Service, the policy commitment, the persistent logical identity, optional registration, credential and assurance bindings and an associated Transparency Service. It does not identify a particular Bundle or evidence period, and it is not a retrieval protocol: Bundle discovery and retrieval are supplied by deployment configuration or another protocol and are outside this document.

This document assumes a token profile in which the authenticated `sub` names the workload that is authenticating; `logical_agent_id` names the agent that workload is an instance of, and the two differ whenever an agent runs under more than one identity. Section 3.1.2 of {{I-D.ietf-wimse-arch}} states that a workload identifier "MAY represent a logical workload, a service implemented by one or more workloads, or a specific workload instance, depending on deployment policy", and that "two credentials containing the same workload identifier value represent the same workload only when validated under the same trust domain and issuer trust configuration". A relying party that receives tokens for the same agent from a development cluster, a production cluster and a cloud identity platform therefore sees three unrelated `sub` values. Carrying `logical_agent_id` in the token gives it the correlation key, and the Agent Credential Statement found through `evidence_service` gives it the signed, registered mapping from that key to each runtime identity and its validity window, so that correlation is verified rather than assumed. JWT and CWT are containers whose profiles assign different meanings to `sub`: in a profile where `sub` names a delegated user or system while the agent acts as a separate actor, the mapping from the token's subject to the agent's runtime identity MUST be separately specified, and {{rp}} does not apply to the token's `sub` directly.

Example, as it would appear in a WIT:

~~~ json
{
  "iss": "https://ids.example.com",
  "sub": "wimse://agents.example.com/agent/billing-assistant",
  "exp": 1790003600,
  "jti": "x-_1CTL2cca3CSE4cwb_l",
  "cnf": { "jwk": { "kty": "OKP", "crv": "Ed25519", "alg": "EdDSA",
           "x": "oJql9HpnWYAv-VX43C0qFKXJnSO-l_hkEn_5ODRVpPA" } },
  "aee_evidence": {
    "evidence_service": "https://harness.example/issuer",
    "policy_pack_digest": {
      "alg": "sha-256",
      "value": "VjoKOgwJt3O38H3WaTHcVmBcsOVtU9HanN7-auTFb00"
    },
    "transparency_service": "https://ts.example.net",
    "logical_agent_id":
      "did:web:register.example:agent:billing-assistant",
    "assurance_statement_digest": {
      "alg": "sha-256",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    },
    "assurance_level": 3,
    "assurance_status": 0,
    "status_checked_at": 1790001009
  }
}
~~~

## Relying Party Behaviour {#rp}

A relying party that receives a token carrying `aee_evidence` and that wishes to verify the agent's conduct:

1. Validates the containing token under its own profile, including issuer, protection, audience, validity and proof of possession where the profile uses one. None of the following steps adds trust to a token that fails its own validation.
2. Establishes the Evidence Service and Transparency Service trust anchors it accepts, obtained out of band or under an accepted retrieval and trust policy. A URI carried in the token, including `transparency_service`, is not a trust anchor, and keys reached from a token-supplied location become trusted only under that policy.
3. Identifies the evidence period it requires and whether it needs historical verification, that is, what was registered and what status evidence existed at that time, or current acceptance.
4. Obtains a Bundle for that period from the Evidence Service or from the agent's operator, by means outside this document.
5. Verifies the Bundle per Section 9 of {{I-D.thaha-scitt-agent-execution-evidence}} against the trust anchors of step 2.
6. Checks each of the following bindings, reporting each failure by kind:
   * issuer binding: the `iss` of the Execution Epoch Statements, or of individually registered Execution Receipt Statements, equals `evidence_service`;
   * runtime identity: the Agent Credential Statement lists the token's authenticated workload identity among its `runtime_identities` (in a token profile where `sub` is that identity, this is the token's `sub`);
   * logical identity: the Agent Credential Statement's `logical_agent_id` equals the claim's `logical_agent_id`, and the Agent Registration Statement it names was issued by an Agent Registration Authority the relying party accepts (and, if `registration_digest` is present, has that digest);
   * policy binding: every receipt's `policy_pack_digest` equals the claim's `policy_pack_digest`, or equals a registered descendant in the Policy Pack lineage that an explicit relying-party rule, an accepted Assurance Statement or another configured policy-evaluation result permits. Registration and ancestry do not by themselves establish that a descendant is semantically more restrictive, and a digest mismatch alone does not show that a policy was weaker or that execution under the declared policy occurred.
7. If `agent_credential_digest` is present, checks that the Agent Credential Statement in the Bundle has that digest and that the public key it represents equals the key in the token's `cnf`, compared as cryptographic keys rather than encodings. Success produces a credential-key-bound result; the claim's validity without `agent_credential_digest` is limited to the basic identity-and-policy correlation of the other steps.
8. If `assurance_statement_digest` is present, checks that the Bundle contains that Assurance Statement, that its `logical_agent_id`, credential, policy and configuration bindings match, and that its level, scope, validity, monitoring and status satisfy relying-party policy, applying configured freshness rules to the required status evidence. The absence of a Revocation Statement or of an adverse status entry in a supplied Bundle establishes only what that Bundle's snapshot supports; it does not establish current non-revocation.

An issuer, runtime-identity, logical-identity or policy-binding failure at step 6 is a distinct conclusion: evidence produced for a different agent is an identity failure, not a policy downgrade, and a policy mismatch is a downgrade conclusion only where the relying party's rules support it.

The claim does not itself make token validation depend on evidence availability. Token validation, workload authentication, access authorization and evidence acceptance are separate decisions: an access token does not necessarily function as an authentication credential, and acceptance for an operation is governed by the containing token's profile and relying-party policy. A relying party MAY require acceptable evidence before permitting an operation, and the absence of evidence cannot satisfy such a policy. A recipient that does not understand the claim ignores it; where evidence is required by policy, an unrecognized claim is not a successful evidence verification.

# Admission by a Serving Party {#admission}

A Serving Party that admits calls from agents only if they are registered and assured performs the following steps on every call, before acting on it. They decide the call; the steps of {{rp}} verify conduct after the fact, and the two are separate.

1. Validate the token and the proof of possession for this request under the applicable credential and authentication profiles; {{I-D.ietf-wimse-workload-creds}} defines the Workload Identity Token, while its proof-of-possession mechanisms are specified separately.
2. Determine the Assurance Statement and Agent Registration Statement that apply, from `aee_evidence` or by other configured means, and their status. The status MUST be no older than the freshness the Serving Party's policy requires for the operation. A token's `assurance_level` and `assurance_status` MAY be used as that status only under the rule on `status_checked_at` in {{claim}}; if that rule is not met, the Serving Party checks the status list itself. For operations its policy marks as high-risk, the Serving Party SHOULD check the status list itself.
3. Check that the registration is from an accepted Agent Registration Authority and is valid; that the Assurance Statement's level meets the minimum the Serving Party's policy sets for the operation, from an accepted assessor and scheme; and that its status is VALID, or RESTRICTED with the operation within the restricted class the scheme defines.
4. Check the Principal and every Actor in the Actor Chain ({{carrying}}) against its policy for the operation, including any status of the Principal's delegation and any minimum Principal assurance it requires.
5. Where `AEE-Caller-Ref` is present, compute `call_digest` over the request received, as defined in Section 6.7 of {{I-D.thaha-scitt-agent-execution-evidence}}; never use the value the caller presents. Refuse the call if `cd` is present and differs from the computed value, or if `cd` is absent while the Serving Party's policy requires linking. Refuse the call if its caller reference names a caller receipt that an earlier admission of this Serving Party already names (Section 6.7.2 of {{I-D.thaha-scitt-agent-execution-evidence}}).
6. Produce an `admission` receipt recording the decision and its basis, as Section 6.7.2 of {{I-D.thaha-scitt-agent-execution-evidence}} specifies, whether the call is admitted or refused. The receipt records the `call_digest` computed in step 5 and, in `admission_basis`, the time of the status observation relied on, which is the token's `status_checked_at` where the token's cached status was used. It is not the time of admission.
7. Act on the call, or refuse it.

A Serving Party that cannot complete a step refuses the call. The absence of evidence does not satisfy a policy that requires it.

A Serving Party cannot check the caller's `egress_host` against its own `hosts` at admission, because it does not see the caller's receipt. That check is made in Linked Verification (Section 9.1 of {{I-D.thaha-scitt-agent-execution-evidence}}).

# Carrying the Caller Reference and Actor Chain {#carrying}

## The AEE-Caller-Ref Field

A Calling Agent that makes an HTTP request to a Serving Party includes the `AEE-Caller-Ref` request header field. It is a Dictionary Structured Field {{RFC9651}} with the following members:

`es`:
: A String: the Issuer identifier of the Calling Agent's Evidence Service.

`seq`:
: An Integer: the `seq` of the Calling Agent's Execution Receipt for this call.

`h`:
: A Byte Sequence: the record-hash of that receipt.

`txn`:
: A String: the transaction identifier. When the request carries a Transaction Token {{I-D.ietf-oauth-transaction-tokens}}, it MUST equal that token's `txn` claim.

`cd`:
: A Byte Sequence: the `call_digest` value of the Calling Agent's receipt for this call, that is, the digest bytes only, which are SHA-256 for HTTP. It is REQUIRED when that receipt carries `call_digest`.

Unknown members are ignored. For example, with a line break added for display:

~~~ http-message
AEE-Caller-Ref: es="https://harness.example/issuer", seq=3,
  h=:ZyTJjSt4/phNskzi2MtjzCFBcZKOxPnrsJdw49kZb6c=:, txn="txn-0001",
  cd=:VE0BdgLT8sJbJj3IuKfBJKJ/RH+YIDY7qZeT1brtpg8=:
~~~

The Serving Party copies `es`, `seq`, `h` and `txn` into the `caller_ref` and `txn` of its `admission` receipt. It never copies `cd`: the `call_digest` of its receipt is the value it computed itself over the request it received ({{admission}}). They are the caller's claim until Linked Verification checks them against the caller's registered chain (Section 9.1 of {{I-D.thaha-scitt-agent-execution-evidence}}). The Calling Agent's receipt is produced before the request is sent, so the hash is available when the field is built.

## Actor Chain and Principal Link

The Actor Chain travels in the token presented on the call as nested `act` claims ({{Section 4.1 of RFC8693}}), the outermost naming the Calling Agent. Both parties record it as `actor_chain`, least recent first. Each party computes the `principal_link` as SHA-256 over the octets of the access token in the request's `Authorization` header field (not the Workload Identity Token or proof token), so no further field is needed. A Serving Party evaluates every Actor in the chain, not only the current one ({{admission}}).

## Other Protocols

Protocols other than HTTP that carry agent calls, such as tool-invocation protocols, can carry the same members in the metadata they provide for each request. This document does not define those bindings.

# Composition with the WIMSE Audit Record {#intoto}

{{I-D.gilda-audit-agent-audit-record}} defines an audit record as an in-toto Statement {{IN-TOTO}} in a DSSE envelope {{DSSE}}, canonicalized with {{RFC8785}}, with a predicate type of its own. That format is richer per event than an Execution Receipt and records vantage, posture and observed effect. The two are complementary: the audit record describes an authorization decision in depth; the Execution Receipt places the call on an identity-bound chain sealed into a Transparency Service.

To let one toolchain carry both, this document defines an in-toto predicate type for the Execution Receipt.

~~~
predicateType: urn:ietf:params:aee:predicate:execution-receipt
~~~

The predicate is the JSON form of an Execution Receipt as defined in Section 6.7 of {{I-D.thaha-scitt-agent-execution-evidence}}, unchanged. The Statement's `subject` MUST contain one entry whose `name` is the decimal `seq` of the receipt and whose `digest` contains `sha256` set to the hex-encoded SHA-256 of the JCS serialization {{RFC8785}} of the receipt JSON object, including `agent_sig` when present; this is the JSON-form record-hash of {{I-D.thaha-scitt-agent-execution-evidence}}. Conversion from the CBOR form changes the bytes and therefore the digest and the epoch inclusion proof: a JSON predicate converted from CBOR MUST NOT be presented as carrying the CBOR record-hash or its epoch proof. Where the CBOR chain must be preserved, the original artifact is carried and verified together with an explicit binding to the JSON representation. The DSSE `payloadType` is `application/vnd.in-toto+json`.

An audit record per {{I-D.gilda-audit-agent-audit-record}} and an Execution Receipt for the same call are associated through two verifiable commitments:

* The Execution Receipt's `request_digest` MAY be the digest of the audit record's `decision.requestDigest` pre-image, so that both commit to the same request bytes once the pre-image is validated.
* The audit record's `correlation.externalAnchor`, a member of the audit-record schema, with `kind` `transparency-log` MAY carry the SCITT Receipt {{RFC9942}} of the Execution Epoch Statement, or of the individual Execution Receipt Statement, that registers the receipt. A relying party validates the anchor under an explicitly defined anchor-validation procedure and verifies the receipt's inclusion in the named epoch. The proof establishes the Transparency Service's registration time for the receipt or epoch; it does not establish when the separately created audit record existed, or when the underlying action occurred.

Neither document is required for the other: deployments may implement either format independently where their requirements permit. Conformance to {{I-D.thaha-scitt-agent-execution-evidence}} or to {{I-D.gilda-audit-agent-audit-record}} is determined by each document's full set of applicable requirements, not by the presence of an artifact of the expected name, and the strength of a cross-format association depends on the verified commitments and registration proofs and on each format's observation scope. An operator that produces both and links them as above gives a relying party a sealed chain and a rich decision record for the same call.

In the terms of {{I-D.kuehlewind-audit-architecture}}, the Execution Receipt is an Action Record produced at the Harness vantage, the `admission` receipt is the corresponding record at the Serving Party, and the `aee_evidence` claim is part of the audit context carried with the agent's credential.

# Security Considerations

The claim is a pointer and a commitment, not a proof. It is protected by the signature on the token that carries it, and it is only as trustworthy as the identity server that issued the token. A compromised identity server can point a relying party at a colluding Evidence Service; the check is the Transparency Service, whose Receipts {{RFC9942}} are verifiable independently of both. Registration itself is limited evidence: a Receipt establishes that a statement was registered with a Transparency Service, not that the statement is truthful, that the evidence is complete, or that it covers all relevant activity ({{RFC9943}} describes the accuracy and selective-registration limits). Acceptance therefore also depends on trusted Issuers and Evidence Services, on any applicable runtime appraisal and on independent observation. Nor is a token-supplied location a trust anchor: Evidence Service and Transparency Service keys are trusted only when obtained out of band or under an accepted retrieval and trust policy, and following a validly signed pointer to an untrusted service does not make that service trusted.

The `policy_pack_digest` in the claim lets a relying party compare the declared policy commitment with the digests in receipts. It does not prevent downgrade; a relying party that does not check it gains nothing from it, and one that accepts any registered descendant of the declared pack accepts a weaker policy whenever an attacker can register one. Whether a descendant is acceptable belongs in explicit relying-party policy, not in the digest comparison itself.

An `assurance_statement_digest` is a binding, not a guarantee. The referenced statement can expire, become stale under its monitoring frequency, or be suspended or withdrawn after token issuance. A relying party that uses it MUST perform the SCITT verification and status checks at decision time. A Bundle is a snapshot of what its producer chose to include: the absence of revocation information in a supplied Bundle does not establish current non-revocation, and a relying party that requires current acceptance applies configured freshness rules to the status evidence.

`assurance_level` and `assurance_status` in a token can be as stale as the `status_checked_at` that the Serving Party's policy accepts; the token's validity period does not bound it. The freshness rule of {{claim}} bounds this, and the Serving Party's own status check for high-risk operations removes it where it matters most. `status_checked_at` is signed inside the token, so a token issuer that misstates it is detectable only against the status list. A Serving Party or relying party that requires tight freshness SHOULD check the status list itself for high-risk operations, as in {{admission}}.

The `AEE-Caller-Ref` field and the `act` claims are assertions by the Calling Agent. A field naming a receipt that does not exist fails Linked Verification with `E_CALLER_REF`. One naming a different real call, such as a payment of another amount under the same token and transaction, fails with `E_CALL_MISMATCH`, because the `call_digest` values differ. One naming the same request sent to a different service fails with `E_SERVING_HOST`, because the caller's `egress_host` is not among the `hosts` the Serving Party declared. A Serving Party refuses at admission a call whose `cd` differs from the value it computed. A replayed field is refused by the Serving Party that already admitted it, and detected by Linked Verification when used at another. A Serving Party that acts before verifying them relies on its own checks of the token and the Principal, not on the field.

Including `transparency_service` in the token reveals to any token recipient which Transparency Service the operator uses. Operators who consider that sensitive omit it and distribute the Transparency Service's identity out of band.

The security considerations of {{I-D.thaha-scitt-agent-execution-evidence}}, {{I-D.ietf-wimse-aims}} and {{RFC9943}} apply.

# Privacy Considerations

The claim carries no information about a Principal, no content, and no per-call data. It adds an Evidence Service identifier, a policy digest, a persistent `logical_agent_id`, and optional credential and Assurance Statement digests. The logical identifier intentionally makes one agent linkable across its runtime platforms; repeated digest values can also be correlated. A relying party MUST accept that correlation only through an Agent Credential Statement from an accepted Issuer that maps each runtime identity and trust domain to the logical agent. The digests do not disclose the committed payloads.

`AEE-Caller-Ref` reveals the Calling Agent's Evidence Service and a transaction identifier to the Serving Party, and the `act` claims reveal which operators' agents took part in a request. Calling Agents SHOULD send them only to the Serving Parties they call.

The privacy considerations of {{I-D.thaha-scitt-agent-execution-evidence}}, in particular its treatment of natural-person Principals, apply to the evidence the claim points to.

# IANA Considerations

## JSON Web Token Claims

IANA is requested to register the following claim in the "JSON Web Token Claims" registry {{RFC7519}}.

* Claim Name: aee_evidence
* Claim Description: Evidence service, policy, persistent identity and optional registration and assurance binding for agent execution evidence
* Change Controller: IETF
* Reference: {{claim}} of this document

## CBOR Web Token Claims

IANA is requested to register the following claim in the "CBOR Web Token (CWT) Claims" registry {{RFC8392}}.

* Claim Name: aee_evidence
* Claim Description: Evidence service, policy, persistent identity and optional registration and assurance binding for agent execution evidence
* JWT Claim Name: aee_evidence
* Claim Key: TBD1
* Claim Value Type: map
* Change Controller: IETF
* Reference: {{claim}} of this document

## HTTP Field Name

IANA is requested to register the following field in the "Hypertext Transfer Protocol (HTTP) Field Name Registry" per {{Section 16.3.1 of RFC9110}}:

* Field Name: AEE-Caller-Ref
* Status: permanent
* Structured Type: Dictionary
* Reference: {{carrying}} of this document

## IETF URN Sub-namespace

IANA is requested to register the sub-namespace `aee` in the "IETF URN Sub-namespace for Registered Protocol Parameter Identifiers" registry per {{RFC3553}}, with this document as the reference and the IETF as the change controller, and within it the identifier `urn:ietf:params:aee:predicate:execution-receipt` as defined in {{intoto}}.

--- back

# Acknowledgements
{:numbered="false"}

The authors thank the authors of {{I-D.ietf-wimse-aims}}, {{I-D.gilda-audit-agent-audit-record}} and {{I-D.kuehlewind-audit-architecture}}, whose work this document is intended to connect rather than duplicate. The authors thank Iman Schrock for her review of linked verification and status freshness in the -00 drafts.

# Changes since -00
{:numbered="false"}

This section is to be removed before publication as an RFC.

* Added `status_checked_at` (CBOR key 10) to `aee_evidence`. The freshness rule now applies to the age of the status observation, independent of token validity, and the "remaining lifetime" rule is removed ({{claim}}).
* Added the `cd` member to `AEE-Caller-Ref`, carrying the caller's `call_digest`, and regenerated the example ({{carrying}}).
* A Serving Party computes its own `call_digest`, and refuses a call whose `cd` differs. A Serving Party MUST refuse a caller reference it has already admitted. The admission receipt records `call_digest` and the status observation time ({{admission}}).
* Corrected the statement in the Security Considerations that a forged caller reference always fails Linked Verification; the failure cases and the replay rule are now listed.
* Updated references to the -01 revision of the SCITT draft, and added EP-AEC as an informative reference.
