
class environment:
    def __init__(self):
        self.dic = dict()

    def lookup(self, variable, env):
        if variable in self.dic:
            return self.dic[variable]
        else:
            print ("variable " + variable + " is undefined")
            return None

    def insert(self, variable, value, env):
        self.dic[variable] = value
        return value
