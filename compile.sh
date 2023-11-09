#!/bin/bash

[[ -n $1 ]] || { echo "missing arg" >&2; exit 1; }

mkdir -p "proto/output/$1"
touch "proto/output/$1/__init__.py"
cp proto/input/*.proto "proto/output/$1/"

docker run                                    \
  --user "$(id -u):$(id -g)"                  \
  -v "$PWD/proto":/proto                      \
  --rm                                        \
  ghcr.io/query-ai/docker-protoc:main         \
  --proto_path=/proto/input                   \
  --fatal_warnings                            \
  --pyi_out="/proto/output/$1"                \
  --python_out="/proto/output/$1"             \
  @/proto/input/filelist.txt
