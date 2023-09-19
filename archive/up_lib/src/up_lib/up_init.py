from .actions import *
from .commands import *
from .log import *
from .cmd.fibo import up_fibo
from .action.wait import wait
from .action.install import install, register_install
from .action.template import template
from .action.vars import vars
from .lookups import *
from .lookup.ssh_key import lookup_ssh_key

def up_init():
    debug("initializing up_lib actions")
    register_action("wait", wait)
    register_action("template", template)
    register_action("vars", vars)
    register_action("install", install)

    register_install(
        "openshift-install", 
        "web",
        "v4",
        "https://mirror.openshift.com/pub/openshift-v4", 
        {
            "linux-x86_64": "/x86_64/clients/ocp/stable/openshift-install-linux.tar.gz"
        },
        "opensift-install -v"
    )

    register_install(
        "openshift-client", 
        "web",
        "v4",
        "https://mirror.openshift.com/pub/openshift-v4", 
        {
            "linux-x86_64": "/x86_64/clients/ocp/stable/openshift-client-linux.tar.gz"
        },
        "oc -v"
    )

    debug("initializing up_lib commands")
    register_command(("fibo",), up_fibo)
    debug("initializing up_lib lookups")
    register_lookup("SSH_KEY", lookup_ssh_key)
