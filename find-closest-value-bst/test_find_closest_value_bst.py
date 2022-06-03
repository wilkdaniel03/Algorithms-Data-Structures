import unittest
import find_closest_value_bst as fcvb

class TestFindClosestValueBst(unittest.TestCase):
    def test_find(self):
        my_fcvb = fcvb.FindClosestValueBst()
        main_tree = fcvb.BST(10)
        sub_tree1 = fcvb.BST(5)
        sub_tree2 = fcvb.BST(15)
        bottom_tree_1 = fcvb.BST(2)
        bottom_tree_2 = fcvb.BST(5)
        bottom_tree_3 = fcvb.BST(13)
        bottom_tree_4 = fcvb.BST(22)

        main_tree.set_left(sub_tree1)
        main_tree.set_right(sub_tree2)
        sub_tree1.set_left(bottom_tree_1)
        sub_tree1.set_right(bottom_tree_2)
        sub_tree2.set_left(bottom_tree_3)
        sub_tree2.set_right(bottom_tree_4)

        result = my_fcvb.find(main_tree, 12, main_tree.get_value())
        print(f"Algorithm 1 -> {result}")

    def test_another_find(self):
        my_fcvb = fcvb.FindClosestValueBst()
        main_tree = fcvb.BST(10)
        sub_tree1 = fcvb.BST(5)
        sub_tree2 = fcvb.BST(15)
        bottom_tree_1 = fcvb.BST(2)
        bottom_tree_2 = fcvb.BST(5)
        bottom_tree_3 = fcvb.BST(13)
        bottom_tree_4 = fcvb.BST(22)

        main_tree.set_left(sub_tree1)
        main_tree.set_right(sub_tree2)
        sub_tree1.set_left(bottom_tree_1)
        sub_tree1.set_right(bottom_tree_2)
        sub_tree2.set_left(bottom_tree_3)
        sub_tree2.set_right(bottom_tree_4)

        result = my_fcvb.another_find(main_tree, 12, main_tree.get_value())
        print(f"Algorithm 2 -> {result}")

if __name__ == "__main__":
    unittest.main()
