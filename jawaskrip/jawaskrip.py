from sys import *
import re
from jawaskrip_lexer import lex
from jawaskrip_parser import parse

# tokens = []
# num_stack = []
# symbols = {}


def open_file(filename):
    if(".jws" in filename):
        data = open(filename, "r").read()
        data += "<EOF>"
        return data
    else:
        print("Mboten jawaskrip file, pastikan ekstensi file .jws")
        exit()


def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)


run()
