#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    Примеры:
#    - 1, 4, 8, 7, 5 -> 8
#   - 78, 55, 36, 90, 2 -> 90

num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
num3 = int(input("Введите 3 число: "))
num4 = int(input("Введите 4 число: "))
num5 = int(input("Введите 5 число: "))
print(f"Максимум равен {max(num1, num2, num3, num4, num5)}")

#Другое решение

my_max = 0
for _ in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num

print(my_max)
