from up_lib import hookimpl, match_prompt, RunConfig

def mk_run_config(prompt):
    result = RunConfig(
        image="fedora",
        command=['echo', 'Thanks for trying UP: '] + prompt)
    return result

@hookimpl
def run_for_prompt(prompt):
    return match_prompt(mk_run_config, prompt, "splat")

