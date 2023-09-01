# rm -rf "/workspace/.pyenv_mirror/poetry/virtualenvs/"up*
poetry env use 3.11
poetry cache clear . --all --no-interaction
poetry -v install
export UP_LOG_LEVEL="debug"

# poetry run up echo hello world
# poetry run up template: ../demos/10_template/install-config.sample.env.yaml

poetry run up install aws-nuke
