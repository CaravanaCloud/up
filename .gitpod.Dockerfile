# docker build --no-cache --pull -f .gitpod.Dockerfile .
FROM gitpod/workspace-full

ARG JAVA_VERSION=22.3.r19-grl
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && sdk install java ${JAVA_VERSION} && sdk default java ${JAVA_VERSION} && sdk install quarkus"
RUN bash -c "gu install python"
RUN bash -c "gu install js"
RUN bash -c "sudo install-packages cowsay fortune"

