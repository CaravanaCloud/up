# docker build --no-cache --progress=plain -t up .
# docker run --rm -it up 
ARG UBI=python:3.11
FROM $UBI as builder
# RUN bash -c "dnf install -y python3-pip git"
RUN bash -c "pip install poetry && poetry config virtualenvs.in-project true"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
COPY . /usr/src/up-tools
WORKDIR /usr/src/up-tools/up_cli
RUN bash -c "poetry install --only main --no-interaction --no-ansi -vvv"

FROM $UBI
COPY --from=builder /usr/src/up-tools/up_cli/dist /opt/up-tools
# RUN bash -c "dnf install -y python3-pip"
RUN bash -c "pip install /opt/up-tools/*.whl"
# RUN bash -c "which up"
RUN bash -c "find /opt/up-tools"
RUN bash -c "echo done"
