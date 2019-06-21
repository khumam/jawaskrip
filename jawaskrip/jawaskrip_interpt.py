num_stack = []
symbols = {}


def evaluationExpr(expr):  # otomatis
    return eval(expr)


def evalExpr(expr):  # Manual
    expr = "," + expr
    i = len(expr) - 1
    num = ""
    while i >= 0:
        if expr[i] == "+" or expr[i] == "-" or expr[i] == "/" or expr[i] == "*" or expr[i] == "%":
            num = num[::-1]
            num_stack.append(num)
            num_stack.append(expr[i])
            num = ""
        elif expr[i] == ",":
            num = num[::-1]
            num_stack.append(num)
            num = ""
        else:
            num += expr[i]
        i -= 1
    print(num_stack)


def doPrint(toPrint, sambung):
    if toPrint[0:6] == "STRING":
        toPrint = toPrint[8:]
        toPrint = toPrint[:-1]
    elif toPrint[0:3] == "NUM":
        toPrint = toPrint[4:]
    elif toPrint[0:4] == "EXPR":
        toPrint = evaluationExpr(toPrint[5:])

    if(sambung == 1):
        print(toPrint + ' ')
    else:
        print(toPrint)


def doSambung(toPrint):
    if toPrint[0:6] == "STRING":
        toPrint = toPrint[8:]
        toPrint = toPrint[:-1]
    elif toPrint[0:3] == "NUM":
        toPrint = toPrint[4:]
    elif toPrint[0:4] == "EXPR":
        toPrint = evaluationExpr(toPrint[5:])
    print(toPrint)


def doAssign(varName, varValue):
    symbols[varName[4:]] = varValue


def getVariabel(varname):
    varname = varname[4:]
    if varname in symbols:
        return symbols[varname]
    else:
        return "Variabel " + varname + " boten kapriksan utawi dereng diinisialisasi"


def getInput(string, varname):
    i = input(string[1:-1])
    symbols[varname] = "STRING:\"" + i + "\""
