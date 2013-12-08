import env

class evaluator:
    def __init__(self):
        return

    def Eval(self, tree, envi):
        print(tree.datatype)
        if tree.datatype == "STATEMENTLIST":
            return self.evalStatementList(tree, envi)
        elif tree.datatype == "STATEMENT":
            return self.evalStatement(tree, envi)
        elif tree.datatype == "DECLARATION":
            return self.evalDeclaration(tree, envi)
        elif tree.datatype == "FUNCTIONBODY":
            return self.evalFunctionBody(tree, envi)
        elif tree.datatype == "RETURNSTATEMENT":
            return self.evalReturnStatement(tree, envi)
        elif tree.datatype == "CONDITIONAL":
            return self.evalConditional(tree, envi)
        elif tree.datatype == "EXPRESSION":
            return self.evalExpression(tree, envi)
        elif tree.datatype == "BLOCK":
            return self.evalBlock(tree, envi)
        elif tree.datatype == "OPTINIT":
            return self.evalOptInit(tree, envi)
        elif tree.datatype == "IFSTATEMENT":
            return self.evalIfStatement(tree, envi)
        elif tree.datatype == "WHILESTATEMENT":
            return self.evalWhileStatement(tree, envi)
        elif tree.datatype == "PRIMARY":
            return self.evalPrimary(tree, envi)
        elif tree.datatype == "VARIABLEFUNCCALL:":
            return self.evalVariableFuncCall(tree, envi)
        elif tree.datatype == "OPERATOR":
            return self.evalOperator(tree, envi)
        elif tree.datatype == "OPTSTATEMENTLIST":
            return self.evalOptStatementList(tree, envi)
        elif tree.datatype == "OPTELSE":
            return self.evalOptElse(tree, envi)
        elif tree.datatype == "FUNCTIONCALL":
            return self.evalFunctionCall(tree, envi)
        elif tree.datatype == "NUMERIC":
            return self.evalNumeric(tree, envi)
        elif tree.datatype == "OPTARGLIST":
            return self.evalOptArgList(tree, envi)
        elif tree.datatype == "ARGLIST":
            return self.evalArgList(tree, envi)

    def evalStatementList(self, tree, envi):
        if tree.right != None:
            self.Eval(tree.left, envi)
            return self.Eval(tree.right, envi)
        else:
            return self.Eval(tree.left, envi)

    def evalStatement(self, tree, envi):
        return self.Eval(tree.left, envi)

    def evalDeclaration(self, tree, envi):
        if tree.left.datatype == "FUNCTION":
            closure = env.cons("CLOSURE", envi, env.cons("JOIN", tree.left.left, env.cons("JOIN", tree.left.right, None)))
            envi.Insert(tree.right, closure, envi) 
        elif tree.right.datatype == "VAR":
            env.Insert(tree.left.left, tree.left.right, envi)

    def evalFunctionBody(self, tree, envi):
        self.Eval(tree.left, envi)
        return self.Eval(tree.right, envi)

    def evalReturnStatement(self, tree, envi):
        return self.Eval(tree.right, envi)

    def evalConditional(self, tree, envi):
        return self.Eval(tree.left, envi)

    def evalExpression(self, tree, envi):
        if tree.right.datatype == "GLUE":
            return evalOperation(tree.left, tree.right.left, tree.right.right, envi)
        else:
            return eval(tree.left, envi)

    def evalBlock(self, tree, envi):
        return eval(tree.left)

    def evalOptInit(self, tree, envi):
        if tree.left != None:
            return eval(tree.right)
        else: 
            return

    def evalIfStatement(self, tree, envi):
        if self.evalBool(tree.left, envi):
            return self.Eval(tree.right.left, envi)
        else:
            return self.Eval(tree.right.right, envi)

    def evalWhileStatement(self, tree, envi):
        result = None
        while self.evalBool(tree.left, envi):
            result = self.Eval(tree.right, envi)
        return result

    def evalPrimary(self, tree, envi):
        if tree.left.datatype == "VARIABLEFUNCCALL":
            return self.Eval(tree.left)
        else:
            return tree.left

    def evalVariableFuncCall(self, tree, envi):
        print("NOT IMPLEMENTED YET")

    def evalOperator(self, tree, envi):
        return tree.left

    def evalOptStatementList(self, tree, envi):
        if tree.left == None:
            return tree
        else:
            return self.Eval(tree.left)

    def evalOptElse(self, tree, envi):
        if tree.left == None:
            return tree
        else:
            return self.Eval(tree.left)

    def evalFunctionCall(self, tree, envi):
        print("NOT IMPLEMENTED YET")

    def evalNumeric(self, tree, envi):
        self.Eval(tree.left, envi)

    def evalOptArgList(self, tree, envi):
        self.Eval(tree.left, envi)

    def evalArgList(self, tree, envi):
        if tree.right != None:
            self.Eval(tree.left, envi)
            return self.Eval(tree.right, envi)
        else:
            return self.Eval(tree.left, envi)

    def evalBool(self, tree, envi):
        if tree.right.left.left.datatype == "GREATERTHAN":
            if self.Eval(tree.left, envi) > self.Eval(tree.right.right, envi):
                return True
            else:
                return False
        elif tree.right.left.left.datatype == "LESSTHAN":
            if self.Eval(tree.left, envi) < self.Eval(tree.right.right, envi):
                return True
            else:
                return False
