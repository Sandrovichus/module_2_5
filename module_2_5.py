def get_matrix(n, m, value):
    matrix = []
    if value > 0 and n > 0 and m > 0:  # если значение аргумента отрицательное или 0 - возвращаем пустой список
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 0)
result2 = get_matrix(3, 5, -5)
result3 = get_matrix(4, 2, 27)
result4 = get_matrix(10, 3, 100)
print(result1)
print(result2)
print(result3)
print(result4)
