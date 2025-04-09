import time as t
dici = {
    'Brasil' : 'Brasilia',
    'EUA' : 'Washington',
    'Canadá':'Toronto',
    'Rússia' : 'Moscow',
    'Reino Unido':'Londres'

}

print(dici['Brasil'],dici['Canadá'],dici['EUA'],dici['Reino Unido'],dici['Rússia'])

t.sleep(1)

dici['Canadá'] = 'França'
print(dici['Brasil'],dici['Canadá'],dici['EUA'],dici['Reino Unido'],dici['Rússia'])

t.sleep(1)

dici['Alemanha'] = "Berlim"
print(dici['Brasil'],dici['Canadá'],dici['EUA'],dici['Reino Unido'],dici['Rússia'],dici['Alemanha'])

t.sleep(1)

dici.pop('Canadá')
print(dici)

t.sleep(1)
list1 = dici.keys()
list2 = dici.values()
print(list1, list2)
