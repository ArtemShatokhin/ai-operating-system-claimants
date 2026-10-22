# What counts as an "AI operating system"

The term is applied to at least ten different things, and the difference is not marketing noise, it is a real difference in what you install and who can act.

**An OS for a person's apps.** Cloudflare OS creates a private instance of each app for each person and puts a security layer, Gatekeepers, between that instance and the outside world. The thing being managed is an app.

**An OS for inference.** Red Hat's post describes a standardised layer that runs models across hardware, built on existing open-source infrastructure, and says it is not an operating system built from scratch. The thing being managed is a workload.

**An OS for data.** VAST's AI OS pulls storage, ingestion, analytics, vector search and runtime into one layer. The thing being managed is a dataset and the compute attached to it.

**An OS for an organisation.** Xyne's post describes a context store the organisation owns, where approval and ownership stay with a person. The thing being managed is institutional knowledge.

**An OS for a machine's schedule.** OpenFang ships one Rust binary that runs Hands — scheduled agents — with a SQLite memory file and a hash-chained log on the same disk. The thing being managed is a recurring run.

**An OS for a company of agents.** Paperclip puts an org chart, budgets and approval gates over other vendors' agents, and calls that infrastructure pillar its Agentic OS. The thing being managed is a task and who in the org owns it.

An AI Operating System in the sense a company deploys, owns and audits as one system has one more unit: a session. Agents, skills, memory and connectors live in one repository; each session runs on its own cloud computer; work lands through a change request. That is the shape [Kortix](https://kortix.com) builds, and it is the shape to compare against whichever of the ten above you were looking at.

## A test you can run in five minutes

Ask one question of each candidate: *what does one unit of work look like, and where does it live afterwards?* An app, an inference call, a table, a wiki row, a channel, a turn, a module and a session are all answers, and the answer tells you who owns the result, what an audit covers, and what a backup actually restores.

**An OS for a person's own machine.** taOS calls itself the self-hosted AI agent operating system and what it installs is a personal cloud: a memory graph, agents, channels and a set of bundled apps, on a board or a machine in your own home. The thing being managed is one person's context.

**An OS for a channel.** Klawty's unit is an always-on agent that takes work from a chat channel, with skill counts and a task counter on its page. The thing being managed is a conversation that keeps running.

**An OS for modules.** SanctumOS names its parts after brain regions and wires each to a tool server, self-hosted and assembled by the operator. The thing being managed is a pipeline of interchangeable pieces.

**An OS for a turn.** CorvinOS routes each turn to the cheapest model that fits and puts fail-closed gates in front of what an agent may do. The thing being managed is a single request and its cost.
