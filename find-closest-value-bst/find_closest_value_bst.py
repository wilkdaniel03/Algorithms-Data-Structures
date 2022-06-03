class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, tree):
        self.left = tree

    def set_right(self, tree):
        self.right = tree

    def get_value(self):
        return self.value

class FindClosestValueBst:
    def find(self, tree, target, closest):
        if tree is None:
            return closest
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            return self.find(tree.left, target, closest)
        elif target > tree.value:
            return self.find(tree.right, target, closest)
        else:
            return closest

    def another_find(self, tree, target, closest):
        current_node = tree
        while current_node is not None:
            if abs(target - closest) > (target - current_node.value):
                closest = current_node.value
            if target < current_node.value:
                current_node = current_node.left
            elif target > current_node.value:
                current_node = current_node.right
            else:
                return closest
        return closest
