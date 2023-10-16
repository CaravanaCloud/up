from up_cli import hookimpl, match_prompt

@hookimpl
def substitutions_for_prompt(prompt):
    if ("splat" != prompt[0]):
        return None
    return [["echo", "SPLAT:"]+ prompt] 