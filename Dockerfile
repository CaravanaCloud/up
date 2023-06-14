# docker build --no-cache --progress=plain -t up .
# docker run --rm -it -p 80:80 up 
ARG UBI=registry.fedoraproject.org/fedora:38
FROM $UBI as builder
RUN bash -c "dnf install -y python3-pip git"
COPY . /usr/src/up-tools
RUN bash -c "cd /usr/src/up-tools/up_cli && poetry install"

FROM registry.fedoraproject.org/fedora:38
CMD ["echo", "#TDO run up-tools"]
