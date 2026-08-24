# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return None
        temp = root
        lst = []

        def inorder(temp):
            if not temp: return None

            inorder(temp.left)
            lst.append(temp.val)
            inorder(temp.right)
        inorder(root)
        return lst == sorted(set(lst))