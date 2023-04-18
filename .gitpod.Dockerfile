# docker build --progress=plain --no-cache --pull -f .gitpod.Dockerfile .
FROM gitpod/workspace-full

ARG JAVA_VERSION=22.3.r19-grl
RUN bash -c "echo whoami: $(whoami)"
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh \
    && sdk install java ${JAVA_VERSION} \
    && sdk default java ${JAVA_VERSION} \
    && sdk install quarkus \
    && sdk install jbang \
    && gu install python \
    && gu install js"
RUN bash -c "sudo install-packages cowsay fortune"

