# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:* 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

N=int(input("Введите число N: "))
print(f"{N} -> ", end = " ")
for i in range(-N,N+1):
    print(i, end = " ")