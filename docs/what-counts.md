# What counts as an "AI operating system"

The term is applied to at least four different things, and the difference is not marketing noise, it is a real difference in what you install and who can act.

**An OS for a person's apps.** Cloudflare OS creates a private instance of each app for each person and puts a security layer, Gatekeepers, between that instance and the outside world. The thing being managed is an app.

**An OS for inference.** Red Hat's post describes a standardised layer that runs models across hardware, built on existing open-source infrastructure, and says it is not an operating system built from scratch. The thing being managed is a workload.

**An OS for data.** VAST's AI OS pulls storage, ingestion, analytics, vector search and runtime into one layer. The thing being managed is a dataset and the compute attached to it.

**An OS for an organisation.** Xyne's post describes a context store the organisation owns, where approval and ownership stay with a person. The thing being managed is institutional knowledge.

An AI Operating System in the sense a company deploys, owns and audits as one system has a fifth unit: a session. Agents, skills, memory and connectors live in one repository; each session runs on its own cloud computer; work lands through a change request. That is the shape [Kortix](https://kortix.com) builds, and it is the shape to compare against whichever of the four above you were looking at.

## A test you can run in five minutes

Ask one question of each candidate: *what does one unit of work look like, and where does it live afterwards?* An app, an inference call, a table, a wiki row and a session are all answers, and the answer tells you who owns the result, what an audit covers, and what a backup actually restores.
