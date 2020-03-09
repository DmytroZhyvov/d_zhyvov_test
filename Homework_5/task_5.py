def clean_string(data):
    result = ''.join([letter for letter in data if letter.isalpha()])
    return result


# Tasks 5_1

my_list = [2**x for x in range(0, 21)]
# print(my_list)

# Task 5_2

original_list2 = [3, 5, 17, 75, 90, -2, -8, 56, 0]
new_list2 = [x % 3 for x in original_list2]
# print(new_list2)


# Task 5_3

original_list3 = ['abc', 19.00, [1, 2, 3, 4], -20, {'key': 'value'}, 100, '245']
new_list3 = [x for x in original_list3 if type(x) == int or type(x) == float]
# print(new_list3)

# Task 5_4

original_list = ['Absc12asas', 19.00, [1, 2, 3, 4], -20, {'key': 'value'}, 100, '245', 'bingo']
sorted_list = [x for x in original_list if type(x) == str]
clean_list = [clean_string(x) for x in sorted_list if not clean_string(x) == '']
# print(clean_list)

# Task 5_5_1

characteristics = {'name': 'Dmytro', 'surname': 'Zhyvov', 'age': 35, 'position': 'QA', 'address': 'Ukraine, Kyiv1, 222',
                   'skills': ['API', 'GUI']}

new_dict = {k:  type(v) for (k, v) in characteristics.items()}
# print(new_dict)



# Task 5_5_2
characteristics = {'name': 'Dmytro', 'surname': 'Zhyvov', 'age': 35, 'position': 'QA', 'address': 'Ukraine, Kyiv1, 222',
                   'skills': ['API', 'GUI']}
new_dict = {k: clean_string(v).lower() for (k, v) in characteristics.items() if type(v) == str}
# print(new_dict)




