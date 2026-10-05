# Agent Execution Evidence — Internet-Drafts

This repository holds two individual Internet-Drafts on verifiable evidence for
AI agent runs. They are working documents, not standards; feedback is welcome on
the relevant working-group lists or via GitHub issues.

| Draft | Intended WG | Formats |
| --- | --- | --- |
| `draft-thaha-scitt-agent-execution-evidence` | SCITT | [.txt](draft-thaha-scitt-agent-execution-evidence-00.txt) · [.html](draft-thaha-scitt-agent-execution-evidence-00.html) · [.xml](draft-thaha-scitt-agent-execution-evidence-00.xml) |
| `draft-thaha-wimse-agent-evidence-binding` | WIMSE | [.txt](draft-thaha-wimse-agent-evidence-binding-00.txt) · [.html](draft-thaha-wimse-agent-evidence-binding-00.html) · [.xml](draft-thaha-wimse-agent-evidence-binding-00.xml) |

## What the drafts do

**Agent Execution Evidence** (SCITT draft, Standards Track) defines a set of
Signed Statement types — Agent Credential, Policy Pack, Configuration
Integrity, Execution Receipt, Execution Epoch, Assurance Statement and
Revocation — that record what an autonomous or semi-autonomous agent actually
did, registered on a SCITT Transparency Service (RFC 9943/9942) so the trail is
tamper-evident. It also specifies an identity-continuity model: a persistent
`logical_agent_id` mapped to the runtime identities an agent presents in
different trust domains, following the identifier semantics of
draft-ietf-wimse-arch.

**Evidence Binding** (WIMSE draft, Informational) is deliberately narrow: it
defines one workload-credential claim, `aee_evidence`, that binds the
authenticated runtime identity to a `logical_agent_id`, the expected Evidence
Service and the policy in force — plus one in-toto predicate type that carries
the corresponding Execution Receipt. It defines no retrieval protocol,
registry, status service or audit schema.

## Discussion

- SCITT: scitt@ietf.org — https://mailarchive.ietf.org/arch/browse/scitt/
- WIMSE: wimse@ietf.org — https://mailarchive.ietf.org/arch/browse/wimse/

## Building

```
pip install xml2rfc cbor2 pynacl
gem install kramdown-rfc            # or build from https://github.com/cabo/kramdown-rfc
kramdown-rfc2629 --v3 draft-thaha-scitt-agent-execution-evidence-00.md > draft-thaha-scitt-agent-execution-evidence-00.xml
xml2rfc --text --pagination --html draft-thaha-scitt-agent-execution-evidence-00.xml
```

All references are defined inline in the YAML front matter, so no network access
is needed at build time except the two BCP 14 references added by
`{::boilerplate bcp14-tagged}`; `.refcache/` carries those bibxml files so the
build also works offline. `idnits` is a useful sanity check on each `.txt`.

## Test vectors

`vectors/make_vectors.py` regenerates the Appendix A test vectors of the SCITT
draft (Ed25519, deterministic seeds; `vectors/vectors.txt` and the three `.cose`
files are its output).

## Status

Both drafts are -00 individual submissions intended for discussion in the SCITT
and WIMSE working groups. See the list posts in `LIST_POSTS.md`.
