import requests
with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3378_3.txt', 'r') as inf:
    r = requests.get(inf.readline().strip())
    while "We" not in r.text:
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
        print(r.text)