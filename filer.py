

def exctract_data() -> list:
    new_list = []

    with open('fil_att_läsa_in.txt', 'r', encoding='utf-8') as f:
        for line in f:
            first_word = line[line.index('-') + 1:line.index(':')]

            list_of_line = line.split(':')

            second_word = list_of_line[1]

            gröt = list_of_line[2]

            third_word = gröt[gröt.index('_')+1 : gröt.index(';')]

            last_word = gröt[gröt.index('>')+ 1:]

            new_list.append([first_word, second_word, third_word, last_word])

    return new_list
if __name__ == '__main__':

    data = exctract_data()

    for word_list in data:
        print(word_list)