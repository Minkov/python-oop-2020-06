def flip_matrix(matrix):
    result = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if len(result) <= column:
                result.append([])
            result[column].append(matrix[row][column])
    return result
