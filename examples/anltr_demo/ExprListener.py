# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#SingleTerm.
    def enterSingleTerm(self, ctx:ExprParser.SingleTermContext):
        pass

    # Exit a parse tree produced by ExprParser#SingleTerm.
    def exitSingleTerm(self, ctx:ExprParser.SingleTermContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#SingleFactor.
    def enterSingleFactor(self, ctx:ExprParser.SingleFactorContext):
        pass

    # Exit a parse tree produced by ExprParser#SingleFactor.
    def exitSingleFactor(self, ctx:ExprParser.SingleFactorContext):
        pass


    # Enter a parse tree produced by ExprParser#Number.
    def enterNumber(self, ctx:ExprParser.NumberContext):
        pass

    # Exit a parse tree produced by ExprParser#Number.
    def exitNumber(self, ctx:ExprParser.NumberContext):
        pass


    # Enter a parse tree produced by ExprParser#Parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#Parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass



del ExprParser