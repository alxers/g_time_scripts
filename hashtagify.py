import shutil

with open('input_h.txt') as old, open('output_h.txt', 'w') as new:
    for line in old:
        for word in line.split():
            new.write('#{} '.format(word))

shutil.move('output_h.txt', 'input_h.txt')
