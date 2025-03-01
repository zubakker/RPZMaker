file = open('inp_constants.json', 'r').read()
out = open('inp_constants_no_rus.json', 'w+')

i = 0
while i < len(file):
    letter = file[i]
    if ord('а') <= ord(letter) <= ord('я') or \
            ord('А') <= ord(letter) <= ord('Я'):
        out.write('Z_{' + str(ord(letter)) + "}")
    elif letter == '.' and not file[i-1].isdigit():
        out.write('\\\\.')
    else:
        out.write(letter)
    i += 1
out.close()
