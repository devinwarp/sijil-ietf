# Draft list posts

Both posts go out before Datatracker submission (see OPEN_ITEMS.md deadlines):
`scitt@ietf.org` first, then `wimse@ietf.org`, then submit the SCITT draft,
then the WIMSE draft. Adjust names/affiliations before sending.

---

## scitt@ietf.org

**Subject:** Individual draft: evidence statements for AI agent execution
(`draft-thaha-scitt-agent-execution-evidence-00`)

Hello SCITT,

We have prepared an individual draft that profiles SCITT for recording what
autonomous and semi-autonomous software agents actually did:

  draft-thaha-scitt-agent-execution-evidence-00

The document defines a set of Signed Statement types for agent execution
evidence, registered on a Transparency Service so a relying party can hold an
agent's operator to a tamper-evident trail:

  - Agent Credential Statement — binds a logical agent identity to the
    runtime identities it presents, with validity windows, lifecycle class
    (ephemeral / persistent / derived) and a derived-agent relationship;
  - Policy Pack Statement — commits to the policy in force, with a layering
    and parent-pack mechanism for jurisdiction- and sector-level packs;
  - Configuration Integrity Statement — commits to the agent's
    instruction/configuration files as typed, Unicode-normalised digests;
  - Execution Receipt and Execution Epoch — commit to hash-chained
    execution records and a Merkle root per epoch, so completeness can be
    appraised rather than spot-checked;
  - Assurance Statement — a signed assessment (levels 1-4) by an assessor,
    binding the credential, policy and configuration digests plus an
    assessed scope, with status-list-based revocation;
  - Revocation Statement — with reason codes for credential and assurance
    withdrawal.

Two design decisions we would particularly like review on:

1. The identity-continuity model. Following draft-ietf-wimse-arch-08
   Section 3.1.2, the draft treats a runtime identity as meaningful only
   inside its trust domain and records the logical-agent-to-runtime-identity
   mapping as signed, registered statements rather than assuming
   correlation. Is that a reasonable use of registered statements, or does
   the WG see a better home for it?

2. The limits we state: a SCITT receipt proves registration under a
   Transparency Service, not the truthfulness or completeness of the
   underlying claims. The draft places the truthfulness burden on the
   Assurance Statement and the completeness burden on epoch proofs, and
   says so explicitly. Does this match how the WG expects transparency to
   be described?

The draft is ~40 pages including a complete worked example and test
vectors. Source and generated artifacts:

  https://github.com/devinwarp/sijil-ietf

Comments welcome on any part; the two points above are where reviewer time
would help most.

Best regards,
Shameer Thaha / Shaibi Shamsudeen

---

## wimse@ietf.org

**Subject:** Individual draft: binding WIMSE credentials to agent evidence —
`draft-thaha-wimse-agent-evidence-binding-00`

Hello WIMSE,

We have prepared an individual draft that adds a single claim to WIMSE
workload credentials so a relying party can reach the evidence trail of an
agentic workload:

  draft-thaha-wimse-agent-evidence-binding-00

The motivation is a gap we see for agent workloads specifically. Section
3.1.2 of draft-ietf-wimse-arch-08 states that a workload identifier "MAY
represent a logical workload, a service implemented by one or more
workloads, or a specific workload instance, depending on deployment
policy", and that "two credentials containing the same workload identifier
value represent the same workload only when validated under the same trust
domain and issuer trust configuration." An agent that runs under a SPIFFE
identity in a development cluster, a WIMSE identity in a production
cluster, and a cloud workload identity in a SaaS environment therefore
presents three unrelated `sub` values, and nothing in the token ties them
to one agent or to its evidence.

The draft is deliberately narrow. It defines:

  - one claim, `aee_evidence` (for JWT and CWT), carrying a required
    `logical_agent_id`, the expected `evidence_service`, the
    `policy_pack_digest`, and optional `agent_credential_digest`,
    `assurance_statement_digest` and `transparency_service`; and
  - one in-toto predicate type that carries the corresponding Execution
    Receipt (a signed statement in the companion SCITT draft,
    draft-thaha-scitt-agent-execution-evidence-00).

It does not define a bundle retrieval protocol, a registry, a status
service, or a policy language. `evidence_service` identifies the expected
Evidence Service; it is not necessarily a retrieval endpoint, and the draft
says so.

Points we would like review on:

1. The `sub`/`logical_agent_id` split. The draft assumes a token profile
   in which `sub` names the authenticating workload and `logical_agent_id`
   names the agent that workload is an instance of. In profiles where `sub`
   names a delegated user or system instead, the draft defers to the
   profile. Does this sit correctly with how the WG expects `sub` to be
   used?

2. Evidence acceptance is separated from token validation: a token can be
   cryptographically valid while the operation is refused because required
   evidence is missing or unacceptable, and the relying-party procedure
   fails the issuer, runtime-identity, logical-identity and policy bindings
   separately rather than collapsing them into one "downgrade" verdict.

3. Whether this mechanism belongs in a WIMSE document at all, or is better
   kept as an individual submission.

Source and generated artifacts:

  https://github.com/devinwarp/sijil-ietf

Best regards,
Shameer Thaha / Shaibi Shamsudeen
