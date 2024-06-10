def get_matrix (n, m, value):   # Объявление функции
    matrix = []     # Создание пустого списка
    for i in range(n):  # цикл для кол-во строк
        matrix.append([])   # добавление строк из переменной n
        for j in range(m):  # цикл для кол-во столбцов
            matrix[i].append(value) # заполняет значение value
    return matrix

matrix1 = get_matrix(2, 2, 10)
matrix2 = get_matrix(3, 5, 42)
matrix3 = get_matrix(4, 2, 13)

print(matrix1)
print(matrix2)
print(matrix3)
