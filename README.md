# Unified Pluggable (UP) Tools

The goal of this project is to enable organizations to deliver solutions that are reliable and easy to build, based on containers.
Many software organizations rely on a complex set of command-line tools (CLIs) and configuration files to deliver container-based solutions.
This project proposes to make that simpler by building tools focused on two key characteristics:

* *Unified*: Help organizations build and publish tools that spans through many service teams through a centralized entrypoint. Just like `aws ec2`, `aws s3`, or any other cloud provider CLIs. This allows their customers to execute new workflows reliably by simply updating the tool, instead of installing and configuring new ones. 

* *Pluggable*: Help developers integrate solutions into any system with minimal friction. Existing CLIs and container images can be leveraged without modification, and still be integrated with UP for additional features.

In this repository you'll find the `up` CLI, demonstrating the proposed plugin system and integration with popular tools such as ```ansible```, ```quarkus```, ```oc```, and others. See the `demos` directory for examples!

This project is at exeperimental stage and all contributions are most welcome.

# What is novel about UP?
UP tools are designed on top of modern container tools to leverage the packaging and distribution standards that are widely adopted. However, this project takes innovative approaches in the development and delivery of container-based solutions.

By building a *plugin-system* that allows organizations to easily integrate their existing containers and command-line solutions into a centralized tool. UP plugins can be simple library packages or even a single configuration file.

By using *doclets* to integrate scripts with containers, so that they can be executed "as is" or through up tools, adding the settings and hooks defined as comments in the script itself.


# How do I use up?

## Command Mode
Any command prompt can be executed with the `up` CLI. Once `up` is invoked, with your prompt as argument, it will look up any plugin that provides container configurations for your execution. For example, one could run `up ansible --version` even without ansible installed. The ansible plugin will load the correct container and execute your command, printing the ansible version.

```bash
$ up ansible --version 
```

## Script Mode

In script mode, just like command mode, your script will be executed in a container. However, besides the plugins, it will look for comments in your script that are containerfile instructions such as "FROM", "PORT", "ENV". Those will be parsed and executed as well. For example, the following script could be created to run your ansible commands through a container.

```bash
#!/bin/bash

# FROM cytopia/ansible:latest

ansible --version
```

# How's that supposed to help?

As a developer, you can use script mode to automate a solution and be assured that it be executed as supposed, with correct dependencies, binaries and settings from the container.

As a organization manager or lead, you can build and distribute your own version of `up`, consolidating the deliveries of service teams and allowing customers to experiment new solutions.

# Frequently Asked Questions?

## What if I want to pass a port or volume? 
So you have 2 options: first: set the volume/port inside the `up.yaml` of your plugin, or in the example case the Ansible plugin; or second: pass the volume/port on the command, e.g:
```bash
$ up -Xp=8080/tcp:5000 ansible --version # will set the port in the container
$ up -Xv=/home:/mnt/vol3,rw ansible --version # will set the volume in the container
```

# Does up have some internal/probing commands?
Yes, the current available commands are in `plugin` reserved keyword:
```bash
$ up plugin list # List all installed plugins
$ up plugin prompts ansible # Shows the prompts from up.yaml of a plugin
$ up plugin details ansible --version # Shows the prompt configuration from up.yaml of a plugin
```
