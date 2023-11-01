#!/bin/sh
set -ex

poetry config virtualenvs.create false

pushd uplib
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
