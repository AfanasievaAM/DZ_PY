
#Упражнение №1
N=int(input("Введите целое число: "))
print(list(range(1, N+1, 2)))

#Упражнение №2
l=list("Иван, Глеб, Влад, Гоша, Артем, Евгений, Николай, Захар")
a = []

for i in range(len(l)):
    if i % 2 == 0:
        a.append(l[i])
print(a)

#Упражнение №3
A=int(input("Введите первое целое число: "))
B=int(input("Введите второе целое число: "))

if A != B:
    if A > B:
        print("Первое число больше второго:", A)
    else:
        print("Второе число больше первого:", B)
else:
    print("Числа равны: ", A, "=", B)

#Упражнение №4
Упражнение 4.
Дано натуральное число. Определите сумму и количество его цифр.
v=input("Введите число: ")

l=list(v)
print(l)
l1=len(l) #кол-во цифр
print(l1)

suma = 0

while a > 0:
    s = a % 10
    suma = suma + s
print(suma)




Упражнение 5.
В данном упражнении вы должны написать программу для подсчета среднего значения всех введенных пользователем чисел. Индикатором окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке, если первым же введенным пользователем значением будет ноль.


Упражнение 6.
В магазине была объявлена скидка размером 60 % на ряд товаров, и для того чтобы покупатели лучше ориентировались, владелец торговой точки решил вывесить отдельную таблицу со скидками с указанием уцененных товаров и их оригинальных цен. Используйте цикл для создания подобной таблицы, в которой будут исходные цены, суммы скидок и новые цены для покупок на сумму $4,95, $9,95, $14,95, $19,95 и $24,95. Убедитесь в том, что суммы скидки и новые цены отображаются с двумя знаками после запятой.

Упражнение 7.
Строка называется палиндромом, если она пишется одинаково в обоих направлениях. Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah». Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом.


Упражнение 8.
Вы загадываете число от 1 до 100 (включительно). Компьютер спрашивает у вас «Твое число равно, меньше или больше, чем число N?»,  где N — число, которое хочет проверить компьютер.
Вы отвечаете одним из трёх чисел:
1 — равно,
2 — больше,
3 — меньше.

Напишите программу, которая с помощью цепочки таких вопросов и ответов угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

