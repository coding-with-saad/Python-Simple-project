import random
chars ="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/%"
lenght=int(input("enter lenght"))
password=""

for a in range(lenght):
    password+=random.choice(chars)
print(password)