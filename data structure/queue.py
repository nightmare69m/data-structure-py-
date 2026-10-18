class stack :
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]

    def add(self,item):
        self.items.append(item)

    def remove(self,item):
        assert item in self.items,f"{item} is not in the stack"
        idx=self.items.index(item)
        return self.items.pop(idx)
    def peek(self,item):   
        return self.items[len(self.items)-1]
    # def peek1(self,item):
    #     return self.items.peek(item)
    def size(self):
        return len(self.items)


s=stack()
s.add(11)
s.add(13)
s.add(14)
s.remove(13)
print(s.peek(12))
print(s.size())
print(s.isempty())
