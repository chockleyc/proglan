
class evaluator:
    def __init__(self):
        return

    def eval(self, tree, env):
        if tree.datatype == "STATEMENTLIST":
            return self.evalStatementList(tree, env)
        elif tree.datatype == "STATEMENT":
            return self.evalStatement(tree, env)
        elif tree.datatype == "DECLARATION":
            return self.evalDeclaration(tree, env)
        elif tree.datatype == "FUNCTIONBODY":
            return self.evalFunctionBody(tree, env)
        elif tree.datatype == "RETURNSTATEMENT":
            return self.evalReturnStatement(tree, env)
        elif tree.datatype == "CONDITIONAL":
            return self.evalConditional(tree, env)
        elif tree.datatype == "EXPRESSION":
            return self.evalExpression(tree, env)
        elif tree.datatype == "BLOCK":
            return self.evalBlock(tree, env)
        elif tree.datatype == "OPTINIT":
            return self.evalOptInit(tree, env)
        elif tree.datatype == "IFSTATEMENT":
            return self.evalIfStatement(tree, env)
        elif tree.datatype == "WHILESTATEMENT":
            return self.evalWhileStatement(tree, env)
        elif tree.datatype == "PRIMARY":
            return self.evalPrimary(tree, env)
        elif tree.datatype == "VARIABLEFUNCCALL:":
            return self.evalVariableFuncCall(tree, env)
        elif tree.datatype == "OPERATOR":
            return self.evalOperator(tree, env)
        elif tree.datatype == "OPTSTATEMENTLIST":
            return self.evalOptStatementList(tree, env)
        elif tree.datatype == "OPTELSE":
            return self.evalOptElse(tree, env)
        elif tree.datatype == "FUNCTIONCALL":
            return self.evalFunctionCall(tree, env)
        elif tree.datatype == "NUMERIC":
            return self.evalNumeric(tree, env)
        elif tree.datatype == "OPTARGLIST":
            return self.evalOptArgList(tree, env)
        elif tree.datatype == "ARGLIST":
            return self.evalArgList(tree, env)

    def evalStatementList(self, tree, env):
        if tree.right != None:
            self.evalStatement(tree.left, env)
            return self.evalStatementList(tree.right, env)
        else:
            return self.evalStatement(tree.left, env)

    def evalStatement(self, tree, env):
        return eval(tree.left, env)

    def evalDeclaration(self, tree, env):
        if tree.left.datatype == "FUNCTION":
            env.Insert(tree.right, tree.left)
        elif tree.right.datatype == "VAR":
            env.Insert(tree.left.left, tree.left.right, env)

    def evalFunctionBody(self, tree, env):
        self.eval(tree.left, env)
        return eval(tree.right, env)



