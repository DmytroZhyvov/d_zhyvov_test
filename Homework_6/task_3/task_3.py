with open('original_text.txt', 'r') as f:    # open an original file
    my_list = []  # get a list of words
    for line in f:  # read a file line by line
        for word in line.split():
            clean_word = word.strip(".,?!...:;()").lower()  # get a word without punctuation
            my_list.append(clean_word)

    my_string = ''  # final string
    for element in sorted(set(my_list)):
        my_string += f'{element}: {my_list.count(element)} \n'

    with open('output_file.txt', 'w') as o:  # write a result into a new file
        o.writelines(my_string)