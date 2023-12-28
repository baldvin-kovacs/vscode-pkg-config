#!/usr/bin/env python
import sys
import subprocess

out = subprocess.run(
    ['pkg-config.exe', '--cflags-only-I', sys.argv[1]],
    capture_output=True)

if out.returncode != 0:
    exit(1)

for item in out.stdout.split():
    cpparg = item.decode();
    if not cpparg.startswith('-I'):
        print('Not a -I element: {}'.format(item), file=sys.stderr)
        exit(1)
    print('                "{}",'.format(cpparg[2:]))
