import lex

class environment:


    def cons(self, datatype, left, right):
        return lex.lexeme(datatype, left, right)

    def car(self, node):
        return node.left

    def cdr(self, node):
        return node.right

    def cadr(self, node):
        return self.car(self.cdr(node))

    def sameVariable(self, one, two):
        if one.data == two.data:
            return True
        else:
            return False

    def setCar(self, node, newVal):
        node.left = newVal

    def create(self):
        return self.cons("ENV", None, self.cons("VALUES", None, None))

    def lookup(self, variable, env):
        while (env != None):
            variables = self.car(env)
            vals = self.cadr(env)
            while (self.cars != None):
                if self.sameVariable(variable, self.car(variables)):
                    return self.car(vals)
                variables = self.cdr(variables)
                vals = self.cdr(vals)
            env = self.cdr(self.cdr(env))
        print("variable ", variable, " is undefined")
        return None

    def update(self, variable, newVal, env):
        while (env != None):
            variables =  self.car(env)
            vals = self.cadr(env)
            while (self.cars != None):
                if self.sameVariable(variable, self.car(variables)):
                    self.setCar(vals, newVal)
                    return None
                variables = self.cdr(variables)
                vals = self.cdr(vals)
            env = self.cdr(self.cdr(env))
        self.insert(variable, newVal, env)

    def insert(self, variable, value, env):
        self.setCar(env, self.cons("JOIN". variable, self.car(env)))
        self.setCar(self.cdr(env), self.cons("JOIN", value, self.cadr(env)))
        return value

    def extend(self, variables, values, env):
        return self.cons("ENV", variables, self.cons("ENV", values, env))










