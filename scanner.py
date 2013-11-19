import sys
import lex

if len(sys.argv) == 0:
    print("No filename provided.  Program will now exit...")
    exit(0)

i = lex.lexer(sys.argv[1])

token = i.lex()
while token.datatype != "ENDofINPUT":
    print(token)
    token = i.lex()
print(token)
