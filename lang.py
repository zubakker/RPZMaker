file = open('out_calculated_no_rus.md', 'r').read()
out = open('out_calculated.md', 'w+')
i = 0
while i < len(file):
    letter = file[i]
    if letter == 'Z':
        if file[i+2] == "{":
            num = file[i+3] + file[i+4] + file[i+5] + file[i+6]
            i += 2
        else:
            num = file[i+2] + file[i+3] + file[i+4] + file[i+5]
        out.write(chr(int(num)))
        i += 6
    else:
        out.write(letter)
        i += 1
out.close()
