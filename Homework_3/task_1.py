# Task 1

# Display string symbols by index and exceptions if any.

value = input('Please, enter your value: ')  # User input.
value_length = len(value)  # Input symbols quantity.
elements_list = []  # A list of elements of all task cases.
error = 'IndexError - the value is too short.'  # Error message.

try:
    elements_list.append(value[2])  # the third input symbol / the first line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[-2])  # the next to the last input symbol / the second line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[:5])  # the first five input symbols / the third line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[:-2])  # the whole input except the last two symbols / # the fourth line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[::2])  # the input symbols with even indexes / # the fifth line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[1::2])  # the input symbols with odd indexes / # the sixth line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[::-1])  # the input symbols in reverse order / # the seventh line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[::-2])  # the next but one input symbols in reverse order / # the eighth line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[-2::-2])  # the next but one input symbols in reverse order starting the next
                                         # to the last / the ninth line
except IndexError:
    elements_list.append(error)

try:
    elements_list.append(value[-2:0:-1])  # input symbols in reverse order except the first and the last one /
                                          # the tenth line
except IndexError:
    elements_list.append(error)

finally:
    elements_list.append(value_length)

for elements in elements_list:
    print(elements)

