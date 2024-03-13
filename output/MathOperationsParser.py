# Generated from MathOperations.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,3,0,31,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,75,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,92,8,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,3,9,100,0,30,1,
        0,0,0,2,41,1,0,0,0,4,49,1,0,0,0,6,74,1,0,0,0,8,91,1,0,0,0,10,93,
        1,0,0,0,12,13,5,1,0,0,13,14,3,2,1,0,14,15,5,2,0,0,15,31,1,0,0,0,
        16,17,5,1,0,0,17,18,3,4,2,0,18,19,5,2,0,0,19,31,1,0,0,0,20,21,5,
        1,0,0,21,22,3,6,3,0,22,23,5,2,0,0,23,31,1,0,0,0,24,25,5,1,0,0,25,
        26,5,11,0,0,26,27,3,8,4,0,27,28,3,10,5,0,28,29,5,2,0,0,29,31,1,0,
        0,0,30,12,1,0,0,0,30,16,1,0,0,0,30,20,1,0,0,0,30,24,1,0,0,0,31,1,
        1,0,0,0,32,33,3,8,4,0,33,34,3,8,4,0,34,35,3,10,5,0,35,42,1,0,0,0,
        36,37,3,8,4,0,37,38,5,12,0,0,38,39,3,8,4,0,39,40,3,10,5,0,40,42,
        1,0,0,0,41,32,1,0,0,0,41,36,1,0,0,0,42,3,1,0,0,0,43,44,3,8,4,0,44,
        45,5,11,0,0,45,50,1,0,0,0,46,47,3,6,3,0,47,48,5,11,0,0,48,50,1,0,
        0,0,49,43,1,0,0,0,49,46,1,0,0,0,50,5,1,0,0,0,51,52,5,1,0,0,52,53,
        3,8,4,0,53,54,5,12,0,0,54,55,5,2,0,0,55,56,3,8,4,0,56,57,3,10,5,
        0,57,75,1,0,0,0,58,59,3,8,4,0,59,60,5,1,0,0,60,61,3,8,4,0,61,62,
        5,12,0,0,62,63,5,2,0,0,63,64,3,10,5,0,64,75,1,0,0,0,65,66,5,1,0,
        0,66,67,3,8,4,0,67,68,5,12,0,0,68,69,5,2,0,0,69,70,5,11,0,0,70,75,
        1,0,0,0,71,72,3,8,4,0,72,73,5,12,0,0,73,75,1,0,0,0,74,51,1,0,0,0,
        74,58,1,0,0,0,74,65,1,0,0,0,74,71,1,0,0,0,75,7,1,0,0,0,76,92,5,10,
        0,0,77,78,5,1,0,0,78,79,3,2,1,0,79,80,5,2,0,0,80,92,1,0,0,0,81,82,
        5,1,0,0,82,83,3,6,3,0,83,84,5,2,0,0,84,92,1,0,0,0,85,86,5,1,0,0,
        86,87,5,11,0,0,87,88,3,8,4,0,88,89,3,10,5,0,89,90,5,2,0,0,90,92,
        1,0,0,0,91,76,1,0,0,0,91,77,1,0,0,0,91,81,1,0,0,0,91,85,1,0,0,0,
        92,9,1,0,0,0,93,94,7,0,0,0,94,11,1,0,0,0,5,30,41,49,74,91
    ]

class MathOperationsParser ( Parser ):

    grammarFileName = "MathOperations.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'%'", "'|'", "<INVALID>", "'MEM'", "'RES'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "MEM", "RES", 
                      "WS" ]

    RULE_expr = 0
    RULE_operationExpr = 1
    RULE_memExpr = 2
    RULE_resExpr = 3
    RULE_item = 4
    RULE_op = 5

    ruleNames =  [ "expr", "operationExpr", "memExpr", "resExpr", "item", 
                   "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    MEM=11
    RES=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operationExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.OperationExprContext,0)


        def memExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.MemExprContext,0)


        def resExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.ResExprContext,0)


        def MEM(self):
            return self.getToken(MathOperationsParser.MEM, 0)

        def item(self):
            return self.getTypedRuleContext(MathOperationsParser.ItemContext,0)


        def op(self):
            return self.getTypedRuleContext(MathOperationsParser.OpContext,0)


        def getRuleIndex(self):
            return MathOperationsParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MathOperationsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(MathOperationsParser.T__0)
                self.state = 13
                self.operationExpr()
                self.state = 14
                self.match(MathOperationsParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(MathOperationsParser.T__0)
                self.state = 17
                self.memExpr()
                self.state = 18
                self.match(MathOperationsParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(MathOperationsParser.T__0)
                self.state = 21
                self.resExpr()
                self.state = 22
                self.match(MathOperationsParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(MathOperationsParser.T__0)
                self.state = 25
                self.match(MathOperationsParser.MEM)
                self.state = 26
                self.item()
                self.state = 27
                self.op()
                self.state = 28
                self.match(MathOperationsParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathOperationsParser.ItemContext)
            else:
                return self.getTypedRuleContext(MathOperationsParser.ItemContext,i)


        def op(self):
            return self.getTypedRuleContext(MathOperationsParser.OpContext,0)


        def RES(self):
            return self.getToken(MathOperationsParser.RES, 0)

        def getRuleIndex(self):
            return MathOperationsParser.RULE_operationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationExpr" ):
                listener.enterOperationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationExpr" ):
                listener.exitOperationExpr(self)




    def operationExpr(self):

        localctx = MathOperationsParser.OperationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operationExpr)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.item()
                self.state = 33
                self.item()
                self.state = 34
                self.op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.item()
                self.state = 37
                self.match(MathOperationsParser.RES)
                self.state = 38
                self.item()
                self.state = 39
                self.op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(MathOperationsParser.ItemContext,0)


        def MEM(self):
            return self.getToken(MathOperationsParser.MEM, 0)

        def resExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.ResExprContext,0)


        def getRuleIndex(self):
            return MathOperationsParser.RULE_memExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemExpr" ):
                listener.enterMemExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemExpr" ):
                listener.exitMemExpr(self)




    def memExpr(self):

        localctx = MathOperationsParser.MemExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memExpr)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.item()
                self.state = 44
                self.match(MathOperationsParser.MEM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.resExpr()
                self.state = 47
                self.match(MathOperationsParser.MEM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathOperationsParser.ItemContext)
            else:
                return self.getTypedRuleContext(MathOperationsParser.ItemContext,i)


        def RES(self):
            return self.getToken(MathOperationsParser.RES, 0)

        def op(self):
            return self.getTypedRuleContext(MathOperationsParser.OpContext,0)


        def MEM(self):
            return self.getToken(MathOperationsParser.MEM, 0)

        def getRuleIndex(self):
            return MathOperationsParser.RULE_resExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResExpr" ):
                listener.enterResExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResExpr" ):
                listener.exitResExpr(self)




    def resExpr(self):

        localctx = MathOperationsParser.ResExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resExpr)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(MathOperationsParser.T__0)
                self.state = 52
                self.item()
                self.state = 53
                self.match(MathOperationsParser.RES)
                self.state = 54
                self.match(MathOperationsParser.T__1)
                self.state = 55
                self.item()
                self.state = 56
                self.op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.item()
                self.state = 59
                self.match(MathOperationsParser.T__0)
                self.state = 60
                self.item()
                self.state = 61
                self.match(MathOperationsParser.RES)
                self.state = 62
                self.match(MathOperationsParser.T__1)
                self.state = 63
                self.op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(MathOperationsParser.T__0)
                self.state = 66
                self.item()
                self.state = 67
                self.match(MathOperationsParser.RES)
                self.state = 68
                self.match(MathOperationsParser.T__1)
                self.state = 69
                self.match(MathOperationsParser.MEM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.item()
                self.state = 72
                self.match(MathOperationsParser.RES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MathOperationsParser.NUMBER, 0)

        def operationExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.OperationExprContext,0)


        def resExpr(self):
            return self.getTypedRuleContext(MathOperationsParser.ResExprContext,0)


        def MEM(self):
            return self.getToken(MathOperationsParser.MEM, 0)

        def item(self):
            return self.getTypedRuleContext(MathOperationsParser.ItemContext,0)


        def op(self):
            return self.getTypedRuleContext(MathOperationsParser.OpContext,0)


        def getRuleIndex(self):
            return MathOperationsParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = MathOperationsParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(MathOperationsParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(MathOperationsParser.T__0)
                self.state = 78
                self.operationExpr()
                self.state = 79
                self.match(MathOperationsParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(MathOperationsParser.T__0)
                self.state = 82
                self.resExpr()
                self.state = 83
                self.match(MathOperationsParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.match(MathOperationsParser.T__0)
                self.state = 86
                self.match(MathOperationsParser.MEM)
                self.state = 87
                self.item()
                self.state = 88
                self.op()
                self.state = 89
                self.match(MathOperationsParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathOperationsParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = MathOperationsParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





