# import re
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     for element in line.split():
#         if element[:int(len(element)/2)] == element[int(len(element)/2):]:
#             print(line)
#             break

# работает и та и та версии программы

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    for element in line.split():
        pattern = r'(\w+)\1'
        if re.match(pattern, element):
            print(line)