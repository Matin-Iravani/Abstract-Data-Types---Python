class Node:
    '''
    This class represents a node of the doubly linked list class which has a next, previous and
    a data attribute.
    '''
    def __init__(self, data, next, prev):
        '''
        Initializations.
        '''
        self.__data = data
        self.__next = next
        self.__prev = prev

        if next:
            self.__next.setPrevious(self)
        if prev:
            self.__prev.setNext(self)

    # Getter Methods
    def getData(self):
        '''
        Returns the data value of the node.
        '''
        return self.__data
    
    def getNext(self):
        '''
        Returns the next referense of the current node.
        '''
        return self.__next
    
    def getPrevious(self):
        '''
        Returns the previous referense of the current node.
        '''
        return self.__prev

    # Setter Methods
    def setData(self, new):
        '''
        Sets a new data value for the node.
        '''
        self.__data = new

    def setNext(self, new):
        '''
        Sets a new next value for the node.
        '''
        self.__next = new

    def setPrevious(self, new):
        '''
        Sets a new previous value for the node.
        '''
        self.__prev = new
        
    # String Methods
    def __str__(self):
        '''
        Returns an informal representation of the current node.
        '''
        if self.__prev:
            prev = self.__prev.getData()
        else:
            prev = 'None'
        
        if self.__next:
            next = self.__next.getData()
        else:
            next = 'None'

        return f'{prev} <- [{self.__data}] -> {next}'
    
class DLinkedList:
    '''
    This is the doubly linked list class which is essentialy a list where each element has a link to the next and
    previous element nodes.
    '''
    def __init__(self):
        '''
        Initializations.
        '''
        self.__head = self.__tail = None
        self.__size = 0

    # Getter Methods
    def isEmpty(self):
        '''
        Returns whether the list is empty or not.
        '''
        return self.__head == None
    
    def size(self):
        '''
        Returns the size of the list.
        '''
        return self.__size
    
    def search(self, item):
        '''
        Returns True if an item is part of the list and False otherwise.
        '''
        current = self.__tail
        found = False

        while not found and current:
            if current.getData() == item:
                found = True
            else:
                current = current.getPrevious()
        
        if found:
            return True
        return False
    
    def index(self, item):
        '''
        Returns the index of an item in the list, and if the item is not part of the list
        it returns -1.
        '''
        current = self.__tail
        index = self.__size-1
        found = False

        while current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getPrevious()
                index -= 1
        
        if found:
            return index
        return -1
    
    def getHead(self):
        '''
        Returns the item at the head of the list.
        '''
        return self.__head.getData()

    # Setter Methods
    def clear(self):
        '''
        Clears the entire list and reinitializes the list.
        '''
        self.__head = self.__tail = None
        self.__size = 0

    def add(self, item):
        '''
        Adds an item to the begining of the list. O(1)
        '''
        temp = Node(item, self.__head, None)
        if not self.__head:
            self.__tail = temp
        self.__head = temp
        self.__size += 1

    def append(self, item):
        '''
        Appends an item to the end of the list. O(1)
        '''
        temp = Node(item, None, self.__tail)
        if not self.__head:
            self.__head = temp
        self.__tail = temp
        self.__size += 1
    
    def insert(self, pos, item):
        '''
        Inserts an item at a given position and if index is out of range of the list, it raises a
        IndexError.
        '''
        if type(pos)!=int or pos<0 or pos>self.__size:
            raise IndexError('Index Out Of Range.')
        
        if pos == 0:
            self.add(item)
        elif pos == self.__size:
            self.append(item)
        else:
            current = self.__head
            previous = None
            index = 0

            while index != pos:
                previous = current
                current = current.getNext()
                index += 1
            
            Node(item, current, previous)
            self.__size += 1
    
    def pop(self, pos=None):
        '''
        Pops from the given position and returns the removed value. If no position is provided the deafault
        value of end of the list is used.
        '''
        if self.isEmpty():
            raise IndexError('List Is Empty.')
        if pos != None and (type(pos)!=int or pos<0 or pos>=self.__size):
            raise IndexError('Index Out Of Range.')
        
        if pos == None:
            pos = self.__size - 1
        
        current = self.__head
        previous = None
        index = 0
        
        while index != pos:
            previous = current
            current = current.getNext()
            index += 1
        
        if not previous:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())

        if not current.getNext():
            self.__tail = previous
        else:
            current.getNext().setPrevious(previous)
        self.__size -= 1

        return current.getData()
    
    def remove(self, item):
        '''
        Removes an item from the list and if item does not exist or list is empty, does nothing.
        '''
        current = self.__head
        previous = None
        
        while current and current.getData() != item:
            previous = current
            current = current.getNext()
        
        if not current:
            return
         
        if not previous:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
        if not current.getNext():
            self.__tail = previous
        else:
            current.getNext().setPrevious(previous)
        self.__size -= 1

    # String Methods
    def __repr__(self):
        '''
        Retruns a formal representation of the doubly linked list class.
        '''
        current = self.__head
        lst = []
        while current != None:
            lst.append(str(current))
            current = current.getNext()
        return ' | '.join(lst)
    
    def __str__(self):
        '''
        Returns an informal representation of the doubly linked list class.
        '''
        current = self.__head
        lst = []
        while current:
            lst.append(current.getData())
            current = current.getNext()
        return str(lst)
    
def main():
    lst = DLinkedList()

    # Adding and removing
    
    lst.append('aa')
    lst.append('bb')
    lst.insert(2, 'cc')

    # Print the list
    print(repr(lst))
    print(lst)
    print()

    # Print is empty
    print('EMPTY:', lst.isEmpty())

    # Print size
    print('SIZE:', lst.size())

    # Print Search for an item
    print('SEARCH:', lst.search('bb'))

    # Print index of an item
    print('INDEX:', lst.index('bb'))

    # Print poped
    '''print('POPED', lst.pop(1))
    lst.pop(0)'''
    lst.remove('bb')
    lst.remove('cc')
    lst.remove('aa')
    lst.remove('aa')
    
    print(repr(lst))
    print(lst)
if __name__ == '__main__':
    main()