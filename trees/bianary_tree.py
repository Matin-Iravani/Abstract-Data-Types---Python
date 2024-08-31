class BianaryTree:
    '''
    This is a Bianary Tree class where each Bianary Tree instance is a root node which has a
    leftChild and a rightChild node. NOTE: node and bianaryTree are in one class for this
    implementation.
    '''
    def __init__(self, root):
        '''
        Initializations
        '''
        self.__root = root
        self.__right = self.__left = None
    
    # Getter Methods
    def getRoot(self):
        '''
        Returns the root value current subtree root.
        '''
        return self.__root
    
    def getRight(self):
        '''
        Returns the right child refrence of current subtree root.
        '''
        return self.__right
    
    def getLeft(self):
        '''
        Returns the left child refrence of current subtree root.
        '''
        return self.__left

    def hasLeft(self):
        '''
        Returns True if the recievers left child is not Null.
        '''
        if self.__left:
            return True
        return False
    
    def hasRight(self):
        '''
        Returns True if the recievers right child is not Null.
        '''
        if self.__right:
            return True
        return False
    
    def findSmallest(self):
        '''
        Find the minimum element in the tree
        Returns: None if tree is None, otherwise a number
        '''
        return self._findSmallest(self)
    
    def _findSmallest(self, currentNode):
        '''
        findSmallest helper function.
        '''
        if currentNode:
            minKey = currentNode.getRoot()

            if currentNode.getRight():
                minRight = self._findSmallest(currentNode.getRight())
                minKey = min(minRight, minKey)

            if currentNode.getLeft():
                minLeft = self._findSmallest(currentNode.getLeft())
                minKey = min(minLeft, minKey)

            return minKey
        else:
            # If no tree exists
            return None
    
    def findLargest(self):
        '''
        Find the maximum element in the tree
        Returns: None if tree is None, otherwise a number
        '''       
        return self._findLargest(self)
    
    def _findLargest(self, currentNode):
        '''
        FindLargest helper function
        '''
        if currentNode:
            maxKey = currentNode.getRoot()

            if currentNode.getLeft():
                maxLeft = self._findLargest(currentNode.getLeft())
                maxKey = max(maxKey, maxLeft)
            
            if currentNode.getRight():
                maxRight = self._findLargest(currentNode.getRight())
                maxKey = max(maxKey, maxRight)
            
            return maxKey  
        else:
            return None
    
    def range(self):
        '''
        Finds the range of key numbers in the Bianary Tree. Returns None if no items in tree
        '''
        if self.__root:
            return self._findLargest(self) - self._findSmallest(self)
        else:
            return None
    
    def contains(self, root):
        '''
        Returns True iff the reciever contains anObject in its root or its child subtrees.
        Traverses the whole tree O(n) recurssively.
        '''
        found = False

        if self.getRoot() == root:
            found = True
        
        if self.hasLeft():
            result = self.getLeft().contains(root)
            if result:
                found = True
        
        if self.hasRight():
            result = self.getRight().contains(root)
            if result:
                found = True
        
        return found
    
    def inorder(self):
        '''
        Gets a list of the inorder traversal of tree and returns this list.
        '''
        lst = []
        self._inorder(lst, self)
        return lst
    
    def _inorder(self, lst, currentNode):
        '''
        inorder() helper function.
        '''
        if currentNode:
            self._inorder(lst, currentNode.getLeft())
            lst.append(currentNode.getRoot())
            self._inorder(lst, currentNode.getRight())

    def preorder(self):
        '''
        Gets a list of the preorder traveral of the tree and returns this list.
        '''
        lst = []
        self._preorder(lst, self)
        return lst
    
    def _preorder(self, lst, currentNode):
        '''
        preorder() helper function.
        '''
        if currentNode:
            lst.append(currentNode.getRoot())
            self._preorder(lst, currentNode.getLeft())
            self._preorder(lst, currentNode.getRight())

    def postorder(self):
        '''
        Gets a list of the postorder traveral of the tree and returns this list.
        '''
        lst = []
        self._postorder(lst, self)
        return lst
    
    def _postorder(self, lst, currentNode):
        '''
        postorder() helper function.
        '''
        if currentNode:
            self._postorder(lst, currentNode.getLeft())
            self._postorder(lst, currentNode.getRight())
            lst.append(currentNode.getRoot())
    
    # Setter Methods
    def setRight(self, new):
        '''
        Sets a new rigth child of reciever.
        '''
        self.__right = new

    def setLeft(self, new):
        '''
        Sets a new left child of the reciever.
        '''
        self.__left = new

    def setRoot(self, new):
        '''
        Sets a new root for the current bianary tree.
        '''
        self.__root = new

    def insertRight(self, key):
        '''
        Creates a new BianaryTree and installs it as the right child of the current node.
        Make the original right subtree, if it exists then make it the right child of the new
        right child.
        '''
        if not self.__right:
            self.__right = BianaryTree(key)
        else:
            newNode = BianaryTree(key)
            newNode.setRight(self.__right)
            self.__right = newNode

    def insertLeft(self, key):
        '''
        Creates a new BianaryTree and installs it as the left child of the current node.
        Make the original left subtree, if it exists then make it the left child of the new
        left child.
        '''
        if not self.__left:
            self.__left = BianaryTree(key)
        else:
            newNode = BianaryTree(key)
            newNode.setLeft(self.__left)
            self.__left = newNode
    
    def clear(self):
        '''
        Makes reciever tree and all subtrees on its left and right child empty.
        Keeps the value of the root node however.
        '''
        self.__right = self.__left = None

    # String Methods
    def _strHelper(self):
        '''
        Returns list of strings, total width of the tree, position of the middle node and the height
        '''
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.__root
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.__root
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
        Returns a printed representation of the tree starting from a given root node
        '''
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result

# Build Tree Function
def buildTree(preorder, inorder):
    '''
    Recurssively builds a copy of a tree based on given inorder and preorder lists.
    '''
    if not preorder or not inorder:
        return None
    
    currentRoot = preorder.pop(0)
    rootIndex = inorder.index(currentRoot)

    tree = BianaryTree(currentRoot)
    
    tree.setLeft(buildTree(preorder, inorder[:rootIndex]))
    tree.setRight(buildTree(preorder, inorder[rootIndex+1:]))

    return tree
    

#### TESTING ####
def main():
    tree = BianaryTree(1)

    tree.insertRight(5)
    tree.insertRight(10)
    tree.getRight().insertLeft(11)
    tree.insertLeft(2)
    tree.insertRight(100)
    tree.getLeft().insertLeft(90)
    tree.getLeft().insertRight(8)
    tree.getRight().getRight().insertLeft(999)
    #tree.clear()

    inn = tree.inorder()
    pre = tree.preorder()
    post = tree.postorder()
    print(post)
    
    print(tree)

    tree2 = buildTree(pre, inn)

    print(tree2)

if __name__ == '__main__':
    main()