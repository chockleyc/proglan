class lexer:
    def __init__(self, filename):
        self.f = open(file, 'r')
        self.ch = ''

    class lexeme:
        def __init__(self, aType = None, aData = None):
            self.type = aType
            self.data = aData

    def lex():
        skipWhiteSpace()

        self.ch = f.read(1)

        if len(self.ch) < 1:
            return lexeme(ENDofINPUT)

        elif self.ch == '(':
            return lexeme(OPAREN)

        elif self.ch == ')':
            return lexeme(CPAREN)

        elif self.ch == ',':
            return lexeme(COMMA)

        elif self.ch == '+':
            return lexeme(PLUS)

        elif self.ch == '*':
            return lexeme(TIMES)

        elif self.ch == '/':
            return lexeme(DIVIDES)

        elif self.ch == '<':
            return lexeme(LESSTHAN)

        elif self.ch == '>':
            return lexeme(GREATERTHAN)

        elif self.ch == '=':
            return lexeme(ASSIGN)

        elif self.ch == ';':
            return lexeme(SEMICOLON)

        else:
            if isDigit(self.ch):
                pushBack(self.ch)
                return lexNumber()

            elif isLetter(self.ch):
                pushBack(self.ch)
                return lexVariable()

            elif self.ch == '\"':
                pushBack(self.ch)
                return lexString()

            else:
                return lexeme(UNKNOWN, self.ch)

    def skipWhiteSpace():
        while self.ch.isspace():
            self.ch = f.read(1)

    def lexNumber():

    def lexVariable():

    def lexString():
