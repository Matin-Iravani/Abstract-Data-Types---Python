def bubbleSort(data: list, passes=True) -> None:
    '''
    Runs a Bubble Sort on a list of data and does the sorting in place (Ascending order).
    - BEST CASE: O(n) -> if list is sorted
    - WORST CASE: O(n^2) -> if list is reverse sorted or unsorted
    - AVG CASE: O(n^2)
    - IF pass is set to FALSE it wont print the passes it took
    '''
    pas = 1

    for lastIndex in range(len(data)-1, 0, -1):
        changed = False

        for index in range(lastIndex):
            if data[index] > data[index + 1]:
                # Swap
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp
                changed = True
        
        if not changed:
            if passes:
                print(pas)
            return
        
        pas += 1
    
    if passes:
        print(pas)
        
#### TESTING ####
def main():
    # test 1
    lst1 = [1,10,0,3,-10,100,0,-2,24,-1]
    # test 2
    lst2 = [100,1,2,3,4,5]                # BEST CASE IF LIST IS SORTED OR HAS ONE ITEM NOT IN PLACE
    # test 3
    lst3 = [10,9,8,7,6,5,4,3,2,1]         # WORST CASE DOES 10 PASSES or N PASSES

    print(lst3)
    bubbleSort(lst3)
    print(lst3)
    
if __name__ == '__main__':
    main()