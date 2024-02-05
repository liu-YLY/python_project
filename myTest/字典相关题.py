x = True
country_counter = {}


def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1


addone('China')
addone('Japan')
addone('china')

print(len(country_counter))
print(country_counter)
# {'China': 1, 'Japan': 1, 'china': 1}


#  第二道题

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)  # 4
