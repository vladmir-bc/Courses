import simplecrypt

passwords = []
with open("passwords.txt", "r") as password:
    for line in password:
        passwords.append(line.strip())
print(passwords)

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for i in passwords:
        try:
            a = simplecrypt.decrypt(i, encrypted)
        except:
            print('Следующая попытка')
print(a)
