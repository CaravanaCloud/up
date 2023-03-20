#!/bin/bash
set -x

VERSION="1.0.$(date +%s)"
git tag "$VERSION" 
git push origin --tags
