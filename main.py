import sympy
from sympy import *
from sympy.parsing.latex import parse_latex

from json import loads


def decode(text):
    i = 0
    outtext = ''
    while i < len(text):
        letter = text[i]
        if letter == 'Z':
            if text[i+2] == "{":
                num = text[i+3] + text[i+4] + text[i+5] + text[i+6]
                i += 2
            else:
                num = text[i+2] + text[i+3] + text[i+4] + text[i+5]
            outtext += chr(int(num))
            i += 6
        else:
            outtext += letter
            i += 1
    outtext = outtext.replace('(', '')
    outtext = outtext.replace(')', '')
    outtext = outtext.replace('{', '(')
    outtext = outtext.replace('}', ')')
    outtext = outtext.replace('*', '')
    return outtext


formulas  = loads(open('inp_formulas_no_rus.json', 'r').read())
constants = loads(open('inp_constants_no_rus.json', 'r').read())
context = open('inp_template.md', 'r').read().split("$$\n$$")

precounted = open('precounted.txt', 'r').read().split('\n')
precout = open('precounted.txt', 'w+')
precountedmd = open('precounted.md','r').read().split('$$$$$$')
precoutmd = open('precounted.md', 'w+')

context_i = 0
out = open('out_calculated_no_rus.md', 'w+')


variables = []
unevariables = []
comments_dict = {}
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
    outname = decode(str(name))
    print(f'var: {outname} val: {float(val)}')
    var_dict[outname] = float(val)
    comments_dict[outname] = comment

preid = input('Input line to start from: ')
if not preid:
    preid = 1
    context_i = 0
else:
    preid = int(preid) 
    context_i = preid
for line in precounted[:preid-1]:
    line, comment = line.split('<comment>')
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
    outname = decode(str(name))
    print(outname, float(val))
    var_dict[outname] = float(val)
    comments_dict[outname] = comment

precout.write('\n'.join(precounted[:preid-1]) + '\n')
precoutmd.write('$$$$$$'.join(precountedmd[:preid-1]) + '$$$$$$')
out.write('\n'.join(precountedmd[:preid-1]))


for line, comment, where_flag, digs, units in formulas[context_i:]:
    context[context_i] = context[context_i].format(**var_dict)
    if not line:
        context_i += 1
        continue
    if line.count('=') > 1:
        if not isinstance(digs, int):
            digs = 5
        line_two = line.split('=')
        comments_dict[str(parse_latex(line_two[0]))] = comment
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
        unevariables.append((name, UnevaluatedExpr(round(float(val), digs))))
        out_line = context[context_i] + f"$$\n {line} = {la_uneval.split("=")[-1]}" 
        if where_flag:
            where_part = ',\n$$\n где'
            for var in eq.atoms():
                if str(var) in comments_dict:
                    where_part += f';<br> ${var}$ -- {comments_dict[str(var)]}'
            where_part = where_part.replace('где;<br> ', 'где ') + '.'
            if where_part == ',\n$$\n где.':
                where_part = '\n$$\n'
        else:
            where_part = '\n$$\n'
        out_line += f" = {round(float(val), digs)} {units}{where_part}"

        # FOR CONTEXT:
        context_i += 1
        precout.write(f"{line_two[0]} = {float(val)}<comment>{comment}\n")
        out.write(out_line)
        precoutmd.write(out_line + '$$$$$$')
        outname = decode(str(name))
        # print(name)
        var_dict[outname] = float(val)
        # print(out_line)
    elif line.count('=') == 0:
        eq = parse_latex(line)
        unevalsubsed = eq.subs(unevariables)
        subsed = eq.subs(variables)
        la_uneval = latex(unevalsubsed)
        la_eval = latex(subsed)
        print(context_i, 'line_0: ', line, '_unev_', la_uneval,'_eval_', '_subs_', subsed)

        out_line = context[context_i]
        if type(subsed) == sympy.logic.boolalg.BooleanTrue or \
                 type(subsed) == sympy.logic.boolalg.BooleanFalse:
            n_line = f"{line}\\\\{la_uneval}\n"
        else:
            n_line =  f"{line}\n"
        out_line += '$$\n' + n_line + '$$\n'
        context_i += 1
        out.write(out_line)
        precout.write('$' + n_line)
        precoutmd.write(out_line + '$$$$$$')

    else:
        eq = parse_latex(line)
        lateq = latex(eq)
        # print('latex', line, eq, lateq) #, latex(unevalved))
        print(context_i, f'line_{context_i}:', lateq)
        out_line = context[context_i]
        out_line += "$$\n " +line + " \n$$\n"
        context_i += 1

        out.write(out_line)
        precout.write('$' + line + '\n')
        precoutmd.write(out_line + '$$$$$$')


