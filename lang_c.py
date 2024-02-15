file = open('kp_1_c.json', 'r').read()

out = open('kp_1_c_no_rus.json', 'w+')

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

file = open('kp_2_c.json', 'r').read()

out = open('kp_2_c_no_rus.json', 'w+')

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
'''



file = open('r_kp.md', 'r').read()

out = open('rr_kp.md', 'w+')
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
'''
