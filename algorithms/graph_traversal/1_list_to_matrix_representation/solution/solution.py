adjacency_list = {
  0:  [0, 1, 3],
  1:  [3, 4],
  2:  [1],
  3:  [0, 2],
  4:  []
}

adjacency_matrix = []

matrix_len = len(adjacency_list.keys())
for row in range(matrix_len):
    for col in range(matrix_len):
        my_matrix = []
        my_matrix.append(0)
        adjacency_matrix.append(list(my_matrix))

print(adjacency_matrix)