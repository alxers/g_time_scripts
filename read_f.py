import shutil

with open('input.txt') as old, open('output.txt', 'w') as new:
    lines = old.readlines()
    for idx, val in enumerate(lines):
        new.write(str(idx + 1) + ') ' + str(val))

shutil.move('output.txt', 'input.txt')
