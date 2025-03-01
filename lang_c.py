from json import loads, dumps

file = loads(open('inp_constants.json', 'r').read())
out = open('inp_constants_no_rus.json', 'w+')

outlist = []
for line, comment in file:
    i = 0
    outline = ''
    while i < len(line):
        letter = line[i]
        if ord('а') <= ord(letter) <= ord('я') or \
                ord('А') <= ord(letter) <= ord('Я'):
            outline += 'Z_{' + str(ord(letter)) + "}"
        elif letter == '.' and not file[i-1].isdigit():
            outline += '\\\\.'
        else:
            outline += letter
        i += 1
    outlist.append([outline, comment])
out.write(dumps(outlist))
out.close()
