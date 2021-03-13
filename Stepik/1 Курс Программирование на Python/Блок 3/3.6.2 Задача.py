import requests
with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3378_2.txt', 'r') as inf:
    r = requests.get(inf.readline().strip())
    print(r.text)
    a = r.text.splitlines()
    print(len(a))