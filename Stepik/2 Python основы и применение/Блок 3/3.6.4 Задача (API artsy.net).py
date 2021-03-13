import requests
import json

client_id = '67e893830b637fa221ba'
client_secret = '76a36e278eda5af44e4c3451d6e40666'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]
painters = []

headers = {"X-Xapp-Token": token}
with open('dataset_24476_4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        r = requests.get("https://api.artsy.net/api/artists/" + line, headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)
        painters.append(j['birthday'] + ' ' + j['sortable_name'])

painters.sort()
for el in painters:
    print(el[5:])
