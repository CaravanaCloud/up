#!/bin/bash
set -ex

rm -f */poetry.lock
rm -rf /workspace/.pyenv_mirror/poetry/virtualenvs/*

pushd uplib
poetry config virtualenvs.create false
poetry install -vvv 
popd

pushd up_ansible
poetry config virtualenvs.create false
poetry install  -vvv 
popd

pushd up_splat
poetry install
popd

pushd upcli
poetry install
popd

echo "done installing all"
