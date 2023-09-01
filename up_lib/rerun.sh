# rm -rf "/workspace/.pyenv_mirror/poetry/virtualenvs/"up*
poetry env use 3.11
poetry cache clear . --all --no-interaction
poetry -v install
export UP_LOG_LEVEL="debug"
poetry run pytest -sv --log-cli-level=DEBUG # --capture=tee-sys 
