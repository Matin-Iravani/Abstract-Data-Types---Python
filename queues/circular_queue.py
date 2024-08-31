class CQueue:
    '''
    This is a circular Queue data structure which uses the FIFO policy when items are queued
    This Queue has a set boundry and only capacity numbers of items can be enqueued.
    - This implementation conciders the head and tail of queue to be set to zero and uses
    value None for values that are dequeued
    - This CQueue also uses a count to keep track of number of cached items in the queue
    (does not use linked-lists)
    - This implementation does not leave an extra space for head and tail but fills in the
    items list with None at the initialization stage
    '''
    def __init__(self, capacity=10):
        '''
        Makes sure the capacity is valid (ie. greater than zero and an integer)
        otherwise raises CapacityError
        '''
        if type(capacity) != int or capacity <= 0:
            raise Exception('CapacityError')
        self.__capacity = capacity
        self.__head = self.__tail = self.__count = 0
        self.__items = [None for i in range(self.__capacity)]

    # Representation methods
    def __str__(self):
        '''
        Returns a string representation of the items in the queue where first element
        from left is the head and the last element from left is the tail.
        '''
        itemStr = str(self.__items)[1:-1]
        return f"]{itemStr}] H={self.__head} T={self.__tail} Capacity={self.__count}/{self.__capacity}"

    def __repr__(self):
        '''
        Returns a string representation of the items in the queue where first element
        from left is the head and the last element from left is the tail.
        '''
        itemStr = '] '
        i = self.__head
        for j in range(self.__count):
            itemStr += str(self.__items[i]) + ' '
            i = (i+1)%self.__capacity
        return f"{itemStr}]  H={self.__head} T={self.__tail} Capacity={self.__count}/{self.__capacity}"

    def show(self):
        '''
        Prints the items in the queue the same fromat as __str__
        '''
        print(self.__items)

    # Mutator methods
    def enqueue(self, item):
        '''
        Enqueues the item to the Queue -> O(1) however if enqueuing an item surpasses the
        capacity limit, it raises a FullQueueError and nothing is enqueued
        '''
        if self.__count == self.__capacity:
            raise Exception('FullQueueError')
        self.__items[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__count += 1

    def dequeue(self):
        '''
        If the Queue is empty it raises an EmptyQueueError and otherwise it returns the
        dequeued item -> O(n)
        '''
        if self.__count == 0:
            raise Exception('EmptyQueueError')
        item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__count -= 1
        return item
    
    def clear(self):
        '''
        Clears the Queue completly
        '''
        self.__items = [None for i in range(self.__capacity)]
        self.__head = self.__tail = self.__count = 0
    
    # Getter methods
    def peek(self):
        '''
        Returns a string repr of the next item at the head of the Queue -> O(n) and 
        if the Queue is empty it raises and EmptyQueueError
        '''
        if self.__count == 0:
            raise Exception('EmptyQueueError')
        return str(self.__items[self.__head])
    
    def size(self):
        '''
        Retruns the number of items in the Queue as an int
        '''
        return self.__count
    
    def capacity(self):
        '''
        Returns the exact value of the capacity of the BQueue
        '''
        return self.__capacity
    
    def isEmpty(self):
        '''
        Checks whether the Queue is empty and returns corresponding boolean value
        '''
        return self.__count == 0
    
    def isFull(self):
        '''
        Checks whether the Queue is full and returns corresponding boolean value
        '''
        return self.__count == self.__capacity
    
def main():
    print(help(CQueue))

if __name__ == "__main__":
    main()