from sys import *
import re

tokens = []
num_stack = []
symbols = {}


def open_file(filename):
    if(".jws" in filename):
        data = open(filename, "r").read()
        data += "<EOF>"
        return data
    else:
        exit()


def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    varStarted = 0
    isexpr = 0
    expr = ""
    n = ""
    var = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            elif var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            tok = ""
        elif tok == "=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            if tokens[-1] == "EQUALS":
                tokens[-1] = "EQEQ"
            else:
                tokens.append("EQUALS")
            tok = ""
        elif tok == "<=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            if tokens[-1] == "LOWEQUALS":
                tokens[-1] = "LWEQ"
            else:
                tokens.append("LOWEQUALS")
            tok = ""
        elif tok == "=" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            if tokens[-1] == "GREATEQUALS":
                tokens[-1] = "GTEQ"
            else:
                tokens.append("GREATEQUALS")
            tok = ""
        elif tok == "@" and state == 0:
            varStarted = 1
            var += tok
            tok = ""
        elif varStarted == 1:
            if tok == "<" or tok == ">":
                if var != "":
                    tokens.append("VAR:" + var)
                    var = ""
                    varStarted = 0
                    tok = ""
            var += tok
            tok = ""
        elif tok == "SERAT" or tok == "serat":
            tokens.append("PRINT")
            tok = ""
        elif tok == "LEBET" or tok == "lebet":
            tokens.append("LEBET")
            tok = ""
        elif tok == "BIBARMENAWI" or tok == "bibarmenawi":
            tokens.append("BIBARMENAWI")
            tok = ""
        elif tok == "MENAWI" or tok == "menawi":
            tokens.append("MENAWI")
            tok = ""
        elif tok == "MILA" or tok == "mila":
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            tokens.append("MILA")
            tok = ""
        elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
            expr += tok
            tok = ""
        elif tok == "+" or tok == "/" or tok == "-" or tok == "*" or tok == "(" or tok == ")" or tok == "%":
            isexpr = 1
            expr += tok
            tok = ""
        elif tok == "\t":
            tok = ""
        elif tok == "\"" or tok == " \"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    # print(tokens)
    # return ''
    return tokens


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


def doPrint(toPrint):
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

# TODO: Membuat fungsi inputan


def getInput(string, varname):
    i = input(string[1:-1])
    symbols[varname] = "STRING:\"" + i + "\""


def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] == "BIBARMENAWI":
            i += 1
        elif toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR" or toks[i] + " " + toks[i+1][0:3] == "PRINT VAR":
            if toks[i+1][0:6] == "STRING":
                doPrint(toks[i+1])
            elif toks[i+1][0:3] == "NUM":
                doPrint(toks[i+1])
            elif toks[i+1][0:4] == "EXPR":
                doPrint(toks[i+1])
            elif toks[i+1][0:3] == "VAR":
                doPrint(getVariabel(toks[i+1]))
            i += 2
        elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
            if toks[i+2][0:6] == "STRING":
                doAssign(toks[i], toks[i+2])
            elif toks[i+2][0:3] == "NUM":
                doAssign(toks[i], toks[i+2])
            elif toks[i+2][0:4] == "EXPR":
                doAssign(toks[i], "NUM:" + str(evaluationExpr(toks[i+2][5:])))
            elif toks[i+2][0:3] == "VAR":
                doAssign(toks[i], getVariabel(toks[i+2]))
            i += 3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "LEBET STRING VAR":
            getInput(toks[i+1][7:], toks[i+2][4:])
            i += 3
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "MENAWI NUM EQEQ NUM MILA":

            if toks[i+1][4:] == toks[i+3][4:]:
                i += 5
            else:
                return 0

        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "MENAWI NUM GREATEQUALS NUM MILA":

            if toks[i+1][4:] == toks[i+3][4:]:
                i += 5
            else:
                return 0

        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "MENAWI NUM LOWEQUALS NUM MILA":

            if toks[i+1][4:] == toks[i+3][4:]:
                i += 5
            else:
                return 0


def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)


run()
