class Set:
    def __init__(self):
        self.__items = []

    def add(self, item):
        if item not in self.__items:
            self.__items.append(item)
        else:
            print("this item already exists in set")

    def delete_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("this item does not exist in set")

    def union(self, other):
        result = Set()
        for item in self.__items:
            result.add(item)
        for item in other.__items:
            result.add(item)
        return result

    def intersection(self, other):
        result = Set()
        for item in self.__items:
            if item in other.__items:
                result.add(item)
        return result

    def difference(self, other):
        result = Set()
        for item in self.__items:
            if item not in other.__items:
                result.add(item)
        return result

    def __iter__(self):
        return iter(self.__items)
    
    def __str__(self):         
        return "{" + " , ".join(str(item) for item in self.__items) + "}"   
    def __getitem__(self, index):
        return self.__items[index]
    
    def __setitem__(self, index, value):
        if value not in self.__items:
            self.__items[index] = value
        else:
            print("this item already exists in set")


if __name__ == "__main__":
    
    s1 = Set()
    s2 = Set()
    
    
    s1.add(1)
    s1.add(2)
    s1.add(3)
    s1.add(4)
    
    
    s2.add(3)
    s2.add(4)
    s2.add(5)
    s2.add(6)
    
    print("first set:", s1)
    print("second set:", s2)
    
    
    union_result = s1.union(s2)
    print("union:", union_result)
    
    
    intersection_result = s1.intersection(s2)
    print("interssec:", intersection_result)
    
    
    difference_result = s1.difference(s2)
    print("diff", difference_result)
    
    
    s1.delete_item(2)
    print(" rem:", s1)
    
    
    print("  ", s1[0])
    
    
    print("items in s1:")
    for item in s1:
        print(item)


