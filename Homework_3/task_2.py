# Task 2

# Split input into two parts. Reverse the order of input parts. Display the input.

while True:
    value = input('Please, enter your value: ')  # User input.
    value_length = int(len(value))  # Input length.

    if value_length < 2:  # Checks if input symbols quantity is enough.
        print('Min length of value is 2 symbols.')  # Asks user to enter a valid value.
    else:

        # Defines index of the last symbol
        if value_length % 2 == 0:
            last_symbol = int(value_length / 2)
        else:
            last_symbol = int(value_length // 2) + 1

        first_part = value[:last_symbol]   # First input part.
        second_part = value[last_symbol:]  # Second input part.

        print(second_part + first_part)  # Displays the modified input.
        break

