# С использованием генератора списков
people = [
    ["Alex", 29],
    ["Olga", 33],
    ["Vadim", 27],
    ['Nadya', 36],
    ['Petr', 40]
]

people_1_level = [item for sublist in people for item in sublist]
print (f"Исходный список списков: {people}")
print (f"Одноуровневый список: {people_1_level}")