from up_cli import hookimpl, match_prompt, RunConfig

def mk_run_config(prompt):
    result = RunConfig(
        image="cytopia/ansible:latest",
        command=prompt)
    return result

@hookimpl
def run_for_prompt(prompt):
    return match_prompt(mk_run_config, prompt, "ansible")
