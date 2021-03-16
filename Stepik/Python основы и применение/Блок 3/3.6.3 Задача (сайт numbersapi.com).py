import requests

with open('dataset_24476_3.txt', 'r') as f:
    for line in f:
        number = line.strip()
        api_url = "http://numbersapi.com/" + str(number) + '/math?json=true'
        res = requests.get(api_url)
        if res.json()["found"] == True:
            print('Interesting')
        else:
            print('Boring')