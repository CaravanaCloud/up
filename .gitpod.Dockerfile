FROM gitpod/workspace-full

ARG JAVA_VERSION=22.3.r19-grl
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && sdk install java ${JAVA_VERSION} && sdk default java ${JAVA_VERSION} && sdk install quarkus"
RUN bash -c "sudo install-packages cowsay fortune"
