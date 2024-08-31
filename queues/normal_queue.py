class Queue:
    '''
    This is a normal Queue data structure which uses the FIFO policy when items are queued
    This Queue has no set boundry and n numbers of items can be enqueued
    - This implementation conciders the top of queue to be the front of list and the back
    to be the back of the list (does not use linked-lists)
    '''
    def __init__(self):
        '''
        Initializations.
        '''
        self.__items = []
    
    # Representation methods
    def __str__(self):
        '''
        Returns a string representation of the items in the queue where first element
        from left is the head and the last element from left is the tail.
        '''
        return str(self.__items)
    
    def show(self):
        '''
        Prints the items in the queue the same fromat as __str__
        '''
        print(self.__items)

    # Mutator methods
    def enqueue(self, item):
        '''
        Enqueues the item to the Queue -> O(1)
        '''
        self.__items.append(item)

    def dequeue(self):
        '''
        If the Queue is empty it raises an EmptyQueueError and otherwise it returns the
        dequeued item -> O(n)
        '''
        if self.__items == []:
            raise Exception('EmptyQueueError')
        return self.__items.pop(0)
    
    def clear(self):
        '''
        Clears the Queue completly
        '''
        self.__items = []

    # Getter methods
    def size(self):
        '''
        Retruns the number of items in the Queue as an int
        '''
        return len(self.__items)
    
    def isEmpty(self):
        '''
        Checks whether the Queue is empty and returns corresponding boolean value
        '''
        return self.__items == []
    
    def peek(self):
        '''
        Returns a string repr of the next item at the head of the Queue -> O(n) and 
        if the Queue is empty it raises and EmptyQueueError
        '''
        if self.__items == []:
            raise Exception('EmptyQueueError')
        return str(self.__items)
    
def main():
    print(help(Queue))

if __name__ == '__main__':
    main()