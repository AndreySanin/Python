# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def odd_sum(my_list):
    if len(my_list)==0:
        return "Пустой список"
    else:
        sum=0
        for i in range(len(my_list)):
            if i%2==1:
                sum+=my_list[i]
        return sum

my_list=[2, 3, 5, 9, 3] # ввод списка
print(odd_sum(my_list))