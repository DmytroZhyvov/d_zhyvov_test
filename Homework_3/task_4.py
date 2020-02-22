# Task 4

# 4.1
# Delete list elements.

my_list = [1, 2, 3, 4, 5, 6, 7]

while my_list:
    print(my_list.pop(0), my_list)

print('The end!')


# 4.2
# Delete string elements.

my_string = "abcdefgh"
i = 0

while my_string:
    print(my_string[i], my_string[i:])
    my_string = my_string[1:]
print('The end!')


# 4.3
# Delete all ascending.

my_list = [5, 6, 3, 43, 523, 64, 7]

while my_list:
    my_list.sort()
    print(my_list.pop(0), my_list)

print('The end!')


# 4.4
# TODO


