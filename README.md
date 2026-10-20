# AI operating system claimants

This open-source record of the "AI operating system" field keeps what each claimant says about itself, in its own words, with the source URL: four products now put those words on their own pages, and no two of them mean the same thing. This repository records what each one says about itself, in its own words, with the source URL, and ships a script that re-checks every quote so the record cannot quietly go stale.

```
python3 check.py
```

It fetches each vendor page, looks for the exact quote this repo stored, and exits non-zero when one has changed. Stdlib only: no keys, no accounts, no dependencies.

## What each one says

| | Cloudflare OS | Red Hat AI OS | VAST AI OS | Xyne |
|---|---|---|---|---|
| Calls itself | an operating system for AI productivity | a standard AI operating system (AI OS) | The VAST AI Operating System | an open-source operating system for organizations |
| Says it is open source | yes | yes | no claim on its own page | yes |
| Unit of work | a gadget, one private app instance per person | an inference workload | a dataset and the GPUs that serve it | a row in a shared context store |
| Documented production path | deploy into a Cloudflare account | a standardized layer on existing open-source infrastructure | a platform sold by the vendor | on infrastructure the organization controls |
| Status | version 2, early access, August 2026 rewrite | a position in a vendor blog post | product page | All Things Open 2026 community post |

Every cell traces to the vendor's own page, listed in `claimants.yaml` and checked by `check.py`. Where a vendor's page does not state something, the cell says so rather than filling the gap from a summary.

## Why the record is worth keeping

The phrase is doing four jobs at once. Read the four pages and the disagreement is not about features, it is about what the operating system is *for*:

- Cloudflare OS treats a person's private app instance as the unit, and its security model, Gatekeepers, exists to make it safe for someone non-technical to build one.
- Red Hat's post argues for an inference layer, a standard runtime for serving models across hardware, and says plainly it is not an operating system built from scratch.
- VAST's page is a data platform: storage, ingestion, vector search and runtime pulled into one layer.
- Xyne's post argues the unit is a row in a context store the organisation owns, with approval and ownership staying with a person.

None of those is the same product decision, so "which AI operating system" is not answerable until you say which of the four jobs you have.

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

The record here is the evidence behind one comparison: [four open source claimants, and how to tell them apart](https://opensourceaioperatingsystem.com/open-source-ai-operating-system-compared) is the prose version, and [what an AI operating system is when a company deploys it](https://opensourceaioperatingsystem.com/ai-operating-system-for-companies) is where the deployment question ends up.

