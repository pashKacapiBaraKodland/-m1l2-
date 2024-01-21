import random
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longs = int(input('введите длинну пароля '))
parol = ""
for i in range(longs):
    parol += random.choice(char)
print(parol)