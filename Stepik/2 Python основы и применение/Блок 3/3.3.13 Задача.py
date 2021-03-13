import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"""\b[a]+\b"""
    print(re.sub(pattern, 'argh', line, 1, re.IGNORECASE))