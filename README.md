Unified Pluggable Tools
===

The goal of this project is to help software teams share and deliver solutions (a.k.a. scripts) reliably under a single, "white-label" command line tool.

**Check out our [demos](./demos) and [FAQ](FAQ.md)**

By "unified" we mean consolidating other CLI tools instead of creating a new one. 
It must be simple for teams to add new commands to the tool, without changing the existing code.
By "pluggable" we mean that we should "plug-in" into developers workflow and tooling, not force them into any structure.

For example, if you'd like to create a Kubernetes cluster using [OKD](https://okd.io), before your script actually deploys resources, you might be able to run it directly:
```bash
up template: install-config.compact-cluster.env.yaml
up wait: okd create cluster
kubectl apply -f myapp.yaml
```
or even less intrusively, as doclets:
``` bash
# template: install-config.compact-cluster.env.yaml
# wait: okd create cluster
kubectl apply -f myapp.yaml
```

Use `--help` to find more about each command and available subjects and actions.

Actions (Doclets)
===
Actions are the main work items in up. 
They are Python functions that can be invoked from the up command line, ansible or other tools.
The following actions are exposed by the up_lib module:

* vars: checks if environment variables are set or loadable
* wait: execute a shell command or python function with timeout
* install: install a known package using its preferred method
* template: process a template using envsubst or jinja2

Functions
===
Some actions (like wait:) can execute both shell commands (like $ echo hello) or python functions (like fibo(10)).
The following functions are exposed by the up_lib module:

* fibo: simple fibonacci calculation for testing

Both actions and functions can be added dynamically as a python module.

= Need help?
Yep, there is a lot TODO :)
Help is most welcome, get in touch if this sounds like something you could use. We'd be glad to help.


