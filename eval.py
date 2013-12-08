import env
import lex

class evaluator:
    def __init__(self):
        return

    def Eval(self, tree, envi):
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
            envi.insert(tree.right, closure, envi) 
        elif tree.left.datatype == "VAR":
            init = self.evalOptInit(tree.left.right, envi)
            if init == None:
                env.insert(tree.left.left, lex.lexeme("INTEGER", 0), envi)
            else:
                env.insert(tree.left.left, init, envi)

    def evalFunctionBody(self, tree, envi):
        self.Eval(tree.left, envi)
        return self.Eval(tree.right, envi)

    def evalReturnStatement(self, tree, envi):
        return self.Eval(tree.right, envi)

    def evalConditional(self, tree, envi):
        return self.Eval(tree.left, envi)

    def evalExpression(self, tree, envi):
        if tree.right != None:
            return self.evalOperation(tree.left, tree.right.left, tree.right.right, envi)
        else:
            return self.Eval(tree.left, envi)

    def evalBlock(self, tree, envi):
        return self.Eval(tree.left, envi)

    def evalOptInit(self, tree, envi):
        if tree.left != None:
            return self.Eval(tree.right, envi)
        else: 
            return None

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
            return self.Eval(tree.left, envi)
        elif tree.left.datatype == "VARIABLE":
            return self.evalVariable(tree.left.left, envi)
        else:
            return tree.left

    def evalVariable(self, tree, envi):
        temp =  env.lookup(tree.data, envi)
        return temp

    def evalVariableFuncCall(self, tree, envi):
        print("NOT IMPLEMENTED YET")

    def evalOperator(self, tree, envi):
        return tree.left

    def evalOptStatementList(self, tree, envi):
        if tree.left == None:
            return tree
        else:
            return self.Eval(tree.left, envi)

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
            if self.Eval(tree.left, envi).data > self.Eval(tree.right.right, envi).data:
                return True
            else:
                return False
        elif tree.right.left.left.datatype == "LESSTHAN":
            if self.Eval(tree.left, envi) < self.Eval(tree.right.right, envi):
                return True
            else:
                return False

    def evalOperation(self, lhs, op, rhs, envi):
        if op.left.datatype == "PLUS":
            return self.Eval(lhs, envi).data + self.Eval(rhs, envi).data
        elif op.left.datatype == "MINUS":
            return self.Eval(lhs, envi).data - self.Eval(rhs, envi).data
        elif op.left.datatype == "TIMES":
            return self.Eval(lhs, envi).data * self.Eval(rhs, envi).data
        elif op.left.datatype == "DIVIDES":
            return self.Eval(lhs, envi).data / self.Eval(rhs, envi).data
        elif op.left.datatype == "ASSIGN":
            env.update(self.Eval(lhs, envi), self.Eval(rhs, envi), envi)
