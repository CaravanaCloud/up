from up_cli import pm
from up_splat import image_for_prompt
from up_splat import substitutions_for_prompt


pm.register(image_for_prompt)
pm.register(substitutions_for_prompt)