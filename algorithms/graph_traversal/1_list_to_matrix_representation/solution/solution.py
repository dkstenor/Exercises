import pprint

adjacency_list = {
  0:  [0, 1, 3],
  1:  [3, 4],
  2:  [1],
  3:  [0, 2],
  4:  []
}

adjacency_matrix = []

matrix_len = len(adjacency_list.keys())

for i in range(matrix_len):
  adjacency_matrix.append([])

for row in range(matrix_len):
  for col in range(matrix_len):
    adjacency_matrix[row].append(0)

for key, value in adjacency_list.items():
  for v in value:
    adjacency_matrix[key][v] = 1
  
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(adjacency_matrix)