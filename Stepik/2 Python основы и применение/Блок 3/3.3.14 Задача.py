import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"""\b(\w)(\w)"""
    print(re.sub(pattern, r'\2\1', line))
