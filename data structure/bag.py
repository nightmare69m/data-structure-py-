class bag:
    def __init__(self):
        self.__items = []
    def add(self, item):
        self.__items.append(item)
    def delete_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("this item does not exist in bag")
    def delete_index (self,index):
        self.__items.pop(index)
    def size(self):
        return len(self.__items)
    
    def contains(self,item):
        return item in self.__items
    
    def __str__(self):
        return "{" + " , ".join(str(item) for item in self.__items) + "}"

b1=bag()
b1.add("apple")
b1.add("banana")
b1.add("cherry")

print(b1)

b1.delete_item("apple")
print(b1)

print(b1.size())
print(b1.contains("banana"))



