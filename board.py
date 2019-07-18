import random

with open('words.txt', 'r') as f_in:
    words = []
    for line in f_in:
        words.append(line.replace('\n', ''))

chosen = []
index = random.randint(0, len(words))
for i in range(1,26):
    while index in chosen:
        index = random.randint(0, len(words) - 1)
    chosen.append(index)
    # print('{0}: {1} - {2}'.format(i, index, words[index]))

with open('board.csv', 'w') as f_out:
    for i in range(0, 5):
        for j in range(0, 5):
            f_out.write('{0},'.format(words[chosen[5*i + j]]))
        f_out.write('\n')
