---
v: 3
title: "Evidence Binding for AI Agent Credentials"
abbrev: "Agent Evidence Binding"
docname: draft-thaha-wimse-agent-evidence-binding-00
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
  I-D.thaha-scitt-agent-execution-evidence:
    title: "Agent Execution Evidence: A SCITT Profile for Verifiable Records of AI Agent Runs"
    author:
      - ins: S. Thaha
      - ins: S. Shamsudeen
    date: 2026-10
    seriesinfo:
      Internet-Draft: draft-thaha-scitt-agent-execution-evidence-00
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
  I-D.ietf-wimse-s2s-protocol:
    title: WIMSE Workload-to-Workload Authentication
    author:
      - ins: B. Campbell
      - ins: J. Salowey
      - ins: A. Schwenkschuster
      - ins: Y. Sheffer
    date: 2025-10
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-s2s-protocol-07
  I-D.ietf-wimse-arch:
    title: Workload Identity in a Multi System Environment (WIMSE) Architecture
    author:
      - ins: J. Salowey
      - ins: Y. Rosomakho
      - ins: H. Tschofenig
    date: 2026-07
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-arch-08
  I-D.ietf-wimse-identifier:
    title: Workload Identifier
    author:
      - ins: Y. Rosomakho
      - ins: J. Salowey
    date: 2026-07
    seriesinfo:
      Internet-Draft: draft-ietf-wimse-identifier-03
  I-D.gilda-wimse-agent-audit-record:
    title: An Audit Record Format for AI Agent Authorization Decisions
    author:
      - ins: S. Gilda
    date: 2026-09
    seriesinfo:
      Internet-Draft: draft-gilda-wimse-agent-audit-record-01
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
  DSSE:
    title: Dead Simple Signing Envelope
    author:
      - org: secure-systems-lab
    date: 2023
    target: https://github.com/secure-systems-lab/dsse

--- abstract

The WIMSE AI Identity Management System (AIMS) requires tamper-evident agent audit logs but does not specify their format or discovery. This document maps the AIMS minimum fields to the SCITT Agent Execution Evidence profile, defines one claim that binds a workload credential to the persistent agent, governing policy, expected Evidence Service and optional Assurance Statement, and defines an in-toto predicate type for carrying Execution Receipts in the audit format proposed for WIMSE. It is input to the AIMS work and makes no change to it.

--- middle

# Introduction

Section 11 of {{I-D.ietf-wimse-aims}} ("Agent Monitoring, Observability and Remediation") requires tamper-evident audit logs and lists the fields an audit event must record at a minimum. Section 8 states that evidence formats are out of scope, and Section 13 states that compliance criteria are out of scope. That is a reasonable division: an identity management framework should not pick a log format. It leaves two practical questions open for an implementer:

1. In what format are the seven minimum fields recorded so that a party other than the operator can verify them?
2. Given an agent's credential, how does a relying party learn which Evidence Service and policy to expect that evidence under, and which assurance statement applies?

{{I-D.thaha-scitt-agent-execution-evidence}} answers the first question with per-call Execution Receipts and Assurance Statements registered through SCITT {{RFC9943}}. This document answers the second with one claim, `aee_evidence`, that an identity server MAY place in a Workload Identity Token {{I-D.ietf-wimse-s2s-protocol}} or other agent token. It also maps the AIMS fields and defines an in-toto predicate so that the formats compose with {{I-D.gilda-wimse-agent-audit-record}}.

This document is short by design. It proposes one claim and one predicate type and defers everything else to the documents it cites.

## Conventions and Definitions

{::boilerplate bcp14-tagged}

The terms Agent, Agent Identity Management System and Workload are used as in {{I-D.ietf-wimse-aims}}. Assurance Statement, Execution Receipt, Evidence Service, Evidence Chain, Policy Pack and Bundle are used as in {{I-D.thaha-scitt-agent-execution-evidence}}. Issuer, Transparency Service, Signed Statement and Receipt are used as in {{RFC9943}}.

# Problem Statement

Section 11 of {{I-D.ietf-wimse-aims}} states that, at a minimum, audit events MUST record: the authenticated agent identifier; the delegated subject (user or system), when present; the resource or tool being accessed; the action requested and the authorization decision; a timestamp and a transaction or request correlation identifier; the posture assessment or risk state influencing the decision; and remediation or revocation events and their cause.

Three things are needed for a relying party to act on such a log that the framework does not supply:

Format:
: A field list is not a format. Two operators recording the same seven fields in their own schemas cannot be verified by one tool.

Discovery:
: A relying party presented with an agent credential has no standard way to learn which Evidence Service is expected to hold the agent's audit evidence, whether it is registered anywhere independent of the operator, or which policy was in force. Discovering and retrieving the evidence itself is a further step that requires deployment configuration or another protocol.

Binding:
: Even when the log is found, nothing in the credential ties the credential to the log. A log entry carrying an agent identifier is only as strong as the link between the identifier, the key, and the entries before and after it.

The remainder of this document addresses each in turn.

# Mapping of AIMS Minimum Fields to the Execution Receipt {#mapping}

The following list maps each minimum field of Section 11 of {{I-D.ietf-wimse-aims}} to the member of the Execution Receipt Statement defined in Section 5.4 of {{I-D.thaha-scitt-agent-execution-evidence}} that carries it. Integer keys are those of the CBOR form; names are those of the JSON form.

Authenticated agent identifier:
: `agent_id` (9), the runtime identity in force, which the Agent Credential Statement maps to a `logical_agent_id` and binds to a key.

Delegated subject, when present:
: `principal` (10). Natural persons are carried as a peppered digest, not in clear.

Resource or tool being accessed:
: `target` (16) and `egress_host` (17). Tool name or model identifier; host for network egress.

Action requested and authorization decision:
: `record_type` (4), `decision` (6) and `request_digest` (12). `record_type` is an event category, not the requested operation; `decision` is one of allow, block, confirm or record as reported by the producer; `request_digest` commits to the request bytes but does not disclose the requested action without a validated pre-image.

Timestamp and correlation identifier:
: `ts` (14), `seq` (2), `task_seq` (11) and `parent_seq` (5). `ts` is producer-declared. `seq` together with `agent_id` is unique per chain, and `parent_seq` links a tool call to the inference that requested it; both are interpreted inside one Evidence Chain, and `task_seq` inside one Task. Correlation across chains, Tasks or systems needs additional context; equal sequence values in distinct chains do not identify the same event.

Posture or risk state influencing the decision:
: `policy_pack_digest` (7) and `config_integrity_digest` (8) commit to the policy and configuration the Evidence Service declares was in force. The applicable Assurance Statement records the assessed capability scope, risk assessment and monitoring summary; these are assessment-level values, not necessarily the per-event posture that influenced a decision. A richer per-event posture record can be carried by {{I-D.gilda-wimse-agent-audit-record}}.

Remediation or revocation events and their cause:
: Revocation Statement (aee-type 8), Configuration Drift Statement (aee-type 4), and an Assurance Statement disposition of reassess, suspend or withdraw, all registered on the same Transparency Service. `reason_code` exists only on a Revocation Statement and carries a revocation cause; a Configuration Drift Statement carries `prev_config_digest`, `new_config_digest` and the changed entries instead. Recording drift, revocation or a disposition does not by itself prove that a remediation instruction was enforced; the enforcement outcome requires additional audit evidence.

The mapping is therefore partial: every AIMS minimum field has a carrier in a signed, hash-chained receipt or a registered statement referenced from it, but those carriers are commitments and producer-reported values rather than the underlying facts. A digest does not disclose its pre-image, a `decision` is what the producer recorded, policy and configuration digests commit to what the Evidence Service declares was in force, the Assurance Statement's risk state is assessment-level rather than per-event, and a recorded remediation event is not proof of enforcement. Missing decision context is disclosed by the format, not inferred from an event code or digest; deployments that need it SHOULD use the audit record of {{I-D.gilda-wimse-agent-audit-record}}, linked as described in {{intoto}}.

# The aee_evidence Claim {#claim}

This section defines one claim. It MAY appear in a Workload Identity Token {{I-D.ietf-wimse-s2s-protocol}}, in a JWT or CWT access token issued to an agent under Section 10 of {{I-D.ietf-wimse-aims}}, or in any other JWT {{RFC7519}} or CWT {{RFC8392}} that identifies an agent. Recipients that do not understand it ignore it, as those specifications require.

~~~
Claim name: aee_evidence
JSON value: object
CBOR value: map
~~~

The value has the following members. `evidence_service`, `policy_pack_digest` and `logical_agent_id` are REQUIRED.

`evidence_service` (CBOR key 1), REQUIRED:
: A URI identifying the Evidence Service that issues Execution Receipt Statements for this agent. The URI is the Issuer identifier that appears in the `iss` claim of those statements' CWT Claims header. It is an identifier, not necessarily a retrievable location.

`policy_pack_digest` (CBOR key 2), REQUIRED:
: The `pack_digest` of the Policy Pack Statement that governs this agent at the time the token is issued, in the digest form of {{I-D.thaha-scitt-agent-execution-evidence}}. In the JSON form, an object `{"alg": "sha-256", "value": "<base64url>"}`; in the CBOR form, the array `[alg, value]`.

`transparency_service` (CBOR key 3), OPTIONAL:
: The base URI of the Transparency Service with which the Evidence Service registers statements, and from which a relying party can resolve registration artifacts through {{I-D.ietf-scitt-scrapi}}. It identifies the service, not a particular Bundle or evidence period.

`agent_credential_digest` (CBOR key 4), OPTIONAL:
: The digest of the Agent Credential Statement payload that binds this agent's identifier to the key in the token's `cnf` claim. When present, the public key represented in the Agent Credential Statement MUST equal the key in `cnf`; equality is of the represented cryptographic public keys, not of the JWK or COSE_Key encodings, which can differ for the same key. Its presence enables the credential-key-bound result of {{rp}}; its absence leaves the claim as identity-and-policy correlation only.

`logical_agent_id` (CBOR key 5), REQUIRED:
: The persistent identifier of the agent across runtime environments, equal to the `logical_agent_id` of the Agent Credential Statement; a Workload Identifier {{I-D.ietf-wimse-identifier}} or a `did:web` identifier, never a newly minted scheme.

`assurance_statement_digest` (CBOR key 6), OPTIONAL:
: The digest of the applicable Assurance Statement payload. The statement, rather than this token claim, carries `assurance_level`, assessed capability scope, risk assessment, monitoring summary, validity and status. This avoids copying assurance values into credentials where they can become stale.

The claim identifies the expected Evidence Service, the policy commitment, the persistent logical identity, optional credential and assurance bindings and an associated Transparency Service. It does not identify a particular Bundle or evidence period, and it is not a retrieval protocol: Bundle discovery and retrieval are supplied by deployment configuration or another protocol and are outside this document.

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
      "did:web:agents.example.com:billing-assistant",
    "assurance_statement_digest": {
      "alg": "sha-256",
      "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
  }
}
~~~

## Relying Party Behaviour {#rp}

A relying party that receives a token carrying `aee_evidence` and that wishes to verify the agent's conduct:

1. Validates the containing token under its own profile, including issuer, protection, audience, validity and proof of possession where the profile uses one. None of the following steps adds trust to a token that fails its own validation.
2. Establishes the Evidence Service and Transparency Service trust anchors it accepts, obtained out of band or under an accepted retrieval and trust policy. A URI carried in the token, including `transparency_service`, is not a trust anchor, and keys reached from a token-supplied location become trusted only under that policy.
3. Identifies the evidence period it requires and whether it needs historical verification, that is, what was registered and what status evidence existed at that time, or current acceptance.
4. Obtains a Bundle for that period from the Evidence Service or from the agent's operator, by means outside this document.
5. Verifies the Bundle per Section 8 of {{I-D.thaha-scitt-agent-execution-evidence}} against the trust anchors of step 2.
6. Checks each of the following bindings, reporting each failure by kind:
   * issuer binding: the `iss` of the Execution Receipt Statements equals `evidence_service`;
   * runtime identity: the Agent Credential Statement lists the token's authenticated workload identity among its `runtime_identities` (in a token profile where `sub` is that identity, this is the token's `sub`);
   * logical identity: the Agent Credential Statement's `logical_agent_id` equals the claim's `logical_agent_id`;
   * policy binding: every receipt's `policy_pack_digest` equals the claim's `policy_pack_digest`, or equals a registered descendant in the Policy Pack lineage that an explicit relying-party rule, an accepted Assurance Statement or another configured policy-evaluation result permits. Registration and ancestry do not by themselves establish that a descendant is semantically more restrictive, and a digest mismatch alone does not show that a policy was weaker or that execution under the declared policy occurred.
7. If `agent_credential_digest` is present, checks that the Agent Credential Statement in the Bundle has that digest and that the public key it represents equals the key in the token's `cnf`, compared as cryptographic keys rather than encodings. Success produces a credential-key-bound result; the claim's validity without `agent_credential_digest` is limited to the basic identity-and-policy correlation of the other steps.
8. If `assurance_statement_digest` is present, checks that the Bundle contains that Assurance Statement, that its `logical_agent_id`, credential, policy and configuration bindings match, and that its level, scope, validity, monitoring and status satisfy relying-party policy, applying configured freshness rules to the required status evidence. The absence of a Revocation Statement or of an adverse status entry in a supplied Bundle establishes only what that Bundle's snapshot supports; it does not establish current non-revocation.

An issuer, runtime-identity, logical-identity or policy-binding failure at step 6 is a distinct conclusion: evidence produced for a different agent is an identity failure, not a policy downgrade, and a policy mismatch is a downgrade conclusion only where the relying party's rules support it.

The claim does not itself make token validation depend on evidence availability. Token validation, workload authentication, access authorization and evidence acceptance are separate decisions: an access token does not necessarily function as an authentication credential, and acceptance for an operation is governed by the containing token's profile and relying-party policy. A relying party MAY require acceptable evidence before permitting an operation, and the absence of evidence cannot satisfy such a policy. A recipient that does not understand the claim ignores it; where evidence is required by policy, an unrecognized claim is not a successful evidence verification.

# Composition with the WIMSE Audit Record {#intoto}

{{I-D.gilda-wimse-agent-audit-record}} defines an audit record as an in-toto Statement {{IN-TOTO}} in a DSSE envelope {{DSSE}}, canonicalized with {{RFC8785}}, with a predicate type of its own. That format is richer per event than an Execution Receipt and records vantage, posture and observed effect. The two are complementary: the audit record describes an authorization decision in depth; the Execution Receipt places the call on an identity-bound chain sealed into a Transparency Service.

To let one toolchain carry both, this document defines an in-toto predicate type for the Execution Receipt.

~~~
predicateType: urn:ietf:params:aee:predicate:execution-receipt
~~~

The predicate is the JSON form of an Execution Receipt as defined in Section 5.4 of {{I-D.thaha-scitt-agent-execution-evidence}}, unchanged. The Statement's `subject` MUST contain one entry whose `name` is the decimal `seq` of the receipt and whose `digest` contains `sha256` set to the hex-encoded SHA-256 of the JCS serialization {{RFC8785}} of the receipt JSON object, including `agent_sig` when present; this is the JSON-form record-hash of {{I-D.thaha-scitt-agent-execution-evidence}}. Conversion from the CBOR form changes the bytes and therefore the digest and the epoch inclusion proof: a JSON predicate converted from CBOR MUST NOT be presented as carrying the CBOR record-hash or its epoch proof. Where the CBOR chain must be preserved, the original artifact is carried and verified together with an explicit binding to the JSON representation. The DSSE `payloadType` is `application/vnd.in-toto+json`.

An audit record per {{I-D.gilda-wimse-agent-audit-record}} and an Execution Receipt for the same call are associated through two verifiable commitments:

* The Execution Receipt's `request_digest` MAY be the digest of the audit record's `decision.requestDigest` pre-image, so that both commit to the same request bytes once the pre-image is validated.
* The audit record's `correlation.externalAnchor`, a member of the audit-record schema, with `kind` `transparency-log` MAY carry the SCITT Receipt {{RFC9942}} of the Execution Epoch Statement, or of the individual Execution Receipt Statement, that registers the receipt. A relying party validates the anchor under an explicitly defined anchor-validation procedure and verifies the receipt's inclusion in the named epoch. The proof establishes the Transparency Service's registration time for the receipt or epoch; it does not establish when the separately created audit record existed, or when the underlying action occurred.

Neither document is required for the other: deployments may implement either format independently where their requirements permit. Conformance to {{I-D.thaha-scitt-agent-execution-evidence}} or to {{I-D.gilda-wimse-agent-audit-record}} is determined by each document's full set of applicable requirements, not by the presence of an artifact of the expected name, and the strength of a cross-format association depends on the verified commitments and registration proofs and on each format's observation scope. An operator that produces both and links them as above gives a relying party a sealed chain and a rich decision record for the same call.

In the terms of {{I-D.kuehlewind-audit-architecture}}, the Execution Receipt is an Action Record produced at the Harness vantage and the `aee_evidence` claim is part of the audit context carried with the agent's credential.

# Security Considerations

The claim is a pointer and a commitment, not a proof. It is protected by the signature on the token that carries it, and it is only as trustworthy as the identity server that issued the token. A compromised identity server can point a relying party at a colluding Evidence Service; the check is the Transparency Service, whose Receipts {{RFC9942}} are verifiable independently of both. Registration itself is limited evidence: a Receipt establishes that a statement was registered with a Transparency Service, not that the statement is truthful, that the evidence is complete, or that it covers all relevant activity ({{RFC9943}} describes the accuracy and selective-registration limits). Acceptance therefore also depends on trusted Issuers and Evidence Services, on any applicable runtime appraisal and on independent observation. Nor is a token-supplied location a trust anchor: Evidence Service and Transparency Service keys are trusted only when obtained out of band or under an accepted retrieval and trust policy, and following a validly signed pointer to an untrusted service does not make that service trusted.

The `policy_pack_digest` in the claim lets a relying party compare the declared policy commitment with the digests in receipts. It does not prevent downgrade; a relying party that does not check it gains nothing from it, and one that accepts any registered descendant of the declared pack accepts a weaker policy whenever an attacker can register one. Whether a descendant is acceptable belongs in explicit relying-party policy, not in the digest comparison itself.

An `assurance_statement_digest` is a binding, not a guarantee. The referenced statement can expire, become stale under its monitoring frequency, or be suspended or withdrawn after token issuance. A relying party that uses it MUST perform the SCITT verification and status checks at decision time. A Bundle is a snapshot of what its producer chose to include: the absence of revocation information in a supplied Bundle does not establish current non-revocation, and a relying party that requires current acceptance applies configured freshness rules to the status evidence.

Including `transparency_service` in the token reveals to any token recipient which Transparency Service the operator uses. Operators who consider that sensitive omit it and distribute the Transparency Service's identity out of band.

The security considerations of {{I-D.thaha-scitt-agent-execution-evidence}}, {{I-D.ietf-wimse-aims}} and {{RFC9943}} apply.

# Privacy Considerations

The claim carries no information about a Principal, no content, and no per-call data. It adds an Evidence Service identifier, a policy digest, a persistent `logical_agent_id`, and optional credential and Assurance Statement digests. The logical identifier intentionally makes one agent linkable across its runtime platforms; repeated digest values can also be correlated. A relying party MUST accept that correlation only through an Agent Credential Statement from an accepted Issuer that maps each runtime identity and trust domain to the logical agent. The digests do not disclose the committed payloads.

The privacy considerations of {{I-D.thaha-scitt-agent-execution-evidence}}, in particular its treatment of natural-person Principals, apply to the evidence the claim points to.

# IANA Considerations

## JSON Web Token Claims

IANA is requested to register the following claim in the "JSON Web Token Claims" registry {{RFC7519}}.

* Claim Name: aee_evidence
* Claim Description: Evidence service, policy, persistent identity and optional assurance binding for agent execution evidence
* Change Controller: IETF
* Reference: {{claim}} of this document

## CBOR Web Token Claims

IANA is requested to register the following claim in the "CBOR Web Token (CWT) Claims" registry {{RFC8392}}.

* Claim Name: aee_evidence
* Claim Description: Evidence service, policy, persistent identity and optional assurance binding for agent execution evidence
* JWT Claim Name: aee_evidence
* Claim Key: TBD1
* Claim Value Type: map
* Change Controller: IETF
* Reference: {{claim}} of this document

## IETF URN Sub-namespace

IANA is requested to register the sub-namespace `aee` in the "IETF URN Sub-namespace for Registered Protocol Parameter Identifiers" registry per {{RFC3553}}, with this document as the reference and the IETF as the change controller, and within it the identifier `urn:ietf:params:aee:predicate:execution-receipt` as defined in {{intoto}}.

--- back

# Acknowledgements
{:numbered="false"}

The authors thank the authors of {{I-D.ietf-wimse-aims}}, {{I-D.gilda-wimse-agent-audit-record}} and {{I-D.kuehlewind-audit-architecture}}, whose work this document is intended to connect rather than duplicate.
