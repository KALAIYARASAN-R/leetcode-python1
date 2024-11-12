# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#def maxDepth(root: TreeNode) -> int:
    # Base case: if the root is None (empty tree), the depth is 0
   # if not root:
       # return 0
    
    # Recursively calculate the depth of left and right subtrees
    #left_depth = maxDepth(root.left)
    #right_depth = maxDepth(root.right)
    
    # The depth of the current tree is the max depth of the subtrees + 1 for the current node
    #return max(left_depth, right_depth) + 1

# Example usage:
#if __name__ == "__main__":
    # Create a simple binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    
   # root = TreeNode(1)
    #root.left = TreeNode(2)
    #root.right = TreeNode(3)
    #root.left.left = TreeNode(4)
    #root.left.right = TreeNode(5)
    
    # Get the maximum depth of the tree
    #depth = maxDepth(root)
    #print("Maximum depth of the tree:", depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left) ,  self.maxDepth(root.right) )