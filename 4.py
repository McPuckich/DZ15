sth = 'Ежевику для ежат \nПринесли два ежа. \nЕжевику еле-еле \nЕжата возле ели съели'
print(sth)

sth = sth.replace("\n", "")
print(sth)
sth = sth.split(" ")
print(sth)

povt = 0
for i in sth:
    if i[0] == 'е' or i[0] == 'Е':
        povt += 1
print("Количество слов: ", povt)
