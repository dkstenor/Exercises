import pprint

adjacency_list = {}

adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
]

matrix_len = len(adjacency_list)
temp_list = []
#adjacency_list = dict.fromkeys(range(len(adjacency_matrix)), []) 
row_count = 0
for row in adjacency_matrix:
    list_enum = enumerate(row)
    for count,ele in list_enum: 
        if ele == 1:
            temp_list.append(count)
    adjacency_list[row_count] = temp_list
    row_count += 1
    temp_list = []

#print(adjacency_list)