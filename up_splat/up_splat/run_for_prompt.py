import uplib as up


def mk_run_config(prompt):
    result = up.RunConfig(
        image="fedora",
        command=['echo', 'Thanks for trying UP: '] + prompt)
    return result

@up.hookimpl
def run_for_prompt(prompt):
    return up.match_prompt(mk_run_config, prompt, "splat")

