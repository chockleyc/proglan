import re

class lexeme:
    def __init__(self, aType = None, aData = None):
        self.type = aType
        self.data = aData
        self.stackString = ""
    def __print__(self):
        print(self.type + " " + self.data)

class lexer:
    def __init__(self, filename):
        self.f = open(file, 'r')
        self.ch = ''

    def pushBack(self):
        self.stackString = self.stackString + self.ch
        return

    def pop(self):
        temp = self.stackString[len(self.stackString)-1]
        self.stackString = self.stackString[:len(self.stackString)-2]
        return temp

    def skipWhiteSpace(self):
        while self.ch.isspace():
            self.ch = self.f.read(1)

    def lexNumber(self):
        myNum = ""
        if re.match("^[0-9]*$", self.ch):
            myNum = myNum + self.ch
        else:
            return lexeme("NUMBER", myNum)

    def lexVariable(self):
        myVar = ""
        if re.match("^[A-Za-z0-9_-]*$", self.ch):
            myVar = myVar + self.ch
        else:
            return lexeme("VARIABLE", myVar)

    def lexString(self):
        myString = ""
        self.ch = self.f.read(1)
        while self.ch != '\"':
            myString = myString + self.ch

        return lexeme("STRING", myString)

    def lex(self):
        self.skipWhiteSpace()

        self.ch = self.f.read(1)

        if len(self.ch) < 1:
            return lexeme("ENDofINPUT")

        elif self.ch == '(':
            return lexeme("OPAREN")

        elif self.ch == ')':
            return lexeme("CPAREN")

        elif self.ch == ',':
            return lexeme("COMMA")

        elif self.ch == '+':
            return lexeme("PLUS")

        elif self.ch == '*':
            return lexeme("TIMES")

        elif self.ch == '/':
            return lexeme("DIVIDES")

        elif self.ch == '<':
            return lexeme("LESSTHAN")

        elif self.ch == '>':
            return lexeme("GREATERTHAN")

        elif self.ch == '=':
            return lexeme("ASSIGN")

        elif self.ch == ';':
            return lexeme("SEMICOLON")

        else:
            if re.match("^[0-9]*$", self.ch):
                self.pushBack(self.ch)
                return self.lexNumber()

            elif re.match("^[A-Za-z]*$", self.ch):
                self.pushBack(self.ch)
                return self.lexVariable()

            elif self.ch == '\"':
                self.pushBack(self.ch)
                return self.lexString()

            else:
                return lexeme("UNKNOWN", self.ch)



