#!/bin/bash
# assert: aws sts get-caller-identity
# install: aws-nuke
# template: aws-nuke.qute.yaml
# log: aws-nuke.log
aws-nuke -c ./aws-nuke.yaml \
  --no-dry-run \
  --force \
  --force-sleep 3
