#!/bin/bash
set -ex

echo "Cleaning up..."
rm -rf dist

echo "Building package"
#TODO: Remove -fn when tests are clear
./mvnw \
  --no-transfer-progress \
  --batch-mode \
  --fail-never \
  clean package

echo "Building app-image"
jpackage --verbose \
  --name up \
  --input target \
  --main-jar up.jar \
  --main-class up.Main \
  --type app-image \
  --dest dist/up/app-image
