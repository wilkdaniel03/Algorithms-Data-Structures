class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getValue(self):
        return self.value

def branchSum(root):
    sums = []
    currentRunningSum(root, 0, sums)
    return sums

def currentRunningSum(node, currentSum, sums):
    if node is None:
        return

    currentSum = node.getValue() + currentSum
    if node.left is None and node.right is None:
        sums.append(currentSum)
        return

    currentRunningSum(node.left, currentSum, sums)
    currentRunningSum(node.right, currentSum, sums)
