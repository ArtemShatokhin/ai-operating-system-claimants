# The deployment question

Whose account does the system run in? That single question separates most of the "open source AI operating system" field faster than a feature list, because it decides what happens when you stop paying, when the vendor renames the product, and when an auditor asks where the data sits.

A short, sourced tour of the ten claimants in `claimants.yaml`:

- Cloudflare OS documents deploying into your own Cloudflare account; that account is where the system, its configuration and its integrations live.
- Red Hat's AI OS is a standard layer over infrastructure you already run, which is the strongest version of "it runs where your hardware does" among the ten, and also the narrowest in scope: it is an inference layer.
- VAST's platform is a product you deploy where the vendor supports it.
- Xyne runs on infrastructure the organization controls, which is the closest of the ten to the deployment shape a regulated company needs.
- OpenFang runs as one binary on the operator's machine, so the answer is the disk it sits on: nothing to deploy, and nothing shared until someone else needs the same memory.
- Paperclip runs as a Node.js server and React UI of your own, and orchestrates agents from other vendors inside it, so the deployment question splits: the dashboard is yours, the runtimes it drives may not be.

- taOS installs on hardware you own and says so plainly: cloud models are opt-in, and storage is append-only so a rollback returns the system to a known good state. The strongest answer in the set for a person, the weakest for a team that needs one shared system.
- Klawty's install script runs on your machine and Docker is ready, on a fork of OpenClaw; the site's own numbers describe a single operator's agent, not a company's deployment.
- SanctumOS is self-hosted by name: the modules are deployed onto infrastructure you run, following their docs. It states the deployment shape and leaves the licence question open.
- CorvinOS clones its repository and runs its installer locally, with the console on your own loopback address; the routing it adds is where the model calls go out, so the deployment question and the model question meet in the same place.

[Kortix](https://kortix.com) states the same answer in one line: it runs on Kortix Cloud, in your VPC, or on your own on-prem network, and self-host is free.

## What to write down before you choose

1. Where the configuration lives, and whether its history is yours (a git repository you own beats an export button).
2. Where a session's work happens, and what a sandbox can reach.
3. What an approval looks like, and who can grant it.
4. What you still have when the vendor relationship ends.

The vendors that answer all four in writing, on their own pages, are the ones to shortlist. The rest are demos.
