import sympy
from sympy import *
from sympy.parsing.latex import parse_latex

from json import loads


formulas  = loads(open('inp_formulas_no_rus.json', 'r').read())
constants = loads(open('inp_constants_no_rus.json', 'r').read())
context_one = open('inp_template.md', 'r').read().split("$$\n$$")

precounted = open('precounted.txt', 'r').read().split('\n')
precout = open('precounted.txt', 'w+')
precountedmd = open('precounted.md','r').read().split('$$$$$$')
precoutmd = open('precounted.md', 'w+')

context_i = 0
out = open('r_kp.md', 'w+')


variables = []
unevariables = []
var_dict = {}
for line, comment in constants:
    if not line:
        continue
    eq = parse_latex(line)
    subsed = eq.subs(variables)
    # print(line, subsed)
    name, val = subsed.args
    variables.append((name, float(val)))
    unevariables.append((name, UnevaluatedExpr(S.One*val)))
    i = 0
    outname = ''
    name = str(name)
    while i < len(name):
        letter = name[i]
        if letter == 'Z':
            if name[i+2] == "{":
                num = name[i+3] + name[i+4] + name[i+5] + name[i+6]
                i += 2
            else:
                num = name[i+2] + name[i+3] + name[i+4] + name[i+5]
            outname += chr(int(num))
            i += 6
        else:
            outname += letter
            i += 1

    outname = outname.replace('(', '')
    outname = outname.replace(')', '')
    outname = outname.replace('{', '(')
    outname = outname.replace('}', ')')
    outname = outname.replace('*', '')
    print(outname, float(val))
    var_dict[outname] = float(val)

preid = input('Input line to start from: ')
if not preid:
    preid = 1
    context_i = 0
else:
    preid = int(preid) 
    context_i = preid
for line in precounted[:preid -1 ]:
    if not line or line.startswith('$'):
        continue
    print('precounted:', line)
    # print(line, subsed)
    eq = parse_latex(line)
    subsed = eq.subs(variables)
    name, val = subsed.args
    variables.append((name, float(val)))
    unevariables.append((name, UnevaluatedExpr(S.One*val)))
    i = 0
    outname = ''
    name = str(name)
    while i < len(name):
        letter = name[i]
        if letter == 'Z':
            if name[i+2] == "{":
                num = name[i+3] + name[i+4] + name[i+5] + name[i+6]
                i += 2
            else:
                num = name[i+2] + name[i+3] + name[i+4] + name[i+5]
            outname += chr(int(num))
            i += 6
        else:
            outname += letter
            i += 1

    outname = outname.replace('(', '')
    outname = outname.replace(')', '')
    outname = outname.replace('{', '(')
    outname = outname.replace('}', ')')
    outname = outname.replace('*', '')
    print(outname, float(val))
    var_dict[outname] = float(val)
precout.write('\n'.join(precounted[:preid-1]) + '\n')
precoutmd.write('$$$$$$'.join(precountedmd[:preid-1]) + '$$$$$$')
out.write('\n'.join(precountedmd[:preid-1]))


for line in formulas[context_i+1:]:
    context[context_i] = context[context_i].format(**var_dict)
    if not line:
        if context_i == 103:
            out_line = context[context_i]

            context_i += 1
            out.write(out_line)
            precoutmd.write(out_line + '$$$$$$')
            continue
        context_i += 1
        continue
    if line.count('=') > 1:
        line_two = line.split('=')
        line = '='.join(line.split('=')[:2])
        # print(line)
        eq = parse_latex(line)
        subsed = eq.subs(variables)
        print(context_i, 'line: ', line,  eq, subsed)
        name, val = subsed.args
        subsed = Eq(name, val)
        unevalsubsed = eq.subs(unevariables)
        
        la_uneval = latex(unevalsubsed) 
        la_subs = latex(subsed)

        variables.append(subsed.args)
        # print('line: ', line, '_eq_', eq, '_lasubs_', la_subs,'_val_',  val, '_subsed_', subsed)
        unevariables.append((name, UnevaluatedExpr(round(float(val), 5))))
        # FOR CONTEXT:
        out_line = context[context_i]
        out_line += "$$\n " +line + " = " + la_uneval.split("=")[-1]
        out_line += " = " + str(round(float(val), 5)) + " \n$$\n"

        context_i += 1
        precout.write(line_two[0] + ' = {:f}'.format(float(val)) + '\n')
        out.write(out_line)
        precoutmd.write(out_line + '$$$$$$')
        outname = ''
        name = str(name)
        # print(name)
        i = 0
        while i < len(name):
            letter = name[i]
            if letter == 'Z':
                if name[i+2] == "{":
                    num = name[i+3] + name[i+4] + name[i+5] + name[i+6]
                    i += 2
                else:
                    num = name[i+2] + name[i+3] + name[i+4] + name[i+5]
                outname += chr(int(num))
                i += 6
            else:
                outname += letter
                i += 1

        # print(outname)
        outname = outname.replace('(', '')
        outname = outname.replace(')', '')
        outname = outname.replace('{', '(')
        outname = outname.replace('}', ')')
        outname = outname.replace('*', '')
        # print(outname, float(val))
        var_dict[outname] = float(val)
        # print(out_line)
    elif line.count('=') == 0:
        eq = parse_latex(line)
        unevalsubsed = eq.subs(unevariables)
        subsed = eq.subs(variables)
        la_uneval = latex(unevalsubsed)
        la_eval = latex(subsed)
        print(context_i, 'line_0: ', line, '_unev_', la_uneval,'_eval_', '_subs_', subsed)
        if type(subsed) == sympy.logic.boolalg.BooleanTrue or \
                 type(subsed) == sympy.logic.boolalg.BooleanFalse:
            out_line = context[context_i]
            out_line += "$$\n " +line + "\\\\" + la_uneval + "\n$$\n"
            context_i += 1

            out.write(out_line)
            precout.write('$' + line + "\\\\" + la_uneval + '\n')
            precoutmd.write(out_line + '$$$$$$')
        else:
            out_line = context[context_i]
            out_line += "$$\n " +line + "\n$$\n"
            context_i += 1
            # out.write("$$\n " +line +  " = " + la_uneval +  " = " + la_eval + "\n$$\n")
            out.write(out_line)
            precout.write('$' + line + '\n')
            precoutmd.write(out_line + '$$$$$$')

    else:
        eq = parse_latex(line)
        lateq = latex(eq)
        # print('latex', line, eq, lateq) #, latex(unevalved))
        print(context_i, 'line_1:', lateq)
        out_line = context[context_i]
        out_line += "$$\n " +line + " \n$$\n"
        context_i += 1

        out.write(out_line)
        precout.write('$' + line + '\n')
        precoutmd.write(out_line + '$$$$$$')


