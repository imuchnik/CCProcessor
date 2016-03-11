#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""

import sys
from CardProcessor import CardProcessor

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as file:
        content = file.read()
        entries = content.splitlines()
else:
    entries = sys.stdin.readlines()

cardProcessor = CardProcessor(entries)
cardProcessor.display_statement()
