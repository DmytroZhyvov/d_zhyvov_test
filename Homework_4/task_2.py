# Task 2


def get_second_arg(*args):
    my_list = []
    for x in sorted(args):
        if x not in my_list:
            my_list.append(x)
    result = my_list[1]
    return result


print(get_second_arg(0, 1, 1, 2))


