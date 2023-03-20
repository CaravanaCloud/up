#!/bin/bash
set -x

echo "Cleaning up..."
rm -rf dist

echo "Building package"
./mvnw clean package

echo "Building app-image"
jpackage --verbose \
  --name up \
  --input target \
  --main-jar up.jar \
  --main-class up.Main \
  --type app-image \
  --dest dist/up/app-image
