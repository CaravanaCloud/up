# docker build --no-cache --progress=plain -t up .
# docker run --rm -it up wait: echo hello
# docker build --no-cache --progress=plain -t up . && docker run --rm -it up
ARG UBI=python:3.11
FROM $UBI as builder

RUN bash -c "pip install poetry && poetry config virtualenvs.in-project true"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_NO_INTERACTION=1

COPY . /usr/src/up-tools
WORKDIR /usr/src/up-tools/up_cli

RUN bash -c "poetry install --only main --no-ansi -vvv"

# TODO: second stage docker image
# FROM $UBI
# RUN bash -c "pip install poetry && poetry config virtualenvs.in-project true"
# COPY --from=builder "/usr/src/up-tools" "/opt/up-tools"
# WORKDIR "/opt/up-tools/up_cli"
# RUN bash -c "find /opt/up-tools"
# RUN bash -c "ls -liah /opt/up-tools/up_cli/.venv/bin/up"
# RUN bash -c "/opt/up-tools/up_cli/.venv/bin/up"
# TODO: Entrypoint to built script
ENTRYPOINT [ "poetry", "run", "up" ]
