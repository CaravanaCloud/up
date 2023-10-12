from up_cli import hookimpl, match_prompt

@hookimpl
def image_for_prompt(prompt):
    return match_prompt(prompt, "ansible", "cytopia/ansible")
