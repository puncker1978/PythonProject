# Задание 1: Напишите программу, которая считывает два целых числа и выводит их сумму, разность, произведение и
# частное.
a, b = int(input('Первое число: ')), int(input('Второе число: '))
print('Сумма a + b:', a + b)
print('Разность a - b:', a - b)
print('Произведение: a * b:', a * b)
print('Частное: a / b', a / b)

# Задание 2: Вычислить площадь треугольника по формуле S = 1/2 * a * h
a, h = int(input('Основание треугольника: ')), int(input('Высота треугольника: '))
print('Площадь треугольника', a * h / 2)

# Задание 3: Напишите программу, которая считывает три целых числа и вычисляет их среднее арифметическое.
# Среднее арифметическое трех чисел это сумма этих чисел, поделенная на три.
a, b, c = int(input('Первое число: ')), int(input('Второе число: ')), int(input('Первое число: '))
print('Среднее арифметическое: ', (a + b + c)/3)