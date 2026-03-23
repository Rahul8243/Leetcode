class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If it's a leaf, check if remaining sum equals node value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recurse on children with reduced sum
        remaining = targetSum - root.val
        
        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )