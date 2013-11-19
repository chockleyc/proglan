import re

class lexeme:
    def __init__(self, aType = None, aData = ""):
        self.datatype = aType
        self.data = aData
    def __str__(self):
        return self.datatype + " " + self.data

class lexer:
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.ch = ""
        self.stackString = ""

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
        while re.match("^[0-9]*$", self.ch):
            myNum = myNum + self.ch
            last_pos = self.f.tell()
            self.ch = self.f.read(1)
        self.f.seek(last_pos)
        return lexeme("INTEGER", myNum)

    def checkForKeyword(self, inputVar):
        if inputVar == "int":
            return lexeme("TYPE_INT")

        elif inputVar == "while":
            return lexeme("WHILE")

        elif inputVar == "for":
            return lexeme("FOR")

        elif inputVar == "return":
            return lexeme("RETURN")

        elif inputVar == "if":
            return lexeme("IF")

        elif inputVar == "else":
            return lexeme("ELSE")

        else:
            return lexeme("VARIABLE", inputVar)

    def lexVariable(self):
        myVar = ""
        while re.match("^[A-Za-z0-9_-]*$", self.ch):
            myVar = myVar + self.ch
            last_pos = self.f.tell()
            self.ch = self.f.read(1)
        self.f.seek(last_pos)
        return self.checkForKeyword(myVar)

    def lexString(self):
        myString = "\""
        self.ch = self.f.read(1)
        while self.ch != '\"':
            myString = myString + self.ch
            self.ch = self.f.read(1)
        return lexeme("STRING", myString + "\"")

    def lex(self):
        self.ch = self.f.read(1)
        self.skipWhiteSpace()

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

        elif self.ch == '-':
            return lexeme("MINUS")

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

        elif self.ch == '.':
            return lexeme("DOT")

        elif self.ch == '{':
            return lexeme("OBRACE")

        elif self.ch == '}':
            return lexeme("CBRACE")

        else:
            if re.match("^[0-9]*$", self.ch):
                self.pushBack()
                return self.lexNumber()

            elif re.match("^[A-Za-z]*$", self.ch):
                self.pushBack()
                return self.lexVariable()

            elif self.ch == '\"':
                self.pushBack()
                return self.lexString()

            else:
                return lexeme("UNKNOWN", self.ch)



