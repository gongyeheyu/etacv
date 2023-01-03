ver = '22.c14w'
keyword = ['var','print','input','if','else','return','def','fun','sleep','continue','break',
    'int','float','str','bool','null','none','true','false']
operator = ['+','-','*','/','^','%']
compator = ['==','!=','<','>','<=','>=']
filename = 'E:\\etacv\\t.ecv'
count = len(open(r"E:\\etacv\\t.ecv",'r').readlines())
var = {}
vint = {}
vfloat = {}
vstr = {}
vbool = {}

def run():
    #output
    t = text
    tlen = textlen
    if t[0] in keyword:
        if t[0] == 'print':
            if t[1][0] and t[-1][-1] == '"':    #第一个和最后一个字符为"
                del t[0]
                outf = " ".join(t)  #以空格连接为字符串
                print(outf[1:-1])
            else:
                print(var.get(t[1]))
        #var
        if t[0] == 'int':
            if '.' in t[1]:
                print('e: wrong value type')
            vint[t[1]] = int(t[3])
            print(vint['t'])   
        if t[0] == 'float':
            if '.' not in t[1]:
                print('e: wrong value type')
            vfloat[t[1]] = float(t[3])
        if t[0] == 'str':
            vstr[t[1]] = str(t[3])
        if t[0] == 'bool':
            if str(t[3]) == '0':
                vbool[t[1]] = 'false'
            elif str(t[3]) == '1':
                vbool[t[1]] == 'true'

    if t[0] in varlist:
        #=
        if t[1] == '=':
            if tlen == 3:
                dict[t[0]] = t[2]
            else:
                #+
                if t[3] == '+':
                    if t[2] in var:
                        t2 = True
                    if t[4] in var:
                        t4 = True
                    if not t2 and not t4:
                        new = t[2] + t[4]
                        dict[t[0]]=new
                    if t2 and t4:
                        new = dict[t[2]] + dict[t[4]]


def check():
    if text[0] in keyword:
        run()
    elif text[1] in operator:
        run()
    elif text[0] in varlist:
        run()
    else:
        print('error:wrong keyword or value')

import linecache
line = 1
while line <= count :
    text = linecache.getline (filename,line)
    text = text.split()
    varlist = var.keys()
    textlen = len(text) 
    check()
    line = line + 1