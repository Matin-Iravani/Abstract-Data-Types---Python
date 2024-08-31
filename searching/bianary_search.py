def bianarySearch(key: int, data: list) -> int:
    '''
    Does a bianary Search in log2 n time and returns an index of
    an item in the list. If the item is not in the list it returns None.
    NOTE: LIST MUST BE SORTED.
    '''
    found = False
    first = 0
    last = len(data)-1

    while not found and first <= last:
        guess = (first + last) // 2

        if data[guess] == key:
            found = True
        elif data[guess] < key:
            first = guess + 1
        else:
            last = guess - 1
    
    if not found:
        return None
    return guess

def main():
    lst = [-100,0,1,100,210]

    print(bianarySearch(210, lst))

if __name__ == '__main__':
    main()