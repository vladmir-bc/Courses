import requests
import re

site1 = 'https://' + input()
site2 = 'https://' + input()
marker = False
all_sites = []
pattern = re.findall(r'(https?://[\w.-/_]+?.html)', requests.get(site1).text)
for element in pattern:
    all_sites.extend(re.findall(r'(https?://[\w.-/_]+?.html)', requests.get(element).text))
    if site2 in all_sites:
        marker = True
if marker:
    print('Yes')
else:
    print('No')