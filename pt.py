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
            temp = self.current
            self.advance()
            return temp
        else:
            print("Syntax error at " + self.current.datatype)
            exit(0)
        return self.current

    def start(self):
        return self.statementList()

    def statementList(self):
        tree = lex.lexeme("STATEMENTLIST")
        tree.left = self.statement()
        if self.statementPending():
            tree.right = self.statementList()
        return tree

    def statementPending(self):
        return self.declarationPending() or self.conditionalPending() or self.expressionPending()

    def statement(self):
        tree = lex.lexeme("STATEMENT")
        if self.declarationPending():
            tree.left = self.declaration()
        elif self.conditionalPending():
            tree.left = self.conditional()
        elif self.expressionPending():
            tree.left = self.expression()
            tree.right = self.match("SEMI")
        return tree

    def declarationPending(self):
        return self.check("FUNCTION") or self.check("VAR")

    def declaration(self):
        tree = lex.lexeme("DECLARATION")
        if self.check("FUNCTION"):
            tree.left = self.match("FUNCTION")
            tree.right = self.match("VARIABLE")
            self.match("OPAREN")
            tree.left.left = self.optArgList()
            self.match("CPAREN")
            tree.left.right = self.functionBody()
        elif self.check("VAR"):
            tree.left = self.match("VAR")
            tree.left.left = self.match("VARIABLE")
            tree.left.right = self.optInit()
            tree.right = self.match("SEMI")
        return tree

    def functionBody(self):
        tree = lex.lexeme("FUNCTIONBODY")
        self.match("OBRACE")
        tree.left = self.optStatementList()
        tree.right = self.returnStatement()
        self.match("CBRACE")
        return tree

    def returnStatement(self):
        tree = lex.lexeme("RETURNSTATEMENT")
        tree.left = self.match("RETURN")
        tree.right = self.statement()
        return tree

    def conditionalPending(self):
        return self.ifStatementPending() or self.whileStatementPending()

    def conditional(self):
        tree = lex.lexeme("CONDITIONAL")
        if self.ifStatementPending():
            tree.left = self.ifStatement()
        elif self.whileStatementPending():
            tree.left = self.whileStatement()
        return tree
            
    def expressionPending(self):
        return self.primaryPending()

    def expression(self):
        tree = lex.lexeme("EXPRESSION")
        tree.left = self.primary()
        if self.operatorPending():
            tree.right = lex.lexeme("GLUE")
            tree.right.left = self.operator()
            tree.right.right = self.expression()
        return tree

    def block(self):
        tree = lex.lexeme("BLOCK")
        self.match("OBRACE")
        tree.left = self.optStatementList()
        self.match("CBRACE")
        return tree

    def optInit(self):
        tree = lex.lexeme("OPTINIT")
        if self.check("ASSIGN"):
            tree.left = self.match("ASSIGN")
            tree.right = self.expression()
        return tree

    def ifStatementPending(self):
        return self.check("IF")

    def whileStatementPending(self):
        return self.check("WHILE")

    def ifStatement(self):
        tree = lex.lexeme("IFSTATEMENT")
        self.match("IF")
        self.match("OPAREN")
        tree.left = self.expression()
        self.match("CPAREN")
        tree.right = lex.lexeme("GLUE")
        tree.right.left = self.block()
        tree.right.right = self.optElse()
        return tree

    def whileStatement(self):
        tree = lex.lexeme("WHILESTATEMENT")
        self.match("WHILE")
        self.match("OPAREN")
        tree.left = self.expression()
        self.match("CPAREN")
        tree.right = self.block()
        return tree

    def primaryPending(self):
        return self.functionCallPending() or self.check("STRING") or self.numericPending()

    def primary(self):
        tree = lex.lexeme("PRIMARY")
        if self.check("STRING"):
            tree.left = self.match("STRING")
        elif self.check("INTEGER"):
            tree.left = self.match("INTEGER")
        elif self.check("VARIABLE"):
            tree.left = self.variableFuncCall()
        return tree

    def variableFuncCall(self):
        tree = lex.lexeme("VARIABLEFUNCCALL")
        tree.left = self.match("VARIABLE")
        if self.check("OPAREN"):
            self.match("OPAREN")
            tree.right = self.optArgList()
            self.match("CPAREN")
        else:
            tree.datatype = "VARIABLE"
        return tree

    def operatorPending(self):
        return self.check("PLUS") or self.check("MINUS") or self.check("TIMES") or self.check("DIVIDES") or self.check("LESSTHAN") or self.check("GREATERTHAN") or self.check("ASSIGN")

    def operator(self):
        tree = lex.lexeme("OPERATOR")
        if self.check("PLUS"):
            tree.left = self.match("PLUS")
        elif self.check("MINUS"):
            tree.left = self.match("MINUS")
        elif self.check("TIMES"):
            tree.left = self.match("TIMES")
        elif self.check("DIVIDES"):
            tree.left = self.match("DIVIDES")
        elif self.check("LESSTHAN"):
            tree.left = self.match("LESSTHAN")
        elif self.check("GREATERTHAN"):
            tree.left = self.match("GREATERTHAN")
        elif self.check("ASSIGN"):
            tree.left = self.match("ASSIGN")
        return tree

    def optStatementList(self):
        tree = lex.lexeme("OPTSTATEMENTLIST")
        if self.statementPending():
            tree.left = self.statementList()
        return tree

    def optElse(self):
        tree = lex.lexeme("OPTELSE")
        if self.check("ELSE"):
            self.match("ELSE")
            tree.left = self.block()
        return tree

    def numericPending(self):
        return self.check("INTEGER") or self.check("VARIABLE")

    def functionCallPending(self):
        return self.check("VARIABLE")

    def functionCall(self):
        tree = lex.lexeme("FUNCTIONCALL")
        tree.left = lex.lexeme("GLUE")
        tree.left.left = self.match("VARIABLE")
        self.match("OPAREN")
        tree.left.right = self.optArgList()
        self.match("CPAREN")
        tree.right = self.match("SEMI")
        return tree

    def numeric(self):
        tree = lex.lexeme("NUMERIC")
        if self.check("INTEGER"):
            tree.left = self.match("INTEGER")
        elif self.check("VARIABLE"):
            tree.left = self.match("VARIABLE")
        return tree

    def optArgList(self):
        tree = lex.lexeme("OPTARGLIST")
        if self.expressionPending():
            tree.left = self.ArgList()
        return tree

    def ArgList(self):
        tree = lex.lexeme("ARGLIST")
        tree.left = self.expression()
        if self.check("COMMA"):
            self.match("COMMA")
            tree.right = self.ArgList()
        return tree

