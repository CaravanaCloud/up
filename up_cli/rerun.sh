rm -rf "/workspace/.pyenv_mirror/poetry/virtualenvs/"up*
poetry cache clear . --all --no-interaction
poetry install
export UP_LOG_LEVEL="debug"
poetry run up vars: USER UALA
