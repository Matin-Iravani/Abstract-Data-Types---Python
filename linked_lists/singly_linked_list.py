class Node:
    '''
    This is a class for a node of a singly linked list which holds attributes of next and data.
    '''
    def __init__(self, data, next):
        '''
        Initializations.
        '''
        self.__data = data
        self.__next = next

    # Getter Methods
    def getData(self):
        '''
        Returns the data of the current node.
        '''
        return self.__data
    
    def getNext(self):
        '''
        Returns the referense to the next node from the curent node.
        '''
        return self.__next
    
    # Setter Methods
    def setData(self, new):
        '''
        Sets the new value of the data of the currnet node.
        '''
        self.__data = new

    def setNext(self, new):
        '''
        Sets the new value of the data of the next node.
        '''
        self.__next = new

    # String methods
    def __str__(self):
        '''
        Retruns a string representation of the node.
        '''
        if self.__next:
            s = f'{self.getData()} -> {self.__next.getData()}'
        else:
            s = f'{self.getData()} -> None'
        return s
    
class SLinkedList:
    '''
    This is a singly linked list class which holds object of the SLinkedList type. This is essentially
    a list which each element node has a referense to the next element node in the list.
    '''
    def __init__(self):
        '''
        Initialzations.
        '''
        self.__head = None
        self.__size = 0
    
    # Getter Methods
    def isEmpty(self):
        '''
        Returns whether the list is empty.
        '''
        return self.__head == None
    
    def size(self):
        '''
        Returns the size of the list.
        '''
        return self.__size
    
    def search(self, item):
        '''
        Searches the list to see if value item exists. Returns bool.
        '''
        current = self.__head
        found = False

        while not found and current:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        if found:
            return True
        return False
    
    def index(self, item):
        '''
        Searches the list to find the index of the item in the list. If the item does not exist,
        returns -1 otherwise returns the index of the item in the list.
        '''
        current = self.__head
        found = False
        index = 0

        while not found and current:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        
        if found:
            return index
        return -1
    
    # Setter Methods
    def clear(self):
        '''
        Clears the whole list and re-intisializes the list.
        '''
        self.__head = None
        self.__size = 0

    def add(self, item):
        '''
        Adds an item to the start of the list. O(1)
        '''
        temp = Node(item, self.__head)
        self.__head = temp
        self.__size += 1

    def append(self, item):
        '''
        Appends an item to the end of the list. O(n)
        '''
        temp = Node(item, None)
        if not self.__head:
            self.__head = temp
        else:
            current = self.__head
            while current.getNext():
                current = current.getNext()
            current.setNext(temp)
        self.__size += 1

    def insert(self, index, item):
        '''
        Inserts an item at a specific index. Positive Indeces accepted only and the index has to be
        in range of the list size. Raise IndexError if index invalid.
        '''
        if type(index) != int or index < 0 or index > self.size():
            raise IndexError('Index out of range.')

        if index == 0:
            self.add(item)
        elif index == self.size():
            self.append(item)
        else:
            current = self.__head
            previous = None
            ind = 0
            
            while ind != index:
                previous = current
                current = current.getNext()
                ind += 1
            
            temp = Node(item, current)
            previous.setNext(temp)
            self.__size += 1
    
    def pop(self, pos=None):
        '''
        Pops from the given position and returns the removed value. If no position is provided the deafault
        value of end of the list is used.
        '''
        if self.isEmpty():
            raise IndexError('List is empty.')
        if pos != None and (type(pos) != int or pos < 0 or pos >= self.size()):
            raise IndexError('Index out of range.')

        if pos == None:
            pos = self.size()-1

        current = self.__head
        previous = None
        index = 0
        while index != pos:
            previous = current
            current = current.getNext()
            index += 1
        
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.__size -= 1
        return current.getData()

    def remove(self, item):
        '''
        Removes an item from the list and if item does not exist or list is empty, does nothing.
        '''
        current = self.__head
        previous = None
        found = False

        while current and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if not found:
            return
        
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.__size -= 1
        
    # Str Methods
    def __repr__(self):
        '''
        Returns a formal string representation of the singly linked list.
        '''
        current = self.__head
        lst = []
        while current != None:
            lst.append(str(current))
            current = current.getNext()
        return ' | '.join(lst)
    
    def __str__(self):
        '''
        Returns an informal representation of the singly linked list.
        '''
        current = self.__head
        lst = []
        while current != None:
            lst.append(current.getData())
            current = current.getNext()
        return str(lst)

def main():
    lst = SLinkedList()

    # Mutations
    
    '''lst.append('matin')
    lst.append('Iravani')
    lst.add(1756439)'''
    print(lst)
    lst.insert(0, 0)
    lst.insert(1, 2)
    lst.insert(1,1)


    # Print the list
    print(repr(lst))
    print()

    # Print popping from the list
    lst.remove(6)
    print(lst)

    # Print list size
    print('SIZE:', lst.size(),)

    # Print list is empty
    print('ISEMPTY:', lst.isEmpty())


    item = 'matin'
    # Search for an item in the list
    print(f'Searching for {item}:', lst.search(item))

    # Get index of an item in list
    print(f'Index of {item}:', lst.index(item))

if __name__ == '__main__':
    main()