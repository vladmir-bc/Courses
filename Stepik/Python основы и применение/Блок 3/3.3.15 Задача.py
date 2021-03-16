import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    match = re.search(pattern, line)
    print(re.sub(pattern, r'\1', line))
