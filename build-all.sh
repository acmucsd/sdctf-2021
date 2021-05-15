#! /usr/bin/env bash
# Builds all deployment files and attachments

cd "$(dirname -- "${BASH_SOURCE[0]}")" || { echo "Failed to change to working directory"; exit 1; }

# TODO: Rahil pushed binary files to the repo so we don't have to regenerate them

# make -C ./misc/alternative-arithmetic/challenge/ all &&
make -C ./misc/no-flag-for-u/ all &&
# make -C ./pwn/flagDropper/challenge/ flagDropper &&
make -C ./pwn/haxlab-s/ all &&
# make -C ./pwn/printFailed/challenge/ printFailed &&
# make -C ./pwn/unique-lasso/challenge/ uniqueLasso &&
make -C ./rev/0xC0F1D19D15EA5E/ 0xC0F1D &&
make -C ./rev/major-change-application/ all &&
make -C ./rev/una_acies/ all &&

echo "All files successfully built" >&2
