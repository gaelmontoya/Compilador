from antlr4 import *
from lenguage.Gramar_ideLexer import Gramar_ideLexer
from lenguage.Gramar_ideParser import Gramar_ideParser

import io
import sys
from lenguage.VIsittor import VIsittor

def run_code(code:str):
    input_stream = inputStream(code)
    lexer = Gramar_ideLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Gramar_ideParser(stream)
    tree=parser.program()

    old_stdout = sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    visitor = VIsittor
    visitor.visit(tree)

    output=buf.getvalue()

    return output