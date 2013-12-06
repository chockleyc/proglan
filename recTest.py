import sys
import newRec

if len(sys.argv) == 0:
    print("No filename provided.  Program will now exit...")
    exit(0)

i = newRec.recognizer(sys.argv[1])
i.statementList()

