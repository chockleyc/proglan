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
  
    if len(ch) < 1:
      return lexeme(ENDofINPUT)
  
    if ch == '(':
      return lexeme(OPAREN) 
  
    elif ch == ')':
      return lexeme(CPAREN) 
  
    elif ch == ',':
      return lexeme(COMMA) 
  
    elif ch == '+':
      return lexeme(PLUS) 
  
    elif ch == '*':
      return lexeme(TIMES) 
  
    elif ch == '/':
      return lexeme(DIVIDES) 
  
    elif ch == '<':
      return lexeme(LESSTHAN) 
  
    elif ch == '>':
      return lexeme(GREATERTHAN) 
  
    elif ch == '=':
      return lexeme(ASSIGN) 
  
    elif ch == ';':
      return lexeme(SEMICOLON) 
  
    else:
      if isDigit(ch):
        pushBack(ch)
        return lexNumber()
  
      elif isLetter(ch):
        pushBack(ch)
        return lexVariable()
  
      elif ch == '\"':
        pushBack(ch)
        return lexString()
  
      else:
        return lexeme(UNKNOWN, ch)
  
  def skipWhiteSpace():
    while self.ch.isspace():
      self.ch = f.read(1)
  
  
  def lexNumber():
  
  
  def lexVaribale():

  
  def lexString():
