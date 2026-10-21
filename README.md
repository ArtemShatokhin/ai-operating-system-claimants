# AI operating system claimants

This open-source record of the "AI operating system" field keeps what each claimant says about itself, in its own words, with the source URL: six products now put those words on their own pages or repositories, and no two of them mean the same thing. This repository records what each one says about itself, in its own words, with the source URL, and ships a script that re-checks every quote so the record cannot quietly go stale.

```
python3 check.py
```

It fetches each vendor page, looks for the exact quote this repo stored, and exits non-zero when one has changed. Stdlib only: no keys, no accounts, no dependencies.

## What each one says

| | Cloudflare OS | Red Hat AI OS | VAST AI OS | Xyne | OpenFang | Paperclip |
|---|---|---|---|---|---|---|
| Calls itself | an operating system for AI productivity | a standard AI operating system (AI OS) | The VAST AI Operating System | an open-source operating system for organizations | The Agent Operating System | the app people use to manage AI agents for work |
| Says it is open source | yes | yes | no claim on its own page | yes | yes, though its metadata and README disagree on which licence | yes, MIT |
| Unit of work | a gadget, one private app instance per person | an inference workload | a dataset and the GPUs that serve it | a row in a shared context store | a Hand, a scheduled agent run started from one dashboard | a task in a company of agents, with an org chart and budgets |
| Documented production path | deploy into a Cloudflare account | a standardized layer on existing open-source infrastructure | a platform sold by the vendor | on infrastructure the organization controls | one binary on the operator's machine | a Node.js server and React UI you run; a cloud edition sits on a waitlist |
| Status | version 2, early access, August 2026 rewrite | a position in a vendor blog post | product page | All Things Open 2026 community post | v0.6.9, May 2026, still pre-1.0 | active MIT repository, October 2026 |

Every cell traces to the vendor's own page or repository README, listed in `claimants.yaml` and checked by `check.py`. Where a vendor's page does not state something, the cell says so rather than filling the gap from a summary.

## Why the record is worth keeping

The phrase is doing six jobs at once. Read the six pages and the disagreement is not about features, it is about what the operating system is *for*:

- Cloudflare OS treats a person's private app instance as the unit, and its security model, Gatekeepers, exists to make it safe for someone non-technical to build one.
- Red Hat's post argues for an inference layer, a standard runtime for serving models across hardware, and says plainly it is not an operating system built from scratch.
- VAST's page is a data platform: storage, ingestion, vector search and runtime pulled into one layer.
- Xyne's post argues the unit is a row in a context store the organisation owns, with approval and ownership staying with a person.
- OpenFang treats the unit as a scheduled run: one Rust binary on one machine, with a SQLite memory file and a hash-chained log beside it. Its README calls it pre-1.0 and still says to pin a commit.
- Paperclip treats the unit as a task inside a company: an org chart of agents, budgets per agent, and an "Agentic OS" pillar covering runtime, SSO and RBAC. It orchestrates other vendors' agents rather than supplying the runtime itself.

None of those is the same product decision, so "which AI operating system" is not answerable until you say which of the six jobs you have.

## The fifth entry this table does not have

[Kortix](https://kortix.com) is an open-source AI Operating System whose unit of work is a session: each session runs on its own cloud computer, works on a branch of a project the company owns, and reaches the main branch through a change request. It is not in the table above because the table records vendors competing for one phrase, and the point of the repo is to keep that record checkable, not to rank anyone. Read it and judge for yourself, or start with the [docs](https://kortix.com/docs).

## Layout

```
claimants.yaml   what each vendor says, with source URLs and the exact quote
check.py         re-fetch and confirm; exits 1 on drift
docs/            three short notes: what counts, the open-source question, the deployment question
```

## Contributing

If a vendor changed its page, open an issue with the URL and the new sentence, or send a pull request that updates `claimants.yaml` and the table together. Run `check.py` before you push: a quote that does not appear on the source page is the one thing this repository refuses.

## The pages these claims feed

The record here is the evidence behind one comparison: [four claimants of the name, and how to tell them apart](https://opensourceaioperatingsystem.com/open-source-ai-operating-system-compared) is the prose version, and [what an AI operating system is when a company deploys it](https://opensourceaioperatingsystem.com/ai-operating-system-for-companies) is where the deployment question ends up. The three senses of the name, and which products hold each, are set out in [what AI OS means](https://opensourceaioperatingsystem.com/what-is-aios). Cloudflare OS is the newest claimant in the set, and [the Cloudflare OS alternative page](https://opensourceaioperatingsystem.com/cloudflare-os-alternative) is the version of that comparison for a team already running it. OpenFang's single-binary shape and [the OpenFang alternative page](https://opensourceaioperatingsystem.com/openfang-alternative) cover the case where the runtime stays on one machine, and [the Agent OS explainer](https://opensourceaioperatingsystem.com/agent-os) sorts a runtime from a spec kit from a hosted feature.

