class Directory:
    def __init__(self, parent=None, children=None, name=""):
        self.name = name
        if children == None:
            self.children = []
        else:
            self.children = children
        self.parent = parent
    
    def get_size(self):
        sum = 0
        for child in self.children:
            sum += child.get_size()
        return sum
        
    def first_half_solver(self, limit, values):
        if self.get_size() <= limit:
            values.append(self.get_size())
        for child in self.children:
            if type(child) == type(self):
                child.first_half_solver(limit, values)
                
    def second_half_solver(self, limit, values):
        if self.get_size() >= limit:
            values.append((self, self.get_size()))
        for child in self.children:
            if type(child) == type(self):
                child.second_half_solver(limit, values)
        
    def add_child(self, item):
        if item not in self.children:
            self.children.append(item)
            item.parent = self
    
    def print_tree(self, level):
        print("  "*level,"-"+self.name)
        for child in self.children:
            child.print_tree(level+1)
            
    def find(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
        
class File:
    def __init__(self, parent=None, size=0, name=""):
        self.name = name
        self.parent = parent
        self.size = size
    
    def get_size(self):
        return self.size
        
    def print_tree(self, level):
        print("  "*level,"-"+self.name + "("+str(self.size)+")")

def get_file_or_dir(line):
    if line[0:3] == "dir":
        return Directory(name=line[4:].strip())
    else:
        items = line.split(" ")
        return File(size=int(items[0]), name=items[1].strip())
        
def init_directory():
    root = Directory(name="/")
    current = root
    with open('RyanProb7Input.txt') as file:
        lines = [l.strip() for l in file]
        for line in lines[1:]:
            parsed = line.split(" ")
            if parsed[0] == "$":
                if parsed[1] == 'cd':
                    if parsed[2] == "..":
                        current = current.parent
                    else:
                        current = current.find(parsed[2])
            elif current.find(parsed[1]) == None:
                if parsed[0] == "dir":
                    current.add_child(Directory(name=parsed[1]))
                else:
                    current.add_child(File(size=int(parsed[0]), name=parsed[1]))
    return root

def first_half():
    root = init_directory()
    values = []
    root.first_half_solver(100000, values)
    sum = 0
    for value in values:
        sum += value
    print("part 1:",sum)

def second_half():
    root = init_directory()
    values = []
    unused_space = 70000000 - root.get_size()
    delete_req = 30000000 - unused_space
    root.second_half_solver(delete_req, values)
    print("part 2:",sorted(values, key=lambda x: x[1])[0][1])
    
first_half()
second_half()
