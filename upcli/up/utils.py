from up.commands import _commands

def get_commands_information() -> str:
    commands = []
    for key, value in _commands.items():
        command = key
        command_description = value[0].__doc__.replace('\n','')
        commands.append(f"    {command}\t {command_description}")
    return "\n".join(commands)

