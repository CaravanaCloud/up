Unified Pluggable Tools
===

The goal of this project is to help software teams share and deliver solutions (a.k.a. scripts) reliably, while reducing CLI proliferation.

Check out our [demos](./demos) and [FAQ](FAQ.md)

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

Commands / Doclets
===

* TODO copy: copy generated files
* TODO expect(variable_name): Ensure variables are present or generated
* TODO ?export: set system variables?
* TODO install: given package
* TODO template: Process a template
* TODO wait(command, timeout, continue_on_fail): Run command and return the same

Yep, there is a lot TODO :)
Help is most welcome, get in touch if this sounds like something you could use. We'd be glad to help.
