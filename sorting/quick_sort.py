TIMES = [0]

def quickSort(data: list, TIMES) -> None:
    '''
    Runs a Quick Sort on a list of data and does the sorting in place (Ascending order).
    - BEST CASE: O(n log2 n) -> if list is unsorted
    - WORST CASE: O(n^2) -> if list is sorted in any way => creates unbalanced recurssive tree makes it
    like a linked list.
    - AVG CASE: O(n log2 n)
    '''
    helper(data, 0, len(data)-1, TIMES)

def helper(data: list, first: int, last: int, TIMES) -> None:
    '''
    QuickSort helper.
    '''
    if first < last:
        TIMES[0] += 1
        pivot = partition(data, first, last)
        helper(data, first, pivot - 1, TIMES)
        helper(data, pivot + 1, last, TIMES)

def partition(data: list, first: int, last: int) -> None:
    '''
    Haore's partitioning to partion for quicksort.
    '''
    pivot = data[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and data[left] <= pivot:
            left += 1
        
        while right >= left and data[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
    
    temp = data[right]
    data[right] = pivot
    data[first] = temp

    return right

#### TESTING ####
def main():
    # test 1
    lst1 = [5,4,3,2,1]
    # test 2
    lst2 = [100,1,2,3,4,5]                # BEST CASE IF LIST IS SORTED OR HAS ONE ITEM NOT IN PLACE
    # test 3
    lst3 = [10,9,8,7,6,5,4,3,2,1]         # WORST CASE DOES 10 PASSES or N PASSES

    print(lst1)
    quickSort(lst1, TIMES)
    print(TIMES)
    print(lst1)
    
if __name__ == '__main__':
    main()