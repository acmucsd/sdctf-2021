#! /usr/bin/env bash

expected_exit_code=1

"$@"
exit_code=$?
if (( exit_code == expected_exit_code )); then
    exit 0
else
    echo "Expected exit code: $expected_exit_code, actual exit code: $exit_code"
    exit 1
fi
