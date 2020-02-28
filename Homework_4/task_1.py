#Task_1


def generate_song(line_quantity=4, word_quantity=5, last_symbol=0):

    line = "la-" * word_quantity
    song = (line[:-1] + '\n')*line_quantity
    if last_symbol == 0:
        song = song[:-1] + '.'
    else:
        song = song[:-1] + '!'

    return song

print(generate_song(4,5,0))