print('Задача 3. Функция')

# Учитель математики придумывает каждому своему ученику отдельные функции,
# которые нужно отобразить на графике и посчитать.
# А ещё этот учитель разбирается в программировании.
# Поэтому, чтобы не считать вручную все эти функции,
# он написал программу, которая делает всю работу за него.

# Напишите программу,
# которая получает от пользователя число X и вычисляет значение функции Y

# Напомним, как это работает:
# Если X больше нуля Y = X - 12.
# Если X равных нулю Y равен пяти.
# Если X меньше нуля Y равен квадрату X.

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: -6
# Игрек равен 36

x = int(input('Введите число X: '))
if x > 0:
  print('Y равно:', x - 12)
elif x < 0:
  print('Y равно:', x**2)
else:
  print('Y равно:', 5)