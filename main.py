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
precountedmd = open('precounted.md','r').read().split('$$$$$$')

context_i = 0
out = open('out_calculated_no_rus.md', 'w+')


variables = []
unevariables = []
comments_dict = {}
var_dict = {}
var_name_dict = {}
for line, comment, units in constants:
    if not line:
        continue
    if ':' in line:
        name, val = line.split(':')
        val = val.strip()
    else:
        clean_nm = line.split('=')[0]
        eq = parse_latex(line)
        subsed = eq.subs(variables)
        # print(line, subsed)
        name, val = subsed.args
    # print(str(val))
    outname = decode(str(name))
    var_name_dict[outname] = clean_nm.strip()
    # print(outname, clean_nm)
    if str(val) != 'NULL' and ':' not in line:
        variables.append((name, float(val)))
        unevariables.append((name, UnevaluatedExpr(S.One*val)))
        var_dict[outname] = float(val)
    elif str(val) != 'NULL':
        var_dict[outname] = val
    print(f'var: {outname} val: {val} units: {units}')
    comments_dict[outname] = comment

preid = input('Input line to start from: ')
if not preid:
    preid = 1
    context_i = 0
else:
    preid = int(preid) 
    context_i = preid
for line in precounted[:preid-1]:
    if not line or line.startswith('$'):
        continue
    if line.startswith('%$'):
        line, comment = line[2:].split('<comment>')
        comment, clean_nm = comment.split('<cleannm>')
        outname = line.split('=')[0]
        var_name_dict[outname.strip()] = clean_nm.strip()
        continue
    line, comment = line.split('<comment>')
    comment, clean_nm = comment.split('<cleannm>')
    outname = line.split('=')[0]
    # print(line, subsed)
    eq = parse_latex(line)
    subsed = eq.subs(variables)
    name, val = subsed.args
    variables.append((name, float(val)))
    unevariables.append((name, UnevaluatedExpr(S.One*val)))
    i = 0
    outname = decode(str(name))
    print(f'precounted: {line}, outname: {outname}, cleannm: {clean_nm}, val: {float(val)}')
    var_dict[outname] = float(val)
    var_name_dict[outname] = clean_nm.strip()
    comments_dict[outname] = comment

precout = open('precounted.txt', 'w+')
precoutmd = open('precounted.md', 'w+')
precout.write('\n'.join(precounted[:preid-1]) + '\n')
precoutmd.write('$$$$$$'.join(precountedmd[:preid-1]) + '$$$$$$')
out.write('\n'.join(precountedmd[:preid-1]))


for line, comment, where_flag, digs, units in formulas[context_i:]:
    context[context_i] = context[context_i].format(**var_dict)
    if not line:
        continue
    if line.count('=') > 1:
        if not isinstance(digs, int):
            digs = 5
        line_two = line.split('=')
        line = '='.join(line.split('=')[:2])
        # print(line)
        eq = parse_latex(line)
        subsed = eq.subs(variables)
        name, val = subsed.args
        # subsed = Eq(name, val)
        unevalsubsed = eq.subs(unevariables)
        
        la_uneval = latex(unevalsubsed) 
        la_subs = latex(subsed)

        variables.append([name, float(val)])
        # print('line: ', line, '_eq_', eq, '_lasubs_', la_subs,'_val_',  val, '_subsed_', subsed)
        outname = decode(str(name))
        print(context_i, f'line: {line}, eq: {eq}, subsed: {subsed}, outname: {outname}')
        comments_dict[outname] = comment
        var_name_dict[outname] = line_two[0].strip()
        # print('cleannames', outname,  line_two[0].strip())

        unevariables.append((name, UnevaluatedExpr(round(float(val), digs))))
        out_line = context[context_i] + f"$$\n {line} = {la_uneval.split("=")[-1]}" 
        where_part = '\n$$\n'
        if where_flag:
            where_part = ',\n$$\n где'
            for var in eq.atoms():
                var = decode(str(var))
                # print(var, eq)
                if var in comments_dict and comments_dict[var] != '':
                    where_part += f';\n<br> ${var_name_dict[var]}$ -- {comments_dict[str(var)]}'
                    comments_dict.pop(var)
            where_part = where_part.replace('где;\n<br> ', 'где ') + '.'
            if where_part == ',\n$$\n где.':
                where_part = '\n$$\n'
        out_line += f" = {round(float(val), digs)} {units}{where_part}"

        # FOR CONTEXT:
        context_i += 1
        precout.write(f"{line_two[0]} = {float(val)}<comment>{comment}<cleannm>{line_two[0].strip()}\n")
        out.write(out_line)
        precoutmd.write(out_line + '$$$$$$')
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

        # print(line, eq, eq.args)
        var_nm_drt = decode(str(eq.args[0]))
        var_name_dict[var_nm_drt] = line.split('=')[0].strip()
        comments_dict[var_nm_drt] = comment
        # print('latex', line, eq, lateq) #, latex(unevalved))
        print(context_i, f'line_{context_i}:', lateq)

        where_part = '\n$$\n'
        if where_flag:
            where_part = ',\n$$\n где'
            for var in eq.atoms():
                # print(str(var), eq, str(var) in comments_dict)
                var = decode(str(var))
                # print(var, eq)
                if var in comments_dict and comments_dict[var] != '':
                    where_part += f';\n<br> ${var_name_dict[var]}$ -- {comments_dict[var]}'
                    comments_dict.pop(var)
            where_part = where_part.replace('где;\n<br> ', 'где ') + '.'
            if where_part == ',\n$$\n где.':
                where_part = '\n$$\n'

        out_line = context[context_i] + f"$$\n {line} {where_part}"
        context_i += 1

        out.write(out_line)
        precout.write(f"%${line}<comment>{comment}<cleannm>{line.split('=')[0].strip()}\n")
        precoutmd.write(out_line + '$$$$$$')


precout.close()
precoutmd.close()
out.write(context[-1])
out.close()
