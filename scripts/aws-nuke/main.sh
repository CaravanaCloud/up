#!/bin/bash

# Check AWS authentication: aws sts get-caller-identity (set AWS_ACCOUNT_ID)
#^ assert: aws sts get-caller-identity (bash)
#^ assert: aws-authenticated (outro script)
#
# baixar e instalar 
#  mkdir /tmp/aws-nuke
#  curl -Ls $URL --output $OUTPUT
#  tar zxvf $OUTPUT -C /tmp/aws-nuke 
#  sudo mv /tmp/aws-nuke/aws-nuke-v2.19.0-linux-amd64 /usr/local/bin/aws-nuke
#
#^ install: aws-nuke
# 
# Gerar o arquivo de config (./aws-nuke/ccsandbox.yml) e passar como paramtro 
#^ qute: aws-nuke.qute.yaml 
#^ j2: aws-nuke.j2.yaml 
# ...
# $ up aws-nuke

aws-nuke -c ./aws-nuke.yaml --no-dry-run --force --force-sleep 3 | tee aws-nuke.log
