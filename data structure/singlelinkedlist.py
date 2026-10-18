class linkedlist :    
    class _node :
       __slots__ = 'element', 'next'
       
       def __init__(self, element, next):  # Fixed: __init__ not __intit__
           self.element = element  # Fixed: use element, not _element
           self.next = next  # Fixed: use next, not _next
    
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size            
    
    def isempty(self):
        return self._size == 0   
    
    def push(self, element):
        # Fixed parameter order: element first, then next
        self._head = self._node(element, self._head)
        self._size += 1
    
    def top(self):
        if self.isempty():
            raise Exception("Stack is empty")
        return self._head.element  # Fixed: access .element (not ._element)
    
    def pop(self):
        if self.isempty():
            raise Exception("Stack is empty")
        else:
            answer = self._head.element  # Fixed: access .element
            self._head = self._head.next  # Fixed: access .next
            self._size -= 1
            return answer


# Test the corrected code
s = linkedlist()
print("Is empty?", s.isempty())  # True
print("Length:", len(s))  # 0

s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)

print("Top element:", s.top())  # Should print 9
print("Length after pushes:", len(s))  # Should print 5

# Test pop
print("Popped:", s.pop())  # Should print 9
print("Top after pop:", s.top())  # Should print 8
print("Length after pop:", len(s))  # Should print 4