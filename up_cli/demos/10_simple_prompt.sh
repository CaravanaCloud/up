# in dev mode...
alias up="poetry run up"

up ansible --version

up ansible --version | head -n1 | awk '{print $2}'
