
my_lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]

def frequency_array(lst):
    high_num = max(lst)
    new_lst_len = high_num + 1
    new_lst = []
    my_dict = {}
    for elem in lst:
        num_count = lst.count(elem)
        my_dict.update({elem: num_count})
    print(my_dict)

x = frequency_array(my_lst)