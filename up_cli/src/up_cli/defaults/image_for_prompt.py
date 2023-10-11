from up_cli import hookimpl

@hookimpl
def image_for_prompt(prompt):
    print("inside Plugin_1.myhook()")
    return "-".join(prompt)
