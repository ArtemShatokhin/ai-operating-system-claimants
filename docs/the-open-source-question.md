# The open-source question

Five of the six claimants say they are open source and one does not, which makes "open source AI operating system" a search that can return six products with five different answers about what open source buys you.

Read the sentence each one writes, not the label:

- Cloudflare OS: "We are making Cloudflare OS open source so that others can copy it and customize it for their own company. The idea is not that your company uses Cloudflare OS, but rather that you make it '*Your Company* OS'." What you get is a codebase to fork, deployed through the vendor's platform.
- Red Hat's post says the layer is built on open source technology; it is a position about infrastructure standards rather than a repository you clone and run as your system.
- Xyne's post says it is an open-source operating system for organizations, running on infrastructure the organisation controls.
- VAST's page makes no open-source claim for the platform itself.
- OpenFang's README says it is open source and its `Cargo.toml` sets `Apache-2.0 OR MIT`, with both licence files at the repo root, while its README badge and License section name MIT alone and GitHub's metadata reports Apache-2.0. Both are permissive; the disagreement is the thing to check before you ship a build.
- Paperclip is MIT, and its claim rests on the orchestration layer: the agents it runs can be any vendor's, so an open dashboard over closed agents is a different bargain from an open runtime.

For [Kortix](https://kortix.com) the sentence is short: open source, read it, fork it, audit it, and it runs on Kortix Cloud, in your VPC, or on your own on-prem network.

## The question behind the question

Open source changes three things a buyer can actually check: whether the code that holds company memory can be read, whether the deployment target is yours to choose, and whether the change history of the configuration survives a vendor. Ask each claimant for those three answers in writing. A repository you can read but a deployment you cannot choose is a weaker claim than the word "open" suggests, and the reverse is also worth avoiding.
