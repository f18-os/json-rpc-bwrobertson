class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def convert(graph):
    #x =  '{ "name":"John", "age":30, "city":"New York"}'
    x = {}
    tempName = graph.name
    tempVal = graph.val
    x[graph.name] = {
        "name": tempName, 
        "value" : tempVal
        }   
    for c in graph.children:
        tempName = c.name
        tempVal = c.val
        x[c.name] = {
            "name": tempName, 
            "value" : tempVal
        }  
    return x
