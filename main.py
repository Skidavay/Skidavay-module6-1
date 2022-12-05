first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
number_sum = 0
for number in range(first_num, second_num +1):
  number_sum += number
print(number_sum)