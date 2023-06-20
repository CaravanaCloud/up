#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
set -ex

pushd $DIR
poetry env use 3.11
poetry cache clear . --all

echo "Checking environment"
echo "pyenv version \n $(pyenv version)"
echo "poetry env info \n $(poetry env info)"
# sleep 333

pushd "up_lib"
echo "Installing up_lib"
poetry build
pip install "$DIR/up_lib/dist/"*.whl
popd

pushd "up_cli"
echo "Installing up_cli"
poetry install
popd

popd

echo done