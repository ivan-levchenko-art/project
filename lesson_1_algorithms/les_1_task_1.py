'''Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь'''

x = input("введите трехзначное число: ")
z = int(x[0]) + int(x[1]) + int(x[2])
y = int(x[0]) * int(x[1]) * int(x[2])
print(f'Сумма цифр {z}')
print(f'Произведение цифр {y}')
