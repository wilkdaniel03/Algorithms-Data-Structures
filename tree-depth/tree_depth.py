class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

def treeDepthUsingIteration(root):
    depthSums = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        depthSums += 1
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return depthSums

def treeDepthUsingRecursion(node, depth = 0):
    if node is None:
        return 0
    return treeDepthUsingRecursion(node.left, depth + 1) + treeDepthUsingRecursion(node.right, depth + 1)
