def insertionSort(data: list) -> None:
    '''
    Runs a Insertion Sort on a list of data and does the sorting in place (Ascending order).
    - BEST CASE: O(n) -> If list is sorted
    - WORST CASE: O(n^2) -> If list is reverse order
    - AVG CASE: O(n^2)
    '''
    pas1 = 1
    pas2 = 1
    for index in range(1, len(data)):

        position = index
        temp = data[index]

        while position > 0 and data[position - 1] > temp:
            data[position] = data[position - 1]
            position -= 1
            pas1 += 1
            
        pas2 += 1

        data[position] = temp
    print('INNER', pas1)
    print('OUTER', pas2)

#### TESTING ####
def main():
    # test 1
    lst1 = [1,10,0,3,-10,100,0,-2,24,-1]
    # test 2
    lst2 = [100,1,2,3,4,5]                # BEST CASE IF LIST IS SORTED OR HAS ONE ITEM NOT IN PLACE
    # test 3
    lst3 = [10,9,8,7,6,5,4,3,2,1]         # WORST CASE DOES 10 PASSES or N PASSES
    lst4 = [2,1,3,4,5]

    print(lst4)
    insertionSort(lst4)
    print(lst4)
if __name__ == '__main__':
    main()