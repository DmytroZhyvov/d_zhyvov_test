# Task 5
# Input two values. Check if inputs are numbers. Depending on inputs type - sum or concatenate.

value1 = input('Please enter the first value: ')  # Asks for the first input.
value2 = input('Please enter the second value: ')  # Asks for the first input.

try:
    print(float(value1) + float(value2))
except:
    print(value1+value2)

