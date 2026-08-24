# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        result = []

        def postorder(temp):
            if temp is None: return 

            postorder(temp.left)
            postorder(temp.right)
            result.append(temp.val)

        postorder(root)
        return result