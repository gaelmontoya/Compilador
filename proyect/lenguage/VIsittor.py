from .Gramar_ideVisitor import Gramar_ideVisitor
from .Gramar_ideParser import Gramar_ideParser

class VIsittor(Gramar_ideVisitor):

    # Definicion de memoria del entorno 
    def __init__(self):
        self.memory = {}

    # Definicion de asignacion
    def visitAssign(self,ctx):
        # Se obtiene el nombre o id de la varibale. 
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value

    # Definicion de la impresion 
    def visitPrint(self,ctx):
        value=self.visit(ctx.expr())
        print(value)

    # Definicion de expresiones
    def visitExpr(self,ctx):
        if ctx.ID():
            name=ctx.ID().getText()
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            return self.memory[name]
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                if right == 0:
                    raise ValueError("Division por cero inexistente")
                return left / right
            
            