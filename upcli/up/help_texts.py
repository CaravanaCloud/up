up_help_text = """\rUnified and Pluggable CLI - Version %s
    \n\rUsage:
    up <prompt>
        or
    up plugin <command>
    \n\rPrompt options:
    -Xv\t Set a volume to be used
    -Xp\t Set a port to be used
    \n\rAvailable commands:
    \r%s

    \rExamples:
    up ansible --version\t Shows ansible version
    up -Xp={8080/tcp: 5000} ansible -h\t Will set the port to ansible
    up plugin prompts ansible\t List all ansible prompts from up.yaml
    """
list_help_text = """\rDescription: %s
    \n\rUsage:
    up plugin list
    """
details_help_text = """\rDescription: %s
    \n\rUsage:
    up plugin details <prompt>

    \rExample:
    up plugin details ansible --version\t Shows prompt configuration from up.yaml
    """
prompts_help_text = """Description: %s
    \n\rUsage:
    up plugin prompts <plugin>

    \rExample:
    up plugin details ansible\t List all ansible prompts from up.yaml
    """

