# Original string
char_string = 'We are not what we should be!\nWe are not what we need to be.\n' \
         'But at least we are not what we used to be.\n(Football Coach)'

# Lowercase string
lower_string = char_string.lower()  # or .casefold() may be used

# List of words with punctuation
char_words = char_string.split()

# List of words without punctuation
words = []

# List of lowercase words without punctuation
lower_words = []

for x in char_words:
    x = x.strip("'.', ',', '!', '(', ')'")
    words.append(x)
    x = x.lower()
    lower_words.append(x)

string = ' '.join(words)

# List of sorted lowercase words
sorted_words = sorted(lower_words)

# Repeated words dictionary
words_dict = {}

for x in lower_words:
    if x in words_dict:
        words_dict[x] += 1
    else:
        words_dict[x] = 1

separator = "*******"

print(char_string)  # displays original string
print(separator)

print('There are {} words in the string.'.format(len(words)))  # displays the total quantity of words
print(separator)

print(string)  # displays string without symbols
print(separator)

print(sorted_words)  # displays string with ordered words
print(separator)

print(words_dict)  # displays quantity of each word
