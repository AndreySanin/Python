#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#    *Примеры:* 
#    - 4, 16 -> да
#    - 25, 5 -> да
#    - 8,9 -> нет

num1, num2 = int(input("Enter 1st number: ")), int(input("Enter 2st number: "))
if (num1==num2**2) or (num2==num1**2):
    print("yes")
else:
    print("no")

