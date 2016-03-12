#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""
import sys
import argparse
from CardProcessor import CardProcessor

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
args = parser.parse_args()
content= file.read(args.infile)
entries = content.splitlines()

cardProcessor = CardProcessor(entries)
cardProcessor.display_statement()
