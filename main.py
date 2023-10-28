input_string = input("Введите строку: ")
words = input_string.split()
count = 0
for word in words:
    match word:
        case "кот" | "КОТ" | "Кот":
            count += 1
        case _:
            continue
print(count)
