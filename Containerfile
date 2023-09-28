# docker build --no-cache --progress=plain -t caravanacloud/up -f Containerfile .
# docker run -it --rm caravanacloud/up echo uala

FROM registry.fedoraproject.org/fedora:38

RUN sudo dnf -y install python3 python3-pip
#RUN python3 --version

ARG YOUR_ENV
ARG POETRY_VERSION=1.6.1
ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=${POETRY_VERSION}
RUN pip3 install "poetry==$POETRY_VERSION"

RUN mkdir -p /opt/up
WORKDIR /opt/up

COPY . .

WORKDIR /opt/up/up_cli
RUN ls
RUN poetry config virtualenvs.create false
# --without dev
RUN poetry install 

ENTRYPOINT ["poetry", "--quiet", "run", "python3", "-m", "up_cli.main"]

