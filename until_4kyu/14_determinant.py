def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        result = 0
        for i in range(len(matrix[0])):
            minor = []
            for row in matrix[1:]:
                minor.append(row[:i] + row[i+1:])
                sign = 1 if i % 2 == 0 else -1
            result += sign * matrix[0][i] * determinant(minor)
        return result


m1 = [[1, 3], [2, 5]]
m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]

assert determinant([[1]]) == 1
assert determinant(m1) == -1
assert determinant(m2) == -20
