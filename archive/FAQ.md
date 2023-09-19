Frequently Asked Questions
===

## Why is this project needed?

The goal of this project is to make the sharing of CLI solutions as simple as possible,
so that customers and partners can easily try and apply solutions built by subject matter
especialists.

This project addresses the common issues in sharing such solutions:
- Installation of dependencies
- Lookup and validation of input variables
- Processing of configuration templates
- Execution of commands and functions
- Wait for resources
- Output filtering

## Why not Ansible / Rundeck / ...?

We don't want to be tightly coupled to any tooling, not to force it upon users.
All features of up-tools are implemented as a python library that can be
easily integrated with most other tools.

## Why not kubectl plugins?

Because they are much more difficult to integrate, regarding:
- Sharing data
- Controlling flow
- Controlling parallelism

So we decided to use [Python Plugin Architecture](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/) instead, loading plugins according to the execution context, including the executable name. This makes it simple to package and release a custom solutions library.

Also, we want to make it simple to integrate with other tools, like Ansible, leveraging their own error and parallelism controls when possible.

## What could I build with up-tools?
This project is a tool that should be easily adaptable to your automation.
Out of the box, it comes with basic actions like "wait", "template" and "install", but you can easily add your own actions and commands.
Here are example solutions:
- Create a Kubernetes cluster, verify health and deploy an app.
- Clean up a cloud account, by listing resources in all accounts and regions and deleting them.
- From a directory of video files, extract audio, transcribe and translate them.
- ...

The actual implementation for all of that is already available in other CLIs, libraries and cloud services.
This tool lets developers build such solutions in their choice of tooling, adding the fetures of up actions on top of them.

## What are those up_ modules?

* up_lib: The core features of this project, like the plugin system and basic actions. Most of work happens here. 
* up_cli: Command line frontend for up_lib, so it can be used in scripts. Also used by the container.
* up_ansible: The ansible frontend for up_lib, to be developed.

## How to learn more?

[Demos](./demos) and [tests](./up_lib/tests/) are a great way to start!

Also feel free to connect with me :) [faermanj](https://twitter.com/faermanj)

## What's the current status of this project?

Extremelly experimental. Join the fun!






