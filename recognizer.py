import sys
import lex

class recognizer:
    def __init__(self):
        self.i = lex.lexer(sys.argv[2])
        self.current = self.i.lex()
        self.statementList()

    def advance(self):
        self.current = self.i.lex()

    def check(self, myType):
        if self.current.datatype == myType:
            return True
        else:
            return False

    def match(self, myType):
        if self.current.datatype == myType:
            self.advance()
        else:
            print("Syntax error at " + self.current)
            exit(0)
        return

    def expression(self):
        self.primary()
        if self.opPending():
            self.operator();
            self.expression();

    def opPending(self):
        return self.check("PLUS") or self.check("TIMES")

    def primary(self):
        if self.check("NUMBER"):
            self.match("NUMBER")

        elif self.check("VARIABLE"):
            self.match("VARIABLE")
            if self.check("OPAREN"):
                self.match("OPAREN")
                self.optExpressionList()
                self.match("CPAREN")

        else:
            self.match("OPAREN")
            self.expression()
            self.match("CPAREN")

    def ifStatement(self):
        self.match("IF")
        self.match("OPAREN")
        self.expression()
        self.match("CPAREN")
        self.block()
        self.optElse()

    def block(self):
        self.match("OBRACE")
        self.statementList()
        self.match("CBRACE")

    def statementList(self):
        self.statement()
        if self.statementPending():
            self.statementList()

    def statement(self):
        if self.expressionPending():
            self.expression()
        elif self.ifStatementPending():
            self.ifStatement()
        elif self.whileStatementPending():
            self.whileStatement()
        else:
            self.match("TYPE_INT")
            self.match("VARIABLE")
            self.optInit()
            self.match("SEMICOLON")

    def optElse(self):
        if self.check("ELSE"):
            self.match("ELSE")
            self.block()

    def optInit(self):
        if self.check("ASSIGN"):
            self.match("ASIGN")
            self.expression()

    def whileStatement(self):
        self.match("WHILE")
        self.match("OPAREN")
        self.expression()
        self.match("CPAREN")
        self.block()



