import re
def arithmetic_arranger(problems,show=False):
    arranged_problems = ""
    up = []
    down = []
    op = []
    res = []
    cont = 0
    size = 0
    j = 0
    err = 0
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
    else:
        cont = 0
        for i in problems:
            if not re.search('\S+\s[+-]\s\S+',i):
                arranged_problems = "Error: Operator must be '+' or '-'."
                err = 1
                break
            if re.search('[0-9][0-9][0-9][0-9][0-9]+',i):
                arranged_problems = "Error: Numbers cannot be more than four digits."
                err = 1
                break
            if re.search('[^0-9\s+-]',i):
                arranged_problems = "Error: Numbers must only contain digits."
                err = 1
                break
            up+=(re.findall('(\S+)\s[+-]\s\S+',i))
            down+=(re.findall('\S+\s[+-]\s(\S+)',i))
            op+=(re.findall('[+-]',i))
            if op[cont]=='+':
                res.append(int(up[cont])+int(down[cont]))
            elif op[cont]=='-':
                res.append(int(up[cont])-int(down[cont]))
            cont+=1
        #Imprimir la parte de arriba
        cont = 0
        if err!=1:
            for i in up:
                if cont != 0:
                    arranged_problems+="    "
                if len(i) > len(down[cont]):
                    size = len(i)+2
                else:
                    size = len(down[cont])+2
                j = size - len(i)
                while j>0:
                    arranged_problems+=" "
                    j -= 1
                arranged_problems+=i
                cont += 1
            cont = 0
            arranged_problems+='\n'
            #Imprimir la parte de abajo
            for i in down:
                if cont != 0:
                    arranged_problems+="    "
                if len(i) > len(up[cont]):
                    size = len(i)+1
                else:
                    size = len(up[cont])+1
                j = size - len(i)
                arranged_problems+=op[cont]
                while j>0:
                    arranged_problems+=" "
                    j -= 1
                arranged_problems+=i
                cont += 1
            cont = 0
            arranged_problems+='\n'
            #Imprimir la línea
            for i in up:
                if cont != 0:
                    arranged_problems+="    "
                if len(i) > len(down[cont]):
                    size = len(i)+2
                else:
                    size = len(down[cont])+2
                while size>0:
                    arranged_problems+="-"
                    size -= 1
                cont += 1
            #Imprimir el resultado
            if show:
                cont = 0
                arranged_problems+='\n'
                for i in res:
                    if cont != 0:
                        arranged_problems+="    "
                    if i<0:
                        maximo=[len(down[cont]),len(up[cont]),len(str(i))-1]
                    else:
                        maximo=[len(down[cont]),len(up[cont]),len(str(i))]
                    size=max(maximo)+2
                    j = size - len(str(i))
                    while j>0:
                        arranged_problems+=" "
                        j -= 1
                    arranged_problems+=str(i)
                    cont += 1
    return arranged_problems