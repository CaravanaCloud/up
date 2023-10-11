from up_cli import pm

from up_splat import image_for_prompt

print("-- Registering plugin 2 --")
pm.register(image_for_prompt)