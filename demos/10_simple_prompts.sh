# Setup "up" alias in dev mode if necessary
alias up="poetry run up"

# Runs `ansible --version` through up
# The ansible binary will be executed inside a container
up ansible --version

# You can check that `ansible` is not installed in the system
type ansible

# If there is no plugin, like there is for ansible
# up will try default container settings (Fedora Linux)
up cat /etc/fedora-release

# TODO: this one is broken
up "ansible --version | head -n1" | awk '{print $2}'
