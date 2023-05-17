Unified Pluggable Tools
===

The goal of this project is to help system administrators and developers to build and share solutions, without reinventing the wheel or having to learn a lot of stuff.

By "unified" we mean this is a tool that should be able to bridge team boundaries and let them compose solutions that can be shared widely, even outside the company.

By "pluggable" we mean that we should "plug-in" into developers workflow and tooling, not force them into any structure.

For example, if you'd like to create a Kubernetes cluster using [OKD](https://okd.io), before your script actually deploys resources, you might be able to run it directly:
```bash
up template install-config.compact-cluster.env.yaml
up wait okd create cluster
kubectl apply -f myapp.yaml
```
or even less intrusively, as doclets:
``` bash
# template: install-config.compact-cluster.env.yaml
# wait: okd create cluster
kubectl apply -f myapp.yaml
```

Or, in a general form that is easy to remember:
```
up $command $subject $action $object
```
The same would work as doclets:
```
# $command: $subject $action $object
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
