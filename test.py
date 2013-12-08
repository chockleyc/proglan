import sys
import pt
import env
import eval

def preorder(tree):
    if tree == None:
        return None
    print(tree.datatype)
    preorder(tree.left)
    preorder(tree.right)

if len(sys.argv) == 0:
    print("No filename provided.  Program will now exit...")
    exit(0)

i = pt.recognizer(sys.argv[1])
e = eval.evaluator()

#preorder(i.start())
e.Eval(i.start(), env.create())

