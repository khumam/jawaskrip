tokens = []


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
        elif tok == ">=" and state == 0:
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
        elif tok == ".":
            tokens.append("SAMBUNG")
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
        elif tok == "kirang" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            if tokens[-1] == "LOW":
                tokens[-1] = "LW"
            else:
                tokens.append("LOW")
            tok = ""
        elif tok == "langkung" and state == 0:
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varStarted = 0
            if tokens[-1] == "GREATHER":
                tokens[-1] = "GT"
            else:
                tokens.append("GREATHER")
            tok = ""
        elif tok == "SERAT" or tok == "serat":
            tokens.append("PRINT")
            tok = ""
        elif tok == "LEBET" or tok == "lebet":
            tokens.append("LEBET")
            tok = ""
        elif tok == "SAMPUN" or tok == "sampun":
            tokens.append("SAMPUN")
            tok = ""
        elif tok == "MENAWI" or tok == "menawi":
            tokens.append("MENAWI")
            tok = ""
        elif tok == "KANGGE" or tok == "kangge":
            tokens.append("KANGGE")
            tok = ""
        elif tok == "NGANTOS" or tok == "ngantos":
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            tokens.append("NGANTOS")
            tok = ""
        elif tok == "MILA" or tok == "mila":
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            tokens.append("MILA")
            tok = ""
        elif tok == "BENTEN" or tok == "benten":
            if expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                expr = ""
            tokens.append("BENTEN")
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

    return tokens
