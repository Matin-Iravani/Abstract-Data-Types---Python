from bianary_search_tree import BianarySearchTree
import os
import time
import random

def printMenue():
    '''
    Prints the menue and actions each round.
    '''
    clearScreen()
    print('MENUE')
    print('SIZE: gets the size of BST\nGET: gets a value of a key in the BST\nMIN: gets the min key of BST')
    print('MAX: gets the max key of the BST\nCONTAINS: checks if a key is in the BST\nRANGE: returns the range of keys in the BST')
    print('EVEN: returns the number of even keys in the BST\nMULTIPLY: multiplies the keys of the tree and returns the value')
    print('CLEAR: clears the BST\nPUT: adds an key/value to the BST\nDEL: deletes an key/value from the BST')
    print('IN: inorder traversal\nPRE: preorder traversal\nPOST: postorder traversal\nRAND: gets a random BST')

def getInput(bst):
    valid = False
    while not valid:
        clearScreen()
        print(bst)

        inp = input('\nPlease Enter What You Would Like To Do: ').lower()

        if inp in ('m', 'q', 'size', 'get', 'min', 'max', 'contains', 'range', 'even', 'multiply', 'clear', 'put', 'del', 'in', 'pre', 'post', 'rand'):
            valid = True
        else:
            print('Invalid Input!')
            time.sleep(1)
    return inp

def clearScreen():
    '''
    Clears the screen.
    '''
    os.system('cls')

def moveCursor(x: int, y: int) -> None:
    '''
    Moves the cursor to the specified location on the terminal.
    - Args:
        - x (int): Column number
        - y (int): Line number
    - Returns: None
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def main():
    
    s = r"""

                WELCOME TO THE BST SIMULATOR! AT ANY TIME ENTER 'M' FOR MENUE AND 'Q' TO QUIT. ;)
        """
    print(s)
    
    for i in range(5):
        print(r"""                .................................................................................""")
        time.sleep(0.5)

    bst = BianarySearchTree()

    while True:
        clearScreen()

        print(bst)
        userInp = getInput(bst)

        if userInp == 'q':
            clearScreen()
            s = r'''                              
            

                                                            GOODBYE!




                '''
            print(s)
            return
        elif userInp == 'm':
            printMenue()
        elif userInp == 'size':
            print('\n> SIZE =', bst.getSize())
        elif userInp == 'min':
            print('\n> MINIMUM KEY =', bst.getMin())
        elif userInp == 'max':
            print('\n> MAXIMUM KEY =', bst.getMax())
        elif userInp == 'range':
            print('\n> RANGE =', bst.range())
        elif userInp == 'even':
            print('\n> # OF EVEN KEYS =', bst.countEven())
        elif userInp == 'multiply':
            print('\n> PRODUCT OF KEYS =', bst.multiplyKey())
        elif userInp == 'in':
            print('\n> INORDER TRAVERSAL:', bst.inorder())
        elif userInp == 'pre':
            print('\n> PREORDER TRAVERSAL:', bst.preorder())
        elif userInp == 'post':
            print('\n> POSTORDER TRAVERSAL:', bst.postorder())
        elif userInp == 'put':
            key = int(input('\nPLEASE ENTER THE KEY: '))
            value = input('PLEASE ENTER THE VALUE: ')
            bst.put(key, value)
        elif userInp == 'get':
            key = int(input('\nPLEASE ENTER THE KEY: '))
            print(f'\n> VALUE OF {key} =', bst.get(key))
        elif userInp == 'contains':
            key = int(input('\nPLEASE ENTER THE KEY: '))
            print(f'\n> BST CONTAINS {key} =', bst.contains(key))
        elif userInp == 'del':
            key = int(input('\nPLEASE ENTER THE KEY: '))
            bst.delete(key)
        elif userInp == 'rand':
            bst = BianarySearchTree()
            lst = [random.randint(0,100) for i in range(150)]
            random.shuffle(lst)
            for item in lst:
                bst.put(item, '')
        elif userInp == 'clear':
            bst.clear()

        input('\nENTER TO CONTINUE....')

if __name__ == '__main__':
    main()