import requests
import re

site1 = input()
all_sites = set()
site = requests.get(site1.strip())
pattern = r"""<a.+?href=\W(?:http:\/\/|https:\/\/|ftp:\/\/)?((\w+\.?-?)+)"""
match = re.findall(pattern, site.text)
for element in match:
    all_sites.add(element[0])
all_sites = list(all_sites)
all_sites.sort()
for el in all_sites:
    print(el)