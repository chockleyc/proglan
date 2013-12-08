import lex

def cons(datatype, left, right):
    return lex.lexeme(datatype, "", left, right)

def car(node):
    return node.left

def cdr(node):
    return node.right

def cadr(node):
    return car(cdr(node))

def sameVariable(one, two):
    if one == two.data:
        return True
    else:
        return False

def setCar(node, newVal):
    node.left = newVal

def create():
    return cons("ENV", None, cons("VALUES", None, None))

def lookup(variable, env):
    while (env != None):
        variables = car(env)
        vals = cadr(env)
        while (variables != None):
            if sameVariable(variable, car(variables)):
                return car(vals)
            variables = cdr(variables)
            vals = cdr(vals)
        env = cdr(cdr(env))
    print("variable ", variable, " is undefined")
    return None

def update(variable, newVal, env):
    while (env != None):
        variables =  car(env)
        vals = cadr(env)
        while (variables != None):
            if sameVariable(variable, car(variables)):
                setCar(vals, newVal)
                return None
            variables = cdr(variables)
            vals = cdr(vals)
        env = cdr(cdr(env))
    insert(variable, newVal, env)

def insert(variable, value, env):
    setCar(env, cons("JOIN", variable, car(env)))
    setCar(cdr(env), cons("JOIN", value, cadr(env)))
    return value

def extend(variables, values, env):
    return cons("ENV", variables, cons("ENV", values, env))

def preorder(tree):
    if tree == None:
        return None
    print(tree.datatype)
    preorder(tree.left)
    preorder(tree.right)









