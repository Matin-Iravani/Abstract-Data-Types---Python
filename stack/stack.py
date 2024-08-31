class Stack:
    '''
    This is a stack class which implements the LIFO policy of item addition and removing.
    '''
    def __init__(self):
        '''
        Initializations.
        '''
        self.__items = []
        
    # Getter Methods
    def size(self):
        '''
        Returns the number of items in the stack.
        '''
        return len(self.__items)
    
    def isEmpty(self):
        '''
        Returns whether the stack is empty or not.
        '''
        return self.size() == 0
    
    def peek(self):
        '''
        Peeks the top of the stack and returns the item that is currently next in line to be poped.
        If the stack has nothing in it it raises an exception.
        '''
        if self.isEmpty():
            raise Exception('EmptyStackError: Stack Is Empty.')
        return self.__items[-1]
    
    # Setter Methods
    def push(self, item):
        '''
        Pushes an item to the top of the stack.
        '''
        self.__items.append(item)

    def pop(self):
        '''
        Pops the top of the stack and returns the item. If the stack is empty it raises an exception.
        '''
        if self.isEmpty():
            raise Exception('EmptyStackError: Stack Is Empty.')
        return self.__items.pop()
    
    # String Methods
    def __str__(self):
        '''
        Returns the string representation of the stack.
        '''
        return str(self.__items)