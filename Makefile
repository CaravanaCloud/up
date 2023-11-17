RM	= rm -rf /home/faermanj/.cache/pypoetry/virtualenvs/up-ansible-EmbwlCf6-py3.12 \
			&& rm -rf /home/faermanj/.pyenv/versions/3.12.0/lib/python3.12/site-packages/up*

# publish_libs.sh
define publish =
#!/bin/sh
set -ex

pushd up_lib
poetry publish --build 
popd

pushd up_ansible
poetry publish --build
popd

pushd up_splat
poetry publish --build
popd
endef

# build_libs
define build =
#!/bin/sh
set -ex

poetry config virtualenvs.create false

pushd up_lib
poetry build 
popd

pushd up_ansible
poetry build
popd

pushd up_splat
poetry build
popd

pushd up_cli
poetry build
popd
endef

# bump_patch
define patch =
#!/bin/sh

increment_version() {
  local version=$1
  local major=$(echo $version | cut -d. -f1)
  local minor=$(echo $version | cut -d. -f2)
  local patch=$(echo $version | cut -d. -f3)
  patch=$((patch+1))
  echo "$major.$minor.$patch"
}

for file in */pyproject.toml; do
    cp "$file" "$file.bak.$(date +%s)"
    new_version=$(cat "$file" | grep "^version" | cut -d= -f2 | tr -d ' "')
    new_version=$(increment_version $new_version)
    echo "Bumping $file to $new_version "
    sed -i "s/^version = .*/version = \"$new_version\"/" "$file" 
    sed -i "s/^up-ansible = .*/up-ansible = \"$new_version\"/" "$file"
    sed -i "s/^up-splat = .*/up-splat = \"$new_version\"/" "$file"
    sed -i "s/^up-lib = .*/up-lib = \"$new_version\"/" "$file"
    
done
endef

# Containerfile
define Containerfile =
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

endef

# uprun
define up =
#!/bin/sh

echo "TODO: Run up container and stuff"
endef

publish_libs:
	@$(value publish)

build_libs:
	@$(value build)

bump_patch:
	@$(value patch)

containerfile:
	@$(value Containerfile)

uprun:
	@$(value up)

clean:
	$(RM)
  
.ONESHELL:
