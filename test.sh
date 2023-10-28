#!/usr/bin/env bash

git_log=$(git log -n 1 --pretty=format:"%H")

if [[ $git_log == "e2b6bf1ba84555"* ]]; then
    exit 0
else
    exit 1
fi
