class BQueue:
    '''
    This is a bounded Queue data structure which uses the FIFO policy when items are queued
    This Queue has a set boundry and only capacity numbers of items can be enqueued.
    - This implementation conciders the top of queue to be the front of list and the back
    to be the back of the list (does not use linked-lists)
    '''
    def __init__(self, capacity=10):
        '''
        Makes sure the capacity is valid (ie. greater than zero and an integer)
        otherwise raises CapacityError
        '''
        if type(capacity) != int or capacity <= 0:
            raise Exception('CapacityError')
        self.__items = []
        self.__capacity = capacity
        
    # Representation methods
    def __str__(self):
        '''
        Returns a string representation of the items in the queue where first element
        from left is the head and the last element from left is the tail.
        '''
        itemStr = str(self.__items)[1:-1]
        return f"<{itemStr}< MAX={self.__capacity}"
    
    def show(self):
        '''
        Prints the items in the queue the same fromat as __str__
        '''
        print(self.__items)
    
    # Mutator Methods
    def enqueue(self, item):
        '''
        Enqueues the item to the Queue -> O(1) however if enqueuing an item surpasses the
        capacity limit, it raises a FullQueueError and nothing is enqueued
        '''
        if len(self.__items) == self.__capacity:
            raise Exception('FullQueueError')
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
    
    # Getter Methods
    def peek(self):
        '''
        Returns a string repr of the next item at the head of the Queue -> O(n) and 
        if the Queue is empty it raises and EmptyQueueError
        '''
        if self.__items == []:
            raise Exception('EmptyQueueError')
        return str(self.__items[0])

    def size(self):
        '''
        Retruns the number of items in the Queue as an int
        '''
        return len(self.__items)
    
    def capacity(self):
        '''
        Returns the exact value of the capacity of the BQueue
        '''
        return self.__capacity
    
    def isEmpty(self):
        '''
        Checks whether the Queue is empty and returns corresponding boolean value
        '''
        return self.__items == []
    
    def isFull(self):
        '''
        Checks whether the Queue is full and returns corresponding boolean value
        '''
        return len(self.__items) == self.__capacity
    
def main():
    bq = BQueue()  # no value sets capacity to 10
    print(help(BQueue))

if __name__ == '__main__':
    main()