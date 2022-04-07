"""
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной
и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце
нужно поменять местами элемент на главной диагонали и на побочной диагонали).

*Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем
элементы матрицы построчно через пробел.

*Формат выходных данных
Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.
"""

n = int(input())

matrix = []

for i in range(n):
    elem = input().split()
    matrix.append(elem)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j or i == n-1-j:
            print(matrix[n-i-1][j], end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()