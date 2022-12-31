ver = '22.c14w'
keyword = ['var','print','input','if','else','return','def','fun','sleep','continue','break',
    'int','float','string','bool','null','none','true','false']
operator = ['+','-','*','/','^','%']
compator = ['==','!=','<','>','<=','>=']
filename = 'D:\\vsc\\javapro\\etacv\\t.ecv'
count = len(open(r"D:\\vsc\\javapro\\etacv\\t.ecv",'r').readlines())
var = {}

def run():
    #output
    if text[0] == 'print':
        if text[1][0] and text[-1][-1] == '"':
            del text[0]
            outf = " ".join(text)
            print(outf[1:-1])
        else:
            print(var.get(text[1]))
    #var
    if text[0] == 'var':
        var[text[1]] = text[3]
        print(var['t'])   
    #+
    if text[3] == '+':
        if text[2] in var:
            t2 = True
        if text[4] in var:
            t4 = True
        if t2 and t4 != True:
            new = text[2] + text[4]
            dict[text[0]]=new


def check():
    if text[0] in keyword:
        run()
    elif text[1] in operator:
        run()
    else:
        print('error:wrong keyword')

import linecache
line = 1
while line <= count :
    text = linecache.getline (filename,line)
    text = text.split()
    check()
    line = line + 1