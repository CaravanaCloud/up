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


