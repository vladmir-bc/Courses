import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # if len(re.findall(r'z...z', line)) > 0:
    #     print(line)
    if re.search(r'\\', line):
        print(line)