# docker build --progress=plain --no-cache --pull -f .gitpod.Dockerfile .
FROM gitpod/workspace-python

RUN pyenv install 3.11 \
    && pyenv global 3.11

RUN bash -c "sudo install-packages cowsay fortune"
