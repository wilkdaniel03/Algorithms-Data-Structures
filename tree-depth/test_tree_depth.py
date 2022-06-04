import unittest
import tree_depth

class TestTreeDepth(unittest.TestCase):
    def test_tree_depth_iteration(self):
        mybst = tree_depth.BST(1)
        subbst1 = tree_depth.BST(2)
        subbst2 = tree_depth.BST(3)
        bottombst1 = tree_depth.BST(4)
        bottombst2 = tree_depth.BST(5)
        bottombst3 = tree_depth.BST(6)
        bottombst4 = tree_depth.BST(7)

        mybst.setLeft(subbst1)
        mybst.setRight(subbst2)

        subbst1.setLeft(bottombst1)
        subbst1.setRight(bottombst2)
        subbst2.setLeft(bottombst3)
        subbst2.setRight(bottombst4)

        print(tree_depth.treeDepthUsingIteration(mybst))

    def test_tree_depth_recursion(self):
        mybst = tree_depth.BST(1)
        subbst1 = tree_depth.BST(2)
        subbst2 = tree_depth.BST(3)
        bottombst1 = tree_depth.BST(4)
        bottombst2 = tree_depth.BST(5)
        bottombst3 = tree_depth.BST(6)
        bottombst4 = tree_depth.BST(7)

        mybst.setLeft(subbst1)
        mybst.setRight(subbst2)

        subbst1.setLeft(bottombst1)
        subbst1.setRight(bottombst2)
        subbst2.setLeft(bottombst3)
        subbst2.setRight(bottombst4)

        print(tree_depth.treeDepthUsingIteration(mybst))

if __name__ == "__main__":
    unittest.main()
