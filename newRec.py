import lex

class recognizer:
    def __init__(self, filename):
        self.i = lex.lexer(filename)
        self.current = self.i.lex()

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
            print("Syntax error at " + self.current.datatype)
            exit(0)
        return self.current

    def statementList(self):
        self.statement()
        if self.statementPending():
            self.statementList()

    def statementPending(self):
        return self.declarationPending() or self.conditionalPending() or self.expressionPending()

    def statement(self):
        if self.declarationPending():
            self.declaration()
        elif self.conditionalPending():
            self.conditional()
        elif self.expressionPending():
            self.expression()
            self.match("SEMI")

    def declarationPending(self):
        return self.check("FUNCTION") or self.check("VAR")

    def declaration(self):
        if self.check("FUNCTION"):
            self.match("FUNCTION")
            self.match("VARIABLE")
            self.match("OPAREN")
            self.optArgList()
            self.match("CPAREN")
            self.functionBody()
        elif self.check("VAR"):
            self.match("VAR")
            self.match("VARIABLE")
            self.optInit()
            self.match("SEMI")

    def functionBody(self):
        self.match("OBRACE")
        self.optStatementList()
        self.returnStatement()
        self.match("CBRACE")

    def returnStatement(self):
        self.match("RETURN")
        self.statement()

    def conditionalPending(self):
        return self.ifStatementPending() or self.whileStatementPending()

    def conditional(self):
        if self.ifStatementPending():
            self.ifStatement()
        elif self.whileStatementPending():
            self.whileStatement()
            
    def expressionPending(self):
        return self.primaryPending()

    def expression(self):
        self.primary()
        if self.operatorPending():
            self.operator()
            self.expression()

    def block(self):
        self.match("OBRACE")
        self.optStatementList()
        self.match("CBRACE")

    def optInit(self):
        if self.check("ASSIGN"):
            self.match("ASSIGN")
            self.expression()

    def ifStatementPending(self):
        return self.check("IF")

    def whileStatementPending(self):
        return self.check("WHILE")

    def ifStatement(self):
        self.match("IF")
        self.match("OPAREN")
        self.expression()
        self.match("CPAREN")
        self.block()
        self.optElse()

    def whileStatement(self):
        self.match("WHILE")
        self.match("OPAREN")
        self.expression()
        self.match("CPAREN")
        self.block()

    def primaryPending(self):
        return self.functionCallPending() or self.check("STRING") or self.numericPending()

    def primary(self):
        if self.check("STRING"):
            self.match("STRING")
        elif self.check("INTEGER"):
            self.match("INTEGER")
        elif self.check("VARIABLE"):
            self.variableFuncCall()

    def variableFuncCall(self):
        self.match("VARIABLE")
        if self.check("OPAREN"):
            self.match("OPAREN")
            self.optArgList()
            self.match("CPAREN")

    def operatorPending(self):
        return self.check("PLUS") or self.check("MINUS") or self.check("TIMES") or self.check("DIVIDES") or self.check("LESSTHAN") or self.check("GREATERTHAN") or self.check("ASSIGN")

    def operator(self):
        if self.check("PLUS"):
            self.match("PLUS")
        elif self.check("MINUS"):
            self.match("MINUS")
        elif self.check("TIMES"):
            self.match("TIMES")
        elif self.check("DIVIDES"):
            self.match("DIVIDES")
        elif self.check("LESSTHAN"):
            self.match("LESSTHAN")
        elif self.check("GREATERTHAN"):
            self.match("GREATERTHAN")
        elif self.check("ASSIGN"):
            self.match("ASSIGN")

    def optStatementList(self):
        if self.statementPending():
            self.statementList()

    def optElse(self):
        if self.check("ELSE"):
            self.match("ELSE")
            self.block()

    def numericPending(self):
        return self.check("INTEGER") or self.check("VARIABLE")

    def functionCallPending(self):
        return self.check("VARIABLE")

    def functionCall(self):
        self.match("VARIABLE")
        self.match("OPAREN")
        self.optArgList()
        self.match("CPAREN")
        self.match("SEMI")

    def numeric(self):
        if self.check("INTEGER"):
            self.match("INTEGER")
        elif self.check("VARIABLE"):
            self.match("VARIABLE")

    def optArgList(self):
        self.expression()
        if self.check("COMMA"):
            self.match("COMMA")
            self.optArgList()


















