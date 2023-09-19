# UP is a CLI tool to run and manage other CLI tools so that they are:
# - Unified: All tools from an organization with a consistent, learnable interface.
# - Pluggable: All teams from an organization can add to the toolset.
#
# Let's start with the simplest example: running a command.
up WAIT echo hello world

# WAIT is the default action
up echo hello world

# Output is JSON by default
up echo hello world | jq

# Logs go to STDERR
up echo hello world 2> up.log && cat up.log
