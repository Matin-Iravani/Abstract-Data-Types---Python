def selectionSort(data: list) -> None:
    '''
    Runs a Selection Sort on a list of data and does the sorting in place (Ascending order).
    - BEST CASE: O(n^2)
    - WORST CASE: O(n^2)
    - AVG CASE: O(n^2)
    '''
    for index in range(len(data)-1):
        smallestIndex = index

        for position in range(index + 1, len(data)):
            if data[position] < data[smallestIndex]:
                smallestIndex = position
        
        # If new smallest index was found
        if smallestIndex != index:
            temp = data[index]
            data[index] = data[smallestIndex]
            data[smallestIndex] = temp

#### TESTING ####
def main():
    # test 1
    lst1 = [1,10,0,3,-10,100,0,-2,24,-1]
    # test 2
    lst2 = [100,1,2,3,4,5]                # BEST CASE IF LIST IS SORTED OR HAS ONE ITEM NOT IN PLACE
    # test 3
    lst3 = [10,9,8,7,6,5,4,3,2,1]         # WORST CASE DOES 10 PASSES or N PASSES

    print(lst1)
    selectionSort(lst1)
    print(lst1)
if __name__ == '__main__':
    main()