def count_islands(adjacency_list):
    count = 0
    for key in adjacency_list:
        if adjacency_list[key] == []:
            count += 1
    return count