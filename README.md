# Unified Pluggable Tools


The goal of this project is to help software teams share and deliver solutions (a.k.a. scripts) reliably under a single, "white-label" command line tool.

**Check out our [demos](./demos) and [FAQ](FAQ.md)**

By "unified" we mean consolidating other CLI tools instead of creating a new one. 
It must be simple for teams to add new commands to the tool, without changing the existing code.
By "pluggable" we mean that we should "plug-in" into developers workflow and tooling, not force them into any technology.

For example, if you'd like to cleanup an aws account using [aws-nuke](https://github.com/rebuy-de/aws-nuke), it could be implemented as:
```
#!/bin/bash
up install: aws-nuke
up template: aws-nuke.envsubst.yaml
up wait: aws-nuke -c aws-nuke.yaml
```

Or even less intrusively, as doclets, in an existing script:
``` bash
#!/bin/bash
# install: aws-nuke
# template: aws-nuke.envsubst.yaml
aws-nuke -c aws-nuke.yaml
```

All features of this project are loaded using the python plugin architecture. 
They are built for re-packaging with another names and plugins, as suitable for your organization.
For example, suppose your organization is interested in creating and managing Kubernetes clusters using [OKD](https://okd.io).
You could simply link or rename the 'up' executable as 'okd'. This would allow the plugin system to load a different set of plugins.
However, the end result could be very similar:
``` bash
#!/bin/bash
okd template: install-config.compact-cluster.env.yaml
okd wait: okd create cluster
kubectl apply -f myapp.yaml
```

This design helps teams share solutions as plugins under a common CLI name, without limiting the actual actions it can perform or imposing any other CLI tool.


## Actions (Doclets)

Actions are the main work items in up. 
They are Python functions that can be invoked from the up command line, ansible or other tools.
The following actions are exposed by the up_lib module:

* vars: checks if environment variables are set or loadable
* wait: execute a shell command or python function with timeout and repeats
* install: install a known package using its preferred method
* template: process a template using envsubst or jinja2

## Functions

Some actions (like wait:) can execute both shell commands (like $ echo hello) or python functions (like fibo(10)).
The following functions are exposed by the up_lib module:

* fibo: simple fibonacci calculation for testing

Both actions and functions can be added dynamically as a python module.

## Wanna join?
Yep, there is a lot TODO :)
Help is most welcome, get in touch if this sounds like something you could use. 
We'd be glad to help.

Here's Julio on twitter if you'd like to chat https://twitter.com/faermanj :)


