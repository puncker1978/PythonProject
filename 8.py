# Задание 1: Проверка пароля
# Напишите программу, которая запрашивает у пользователя пароль. Если пользователь вводит пароль «qwerty123»,
# программа должна вывести: Доступ разрешен. В противном случае программа должна вывести: Доступ запрещен.
# password = input('Введите пароль: ')
# if password == 'qwerty123':
#     print('Доступ разрешён')
# else:
#     print('Доступ запрещён')

# Задание 2: Задание 2: Определение времени суток
# Напишите программу, которая запрашивает у пользователя текущий час (от 0 до 23) и выводит сообщение:
# «Утро», если час от 6 до 11 включительно,
# «День», если час от 12 до 17 включительно,
# «Вечер», если час от 18 до 23 включительно,
# «Ночь», если час от 0 до 5 включительно.
# current_hour = int(input('Текущий час (число от 0 до 23): '))
# if 6 <= current_hour <= 11:
#     print('Утро')
# if 12 <= current_hour <= 17:
#     print('День')
# if 18 <=current_hour <= 23:
#     print('Вечер')
# if 0<= current_hour <= 5:
#     print('Ночь')

# Задача 3: Проверка температуры
# Напишите программу, которая запрашивает у пользователя текущую температуру в градусах Цельсия и выводит сообщение:
# «Жарко», если температура выше 30,
# «Тепло», если температура от 20 до 30 включительно,
# «Прохладно», если температура от 10 до 19 включительно,
# «Холодно», если температура ниже 10.
# temperature = int(input('Введите температуру: '))
# if temperature > 30:
#     print('Жарко')
# if 20 <= temperature <= 30:
#     print('Тепло')
# if 10 <= temperature <= 19:
#     print('Прохладно')
# if temperature < 10:
#     print('Холодно')

# Задача 4: Проверка диапазона чисел
# Напишите программу, которая запрашивает у пользователя число и проверяет, находится ли оно в диапазоне
# от 50 до 100 включительно. Если число находится в этом диапазоне, программа должна вывести: Число в диапазоне.
# В противном случае программа должна вывести: Число вне диапазона.
# num = int(input('Введите число: '))
# if 50 <= num <= 100:
#     print('Число в диапазоне')
# else:
#     print('Число вне диапазона')

# Задача 5: Проверка на положительное число
# Напишите программу, которая запрашивает у пользователя число и проверяет, является ли оно положительным.
# Если число положительное, программа должна вывести: Число положительное. В противном случае программа должна вывести:
# Число не положительное.
# num = int(input('Введите число: '))
# if num > 0:
#     print('Число положительное')
# else:
#     print('Число не положительное')

# Задача 6: Проверка цифр
# Напишите программу, которая запрашивает у пользователя трехзначное число и проверяет, является ли сумма первой
# и последней цифры этого числа равной той цифре, которая находится посередине и если является, то
# выводит на экран надпись: Число подходит
# a = int(input('Введите трёхзначное число: '))
# n3 = a % 10
# n2 = (a % 100) // 10
# n1 = a // 100
# if n2 == n1 + n3:
#     print('Подходит')
# else:
#     print('Не подходит')