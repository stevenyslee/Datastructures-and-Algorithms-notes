class stack:

    def __init__(self): #makeEmpty
        self.elements = []

    def __len__(self):
        return len(self.elements)

    # Boolean function, returns true if the stack is not empty.
    # Is to be used in place of isEmpty
    def __bool__(self):
        return bool(self.elements)

    # Allows us to do this: stack += x and x is put at the top of the stack
    def __iadd__(self, element):
        self.elements.append(element)
        return self

    # Pushes an element at the top of the stack, same as
    def push(self, element):
        self.elements.append(element)
        return self

    #Allows us to pop n times the stack using stack -= n
    def __isub__(self, other):
        for i in range(other):
            self.elements.pop()
        return self

    def __str__(self):
        return str(self.elements)

    #Removes the element at the top of the stack
    def pop(self):
        return self.elements.pop()

    # Not a default operation of a stack but allows us to 
    # pop the stack count times and keep the all the elements.
    # as it returns a generator object
    def chop(self, count=1):
        for _ in range(count):
            yield self.elements.pop()

    #Get the topmost element.
    def peek(self):
        return self.elements[-1]

    #Empties itself by creating a new list.
    def make_empty(self):
        self.elements = []
        return self

u = stack()
for x in range(20):
    u += x
print(u)
u -= 4
print(u)
print(u.peek())
u += 1
print(u)
print(u.peek())
for x in u.chop(4):
    print(x)
print(u)
