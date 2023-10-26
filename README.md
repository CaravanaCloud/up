# Unified Pluggable Tools

The goal of this project is to enable organizations to build and publish their own unified toolkit, especially regarding CLI tools and solutions. More precisely:

* *Unified* means providing a single entry point for the organization tools, in constrast with having customers handle the installation and configuration of several CLI tools.

* *Pluggable* means letting any team in the organization contribute their features to the CLI, including new teams that may already have their own legacy code and binaries.

In that sense, as an hypotetical example, a comany called "Red Hat" that publishes binaries such as ```ansible```, ```quarkus```, ```oc```, ```ccmctl```, and so on, would be able to have those binaries executed as ```rh ansible```, ```rh quarkus```, ```rh oc```, and so on. The default executable from this project is named ```up```, organizations can use that or link/alias to any executable name, like as ```rh``` in this example.

Besides CLI management, such a tool would be a convenient opportunity to deliver complex solutions, such as creating an OKD cluster with specific features and operators installed, or pruning and cloud provider account. The specific operations are performed by the existing tools, such as ```openshift-installer``` or ```aws-nuke```, this projects aim to automate the configuration and verification steps so that solutions can be shared across different environments. 

A "cli facade" like that allows for the introduction of several benefits, such as:
* simplified installation for customers
* predictable runtime environments
* delivery of repeable solutions
* simplified experimentation

This project is at exeperimental stage and all contributions are most welcome.

# Design Decisions

## Not reinvent the wheel

Do not re-create a package manager, plugin system or packaging model. Let's use containers and existing libraries as much as possible.


## Leverage Python and Ansible

Provide a framework so that solutions can be automated with Ansible, and leveraging it's many features in that area. However, offer a stable and predictable environment, execute configuration and validation steps, allowing for testable and repeatable solutions.

For a better integration with the Ansible ecosystem, this project is mostly written in python, using pluggy as a plugin system.

