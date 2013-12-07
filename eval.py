
class evaluator:
    def __init__(self):
        return

    def eval(self, tree, env):
        if tree.datatype == "NUMBER":
            return tree
        elif tree.datatype == "STRING":
            return tree
        elif tree.datatype == "VARIABLE":
            return env.lookup(tree, env)
        elif tree.datatype == "PLUS":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "MINUS":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "TIMES":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "DIVIDES":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "LESSTHAN":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "GREATERTHAN":
            return self.evalSimpleOp(tree, env)
        elif tree.datatype == "ASSIGN":
            return self.evalAssign(tree, env)
        elif tree.datatype == "VARDEF":
            return self.evalVarDef(tree, env)
        elif tree.datatype == "FUNCDEF":
            return self.evalFuncDef(tree, env)
        elif tree.datatype == "IFSTATEMENT":
            return self.evalIf(tree, env)
        elif tree.datatype == "WHILESTATEMENT":
            return self.evalWhile(tree, env)
        elif tree.datatype == "FUNCTIONCALL":
            return self.evalFuncCall(tree, env)
        elif tree.datatype == "BLOCK":
            return self.evalBlock(tree, env)

    def evalSimpleOp(self, tree, env):

