
# Generated from MathOperations.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MathOperationsParser import MathOperationsParser
else:
    from MathOperationsParser import MathOperationsParser

# This class defines a complete listener for a parse tree produced by MathOperationsParser.
class MathOperationsListener(ParseTreeListener):

    # Enter a parse tree produced by MathOperationsParser#expr.
    def enterExpr(self, ctx:MathOperationsParser.ExprContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#expr.
    def exitExpr(self, ctx:MathOperationsParser.ExprContext):
        pass


    # Enter a parse tree produced by MathOperationsParser#operationExpr.
    def enterOperationExpr(self, ctx:MathOperationsParser.OperationExprContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#operationExpr.
    def exitOperationExpr(self, ctx:MathOperationsParser.OperationExprContext):
        pass


    # Enter a parse tree produced by MathOperationsParser#memExpr.
    def enterMemExpr(self, ctx:MathOperationsParser.MemExprContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#memExpr.
    def exitMemExpr(self, ctx:MathOperationsParser.MemExprContext):
        pass


    # Enter a parse tree produced by MathOperationsParser#resExpr.
    def enterResExpr(self, ctx:MathOperationsParser.ResExprContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#resExpr.
    def exitResExpr(self, ctx:MathOperationsParser.ResExprContext):
        pass


    # Enter a parse tree produced by MathOperationsParser#item.
    def enterItem(self, ctx:MathOperationsParser.ItemContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#item.
    def exitItem(self, ctx:MathOperationsParser.ItemContext):
        pass


    # Enter a parse tree produced by MathOperationsParser#op.
    def enterOp(self, ctx:MathOperationsParser.OpContext):
        pass

    # Exit a parse tree produced by MathOperationsParser#op.
    def exitOp(self, ctx:MathOperationsParser.OpContext):
        pass



del MathOperationsParser