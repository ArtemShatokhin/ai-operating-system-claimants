# The deployment question

Whose account does the system run in? That single question separates most of the "open source AI operating system" field faster than a feature list, because it decides what happens when you stop paying, when the vendor renames the product, and when an auditor asks where the data sits.

A short, sourced tour of the four claimants in `claimants.yaml`:

- Cloudflare OS documents deploying into your own Cloudflare account; that account is where the system, its configuration and its integrations live.
- Red Hat's AI OS is a standard layer over infrastructure you already run, which is the strongest version of "it runs where your hardware does" among the four, and also the narrowest in scope: it is an inference layer.
- VAST's platform is a product you deploy where the vendor supports it.
- Xyne runs on infrastructure the organization controls, which is the closest of the four to the deployment shape a regulated company needs.

[Kortix](https://kortix.com) states the same answer in one line: it runs on Kortix Cloud, in your VPC, or on your own on-prem network, and self-host is free.

## What to write down before you choose

1. Where the configuration lives, and whether its history is yours (a git repository you own beats an export button).
2. Where a session's work happens, and what a sandbox can reach.
3. What an approval looks like, and who can grant it.
4. What you still have when the vendor relationship ends.

The vendors that answer all four in writing, on their own pages, are the ones to shortlist. The rest are demos.
