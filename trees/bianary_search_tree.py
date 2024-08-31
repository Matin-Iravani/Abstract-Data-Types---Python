class TreeNode:
    '''
    This is a class defining the tree nodes of a bianary search tree BST.
    '''
    def __init__(self, key, val, right=None, left=None, parent=None):
        '''
        Initialize the data attributes of the node.
        '''
        self.__key = key
        self.__val = val
        self.__right = right
        self.__left = left
        self.__parent = parent

    # Getter Methods
    def getKey(self):
        '''
        Returns the key of the tree node.
        '''
        return self.__key
    
    def getValue(self):
        '''
        Returns the value of the tree node.
        '''
        return self.__val
    
    def getRight(self):
        '''
        Returns the right child of the current tree node.
        '''
        return self.__right
    
    def getLeft(self):
        '''
        Returns the left child of the current tree node.
        '''
        return self.__left
    
    def getParent(self):
        '''
        Returns the parent tree node of the current tree node.
        '''
        return self.__parent
    
    def hasRight(self):
        '''
        Returns True if currentNode has a right child.
        '''
        if self.__right:
            return True
        return False
    
    def hasLeft(self):
        '''
        Returns True if the currentNode has left child.
        '''
        if self.__left:
            return True
        return False
    
    # Setter Methods
    def setKey(self, new):
        '''
        Sets a new key for the node.
        '''
        self.__key = new

    def setValue(self, new):
        '''
        Sets a new value for the node.
        '''
        self.__val = new

    def setRight(self, new):
        '''
        Sets a new right child for the node.
        '''
        self.__right = new

    def setLeft(self, new):
        '''
        Sets a new left child for the node.
        '''
        self.__left = new
    
    def setParent(self, new):
        '''
        Sets a new parrent node for the node.
        '''
        self.__parent = new

    # String Methods
    def _strHelper(self):
        '''
        Returns list of strings, total width of the tree, position of the middle node and the height
        '''
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.__key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.__key
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper() 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
        
    def __str__(self):
        '''
        Returns a printed representation of the tree starting from a given root node.
        '''
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result

class BianarySearchTree:
    '''
    This is a bianary search tree class which creates objects of the type BST which follow a normal
    bianary tree just with specific ordering to how items are added and removed. Where searching/inserting/deleting
    can be done in log2 n time if the tree is balanced. Another property is that an unsorted aray of numbers
    can be inserted into a BST and an inorder traversal will result in a sorted ascending list of keys.
    '''
    def __init__(self):
        self.__root = None
        self.__size = 0
    
    # Getter Methods
    def getSize(self):
        '''
        Returns the number of items in the tree.
        '''
        return self.__size
    
    def get(self, key):
        '''
        Returns the value stored in the tree for a key if exists, returns None otherwise.
        '''
        return self._get(key, self.__root)
    
    def _get(self, key, currentNode: TreeNode):
        '''
        getKey() helper function.
        '''
        if not currentNode:
            return None
        elif currentNode.getKey() == key:
            return currentNode.getValue()
        elif currentNode.getKey() < key:
            return self._get(key, currentNode.getRight())
        else:
            return self._get(key, currentNode.getLeft())
    
    def getMin(self):
        '''
        Returns the minimum key of the bst useing recurssion.
        '''
        return self._getMin(self.__root)
    
    def _getMin(self, currentNode: TreeNode):
        '''
        getMin() helper function.
        '''
        if not currentNode:
            return None
        else:
            if currentNode.hasLeft():
                return self._getMin(currentNode.getLeft())
            else:
                return currentNode.getKey()
    
    def getMax(self):
        '''
        Returns the maximum key of the bst using recurssion.
        '''
        return self._getMax(self.__root)
    
    def _getMax(self, currentNode: TreeNode):
        '''
        getMax() helper function.
        '''
        if not currentNode:
            return None
        else:
            if currentNode.hasRight():
                return self._getMax(currentNode.getRight())
            else:
                return currentNode.getKey()
    
    def getCopy(self):
        '''
        Returns a copy of the BST by using its own preorder traversal to rebuild a scondary BST.
        '''
        if not self.__root:
            return None
        else:
            newTree = BianarySearchTree()
            pre = self.preorder()

            for item in pre:
                newTree.put(item, self.get(item))
            
            return newTree
    
    def contains(self, key):
        '''
        Returns True if the tree contains a key and Flase otherwise.
        '''
        return self._contains(key, self.__root)
    
    def _contains(self, key, currentNode: TreeNode):
        '''
        contains() helper function.
        '''
        if not currentNode:
            return False
        elif currentNode.getKey() == key:
            return True
        elif currentNode.getKey() < key:
            return self._contains(key, currentNode.getRight())
        else:
            return self._contains(key, currentNode.getLeft())
    
    def range(self):
        '''
        Finds the range of key numbers in the Bianary Tree. Returns None if no items in tree
        '''
        if self.__root:
            return self._getMax(self.__root) - self._getMin(self.__root)
        else:
            return None
    
    def countEven(self):
        '''
        Returns the number of keys which are even.
        '''
        return self._countEven(self.__root)
    
    def _countEven(self, currentNode: TreeNode):
        '''
        countEven() helper function.
        '''
        if not currentNode:
            return 0
        
        total = 0

        if currentNode.getKey() % 2 == 0:
            total += 1
        
        return total + self._countEven(currentNode.getLeft()) + self._countEven(currentNode.getRight())
    
    def multiplyKey(self):
        '''
        Multiplies all keys in the BST and returns the value. Returns None if BST is empty.
        '''
        if self.__root:
            return self._multiply(self.__root)
        else:
            return None
    
    def _multiply(self, currentNode: TreeNode):
        '''
        multiplyKey() helper function.
        '''
        if currentNode:
            return currentNode.getKey() * self._multiply(currentNode.getLeft()) * self._multiply(currentNode.getRight())
        else:
            return 1
    
    # Setter Methods
    def clear(self):
        '''
        Clears the BST completely.
        '''
        self.__root = None
        self.__size = 0

    def put(self, key, val):
        '''
        Adds a new key-value pair to the tree, replaces the old value if the key already exists in the
        tree.
        '''
        if not self.__root:
            self.__root = TreeNode(key, val)
            self.__size += 1
        else:
            self._add(key, val, self.__root)
    
    def _add(self, key, val, currentNode: TreeNode):
        '''
        put() helper function.
        '''
        if currentNode.getKey() == key:
            currentNode.setValue(val)
        elif currentNode.getKey() < key:
            if currentNode.hasRight():
                self._add(key, val, currentNode.getRight())
            else:
                currentNode.setRight(TreeNode(key, val, parent = currentNode))
                self.__size += 1
        else:
            if currentNode.hasLeft():
                self._add(key, val, currentNode.getLeft())
            else:
                currentNode.setLeft(TreeNode(key, val, parent = currentNode))
                self.__size += 1
    
    def delete(self, key):
        '''
        Delets a key-value pari from the tree.
        '''
        if self.__size == 1 and self.__root.getKey() == key:
            self.__root = None
            self.__size -= 1
        elif self.__size > 1:
            nodeToRemove = self._locate(key, self.__root)
            #print("REMOVE:", nodeToRemove)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self.__size -= 1
            else:
                print('No such node exists!')
        else:
            print('No such node exists!!')
    
    def _locate(self, key, currentNode: TreeNode):
        '''
        delete() helper function.
        '''
        if not currentNode:
            return None
        elif currentNode.getKey() == key:
            return currentNode
        elif currentNode.getKey() < key:
            return self._locate(key, currentNode.getRight())
        else:
            return self._locate(key, currentNode.getLeft())
    
    def _remove(self, currentNode: TreeNode):
        '''
        delete() helper function.
        '''
        right = currentNode.getRight()
        left = currentNode.getLeft()
        parent = currentNode.getParent()

        # Case 1 a leaf node
        if not right and not left:
            if parent.getLeft() == currentNode:
                parent.setLeft(None)
            else:
                parent.setRight(None)

        # Case 2.1 has one right child
        elif right and not left:
            if not parent:
                self.__root = right
            elif parent.getLeft() == currentNode:
                parent.setLeft(right)
            else:
                parent.setRight(right)
            right.setParent(parent)

        # Case 2.2 one left child
        elif left and not right:
            if not parent:
                self.__root = left
            elif parent.getLeft() == currentNode:
                parent.setLeft(left)
            else:
                parent.setRight(left)
            left.setParent(parent)
        
        # Case 3 has 2 childeren
        else:
            swap = self._findSmallest(right)
            currentNode.setKey(swap.getKey())
            currentNode.setValue(swap.getValue())
            self._remove(swap)
    
    def _findSmallest(self, currentNode: TreeNode):
        '''
        _remove() helper function.
        '''
        if currentNode.hasLeft():
            return self._findSmallest(currentNode.getLeft())
        else:
            return currentNode

    # Traversal Methods
    def inorder(self):
        '''
        Returns a list containing the inorder traversal of the BST.
        '''
        lst = []
        self._inorder(self.__root, lst)
        return lst

    def _inorder(self, currentNode: TreeNode, lst):
        '''
        inorder() helper function.
        '''
        if currentNode:
            self._inorder(currentNode.getLeft(), lst)
            lst.append(currentNode.getKey())
            self._inorder(currentNode.getRight(), lst)
    
    def preorder(self):
        '''
        Returns a list containing the preorder traversal of the BST.
        '''
        lst = []
        self._preorder(self.__root, lst)
        return lst
    
    def _preorder(self, currentNode: TreeNode, lst):
        '''
        preorder() helper function.
        '''
        if currentNode:
            lst.append(currentNode.getKey())
            self._preorder(currentNode.getLeft(), lst)
            self._preorder(currentNode.getRight(), lst)
    
    def postorder(self):
        '''
        Returns a list containing the postorder Traversal of the BST.
        '''
        lst = []
        self._postorder(self.__root, lst)
        return lst
    
    def _postorder(self, currentNode: TreeNode, lst):
        '''
        postorder() helper function.
        '''
        if currentNode:
            self._postorder(currentNode.getLeft(), lst)
            self._postorder(currentNode.getRight(), lst)
            lst.append(currentNode.getKey())

    # String Methods
    def __str__(self):
        '''
        Returns formated tree from the root node.
        '''
        return str(self.__root)

#### TESTING ####
def main():
    bst = BianarySearchTree()

    bst.put(10, 'a')
    bst.put(11, 'b')
    bst.put(5, '4')
    bst.put(2, 'a')
    bst.put(4, 'a')
    bst.put(10.5, 'a')
    bst.put(1, 'a')
    bst.put(9, 'matin')
    #bst.put(1000,'l')
    #bst.clear()
    #bst.put(9, 'a')
    bst.delete(10)
    
    minn = bst.getMin()
    maxx = bst.getMax()
    rang = bst.range()
    even = bst.countEven()

    print(bst.multiplyKey())
    print(even)

    print(rang)
    print(bst.contains(4))
    print(bst)
    print(minn)
    print(maxx)

if __name__ == '__main__':
    main()