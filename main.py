# С использованием функции itertools.chain
import itertools

people = [
    ["Alex", 29],
    ["Olga", 33],
    ["Vadim", 27],
    ['Nadya', 36],
    ['Petr', 40]
]

people_1_level = list(itertools.chain(*people))
print (f"Исходный список списков: {people}")
print (f"Одноуровневый список: {people_1_level}")