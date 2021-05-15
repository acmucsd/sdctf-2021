#! /usr/bin/env python3
import os, sys

RBASH_PATH = '/bin/rbash'
RUN_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/run'

print('There is no flag here.')
# Vulnerable to shell injection!
# Sample escape (without ``) without check_quotes: `';bash #`
# Sample escape (without ``) that passes check_quotes: `';bash -c 'bash`
os.chdir(RUN_DIRECTORY)

def check_quotes(ipt: str):
    quote_count_even = True
    for c in ipt:
        if c == "'":
            quote_count_even = not quote_count_even
    if not quote_count_even:
        # Give an error message telling participants that they are on the right track
        print("rbash: INTERNAL ERROR!")
        return False
    return True

try:
    while True:
        ipt = input('rbash$ ')
        if check_quotes(ipt):
            os.system("PATH='{}/bin' {} --noprofile --norc -c '{}' 2>&1".format(RUN_DIRECTORY, RBASH_PATH, ipt))
except EOFError:
    pass
