import random

answers = []
with open('board.csv', 'r') as f_in:
    for line in f_in:
        elements = line.split(',')
        for element in elements:
            if element != '\n':
                answers.append(element)
#print(answers)

cells = []
for i in range(0,25):
    cells.append(i)
# print(cells)

blue = []
for i in range(0, 9):
    index = random.randint(0, len(cells) - 1)
    # print(index)
    # print(cells[index])
    blue.append(cells[index])
    cells.remove(cells[index])

# print('--------------------------')

red = []
for i in range(0, 8):
    index = random.randint(0, len(cells) - 1)
    # print(index)
    # print(cells[index])
    red.append(cells[index])
    cells.remove(cells[index])

assasin = cells[random.randint(0, len(cells) - 1)]
cells.remove(assasin)

# print(blue)
# print(red)
# print(assasin)
# print(cells)

with open ('key.csv', 'w') as f_out:
    for i in range(0, 5):
        for j in range(0, 5):
            if (5*i + j) in blue:
                f_out.write('A) {0},'.format(answers[5*i + j]))
            elif (5*i + j) in red:
                f_out.write('B) {0},'.format(answers[5*i + j]))
            elif (5*i + j) in cells:
                f_out.write('N) {0},'.format(answers[5*i + j]))
            else:
                f_out.write('X) {0},'.format(answers[5*i + j]))
        f_out.write('\n')
