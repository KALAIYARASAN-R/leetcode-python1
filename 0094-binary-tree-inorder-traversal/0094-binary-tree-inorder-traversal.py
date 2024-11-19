# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def f(root):
            if root is None:
                return
            f(root.left)    
            ans.append(root.val)
            f(root.right)
        f(root)
        return ans    
        