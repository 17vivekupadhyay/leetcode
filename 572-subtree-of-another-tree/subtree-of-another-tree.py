# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False

        def same(p,q):
            if q == None and p == None:
                return True
            
            if q == None or p == None:
                return False
            
            if q.val != p.val:
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
                
        if same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        