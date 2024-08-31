def mergeSort(data: list) -> list:
    '''
    Runs a Merge Sort on a list of data and does not do the sorting in place (Ascending order).
    - BEST CASE: O(n log2 n)
    - WORST CASE: O(n log2 n)
    - AVG CASE: O(n log2 n)
    '''
    if len(data) <= 1:
        return data
    
    middle = len(data)//2

    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])

    return merge(left, right)

def merge(left: list, right: list) -> list:
    '''
    Merge function for mergeSort which merges two sorted lists into one and returns the new
    list.
    '''
    leftIndex = rightIndex = 0
    result = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    
    result += left[leftIndex:]
    result += right[rightIndex:]

    return result

#### TESTING ####
def main():
    # test 1
    lst1 = [1,10,0,3,-10,100,0,-2,24,-1]
    # test 2
    lst2 = [100,1,2,3,4,5]                # BEST CASE IF LIST IS SORTED OR HAS ONE ITEM NOT IN PLACE
    # test 3
    lst3 = [10,9,8,7,6,5,4,3,2,1]         # WORST CASE DOES 10 PASSES or N PASSES

    print(lst1)
    new = mergeSort(lst1)
    print(new)
    
if __name__ == '__main__':
    main()