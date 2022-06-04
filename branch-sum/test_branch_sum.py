import unittest
import branch_sum

class TestBranchSum(unittest.TestCase):
    def test_branch_sum(self):
        mybst = branch_sum.BST(1)
        subbst1 = branch_sum.BST(2)
        subbst2 = branch_sum.BST(3)
        bottombst1 = branch_sum.BST(4)
        bottombst2 = branch_sum.BST(5)
        bottombst3 = branch_sum.BST(6)
        bottombst4 = branch_sum.BST(7)

        mybst.setLeft(subbst1)
        mybst.setRight(subbst2)

        subbst1.setLeft(bottombst1)
        subbst1.setRight(bottombst2)
        subbst2.setLeft(bottombst3)
        subbst2.setRight(bottombst4)

        print(branch_sum.branchSum(mybst))

if __name__ == "__main__":
    unittest.main()
