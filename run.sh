#!/bin/bash
set -ex

mvn -DskipTests package quarkus:dev
