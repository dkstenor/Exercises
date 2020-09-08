# Write your solution here
import operator

def sort_dict(my_dictionary):
    my_tup = (sorted(my_dictionary, key=operator.itemgetter(0)))
    new_dict = {}
    for item in my_tup:
        new_dict[item] = my_dictionary[item]

    return new_dict

dict = sort_dict({"Jim": 71, "David": 57, "Simba": 10, "Rufus": 7})
print(dict)