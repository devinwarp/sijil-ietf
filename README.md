# sijil-ietf

Two individual Internet-Drafts on verifiable evidence for AI agent runs.

| Draft | Intended WG | Status | Pages (txt) |
|-------|-------------|--------|-------------|
| `draft-thaha-scitt-agent-execution-evidence-00` | SCITT | Standards Track, individual | 40 |
| `draft-thaha-wimse-agent-evidence-binding-00` | WIMSE (input to AIMS) | Informational, individual | 14 |

Each draft is present as `.md` (kramdown-rfc source), `.xml` (RFCXML v3), `.txt` and `.html`.
`vectors/make_vectors.py` regenerates the Appendix A test vectors of the SCITT draft
(Ed25519, deterministic seeds; `vectors/vectors.txt` and the three `.cose` files are its output).

## Rebuilding

```
pip install xml2rfc cbor2 pynacl
gem install kramdown-rfc            # or build from https://github.com/cabo/kramdown-rfc
kramdown-rfc2629 --v3 draft-thaha-scitt-agent-execution-evidence-00.md > draft-thaha-scitt-agent-execution-evidence-00.xml
xml2rfc --text --pagination --html draft-thaha-scitt-agent-execution-evidence-00.xml
```

All references are defined inline in the YAML front matter, so no network access is needed
at build time except for the two BCP 14 references the `{::boilerplate bcp14-tagged}` macro
adds; `.refcache/` carries those two bibxml files so the build also works offline.

Before submitting, run `idnits` (https://author-tools.ietf.org/idnits) against each `.txt`.

## Changes in this revision (post external review, 2026-10-03)

SCITT draft:
- Agent Credential Statement gains `logical_agent_id` (WIMSE identifier or did:web, never a new scheme), `responsible_entity`, `runtime_identities[]` ({identifier, scheme, trust_domain, valid_from, valid_until}), `lifecycle_class` {ephemeral, persistent, derived} and `derived_from`; motivation cites draft-ietf-wimse-arch-08 Section 3.1.2 verbatim.
- Execution Receipt `agent_id` is now explicitly the runtime identity in force; verification step 5 (`E_RUNTIME_IDENTITY`) checks it against the credential's `runtime_identities` window.
- "Conformance Receipt Statement" renamed "Assurance Statement" and extended with declared purpose, objectives, intended use, effective model/tool/data/permission/delegation scope, risk assessment, time-bounded monitoring, reassessment, suspension and withdrawal. It retains the original `assurance_level` field with levels 1 through 4 and introduces no new acronym for it.
- New "Derivable Risk Facts" subsection under Meaning of PASS (autonomy ratio; private inference witness), no thresholds.
- Registration Policy checks the new credential fields and the assessor rule structurally.
- Appendix B trimmed to one three-row table; Appendix A compacted (full COSE objects live in `vectors/`). Prose condensed throughout to offset growth.
- Shaibi Shamsudeen is added as the second author; the placeholder acknowledgement is removed.
- Test vectors regenerated: `agent-credential.cose` now carries keys 9-12 (payload digest `78609922...3389`); receipt and epoch vectors unchanged.

WIMSE draft:
- `aee_evidence` gains a REQUIRED `logical_agent_id` (CBOR key 5) with a paragraph on why, citing the same WIMSE architecture sentences; relying-party step 3 and IANA descriptions updated.
- `aee_evidence` gains an OPTIONAL `assurance_statement_digest` (CBOR key 6). Assurance level, capability scope, risk, monitoring, validity and status remain solely in the SCITT Assurance Statement.
- The Execution Receipt predicate cross-reference is corrected from SCITT Section 4.1 to Section 5.4, and Shaibi Shamsudeen is added as the second author.

Rendering succeeds for both drafts. The revised SCITT draft is 40 paginated text pages and the WIMSE draft is 14. Both pass the official IETF `idnits` submission check. IETF guidance sets no fixed page limit; the complete test-vector appendix remains in the SCITT draft.

## Submission plan

Deadline that matters: the IETF 127 Internet-Draft submission cut-off is
**Monday 2026-11-02, 23:59 UTC** (applies to all drafts, including -00).
IETF 127 is in San Francisco, 2026-11-14 onward. Draft WG agendas are due 2026-11-04,
so chairs will decide agenda slots in the days right after the cut-off.

Recommended order:

1. **Post to the lists first, before Datatracker submission.**
   A -00 that appears on a WG list with a short cover note before it appears in the
   Datatracker gets read; one that appears cold does not. Send one message per list,
   attach nothing, link the `.txt` and `.html` from the GitHub repository named in the
   draft header.

   - `scitt@ietf.org`: the SCITT draft. Lead with the three gaps (identity-to-chain
     binding, configuration integrity, revocable conformance) and the Registration
     Policy section, since that is the WG's work item from the audit architecture draft
     (WI-3). Name the related SCITT agent drafts (Mih, Toraman, Emirdag) and say the
     Related Work section is an invitation to align vocabularies, not a competing
     proposal. Ask for a 10-minute slot at IETF 127.
   - `wimse@ietf.org`: the WIMSE draft, with the SCITT draft linked as the companion.
     Lead with the AIMS Section 11 mapping and the single `aee_evidence` claim. Copy
     the AIMS authors. Say explicitly it is input to AIMS and makes no change to it.
     Ask whether the AIMS editors would rather absorb the claim than see a separate
     document.

2. **Submit both drafts via the Datatracker** at https://datatracker.ietf.org/submit
   within a day or two of the list posts and no later than 2026-11-02 23:59 UTC.
   Upload the `.xml` (xml2rfc v3 is the preferred format; the tool regenerates txt/html).
   Submission as a first-time author requires email confirmation; the draft becomes
   visible after the author confirms. Submit the SCITT draft first so that the WIMSE
   draft's normative reference resolves.

3. **After submission**, reply on each list thread with the Datatracker URL.
   Request agenda time from the chairs (`scitt-chairs@ietf.org`, `wimse-chairs@ietf.org`)
   before 2026-11-04.

4. **Before IETF 127**: push the generated vectors into an interoperable form (the three
   `.cose` files already exist) and offer them on the SCITT list for anyone implementing
   RFC 9943/9942 verifiers to try.

## Things to check before submission

- `venue.repo` / `venue.latest` in both `.md` headers point at this repository, `https://github.com/devinwarp/sijil-ietf`; the repo must be public before submission.
- The draft date is October 2026; `docname` carries `-00`. Datatracker will reject a -00 whose name already exists.
- Appendix A of the SCITT draft states the CWT `aee_type` claim uses its text-string key until IANA assigns TBD1; keep that sentence until the key is assigned.
- The Implementation Status section names Sijil once, as RFC 7942 permits; it is marked for removal before RFC publication.
- The SCITT draft is 40 paginated text pages. Page count is an editorial metric rather than an IETF submission limit; preserve the complete test-vector appendix and shorten only where semantics and clarity are unaffected.
