people = [
    ["Alex", 29],
    ["Olga", 33],
    ["Vadim", 27],
    ['Nadya', 36],
    ['Petr', 40]
]

people_1_level = list()
for person in people:
    for elem in person:
        people_1_level.append(elem)

print (f"Исходный список списков: {people}")
print (f"Одноуровневый список: {people_1_level}")