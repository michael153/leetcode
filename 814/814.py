# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def solve(cur):
            if not cur:
                return True
            l = solve(cur.left)
            r = solve(cur.right)
            if l:
                cur.left = None
            if r:
                cur.right = None
            return l and r and cur.val == 0
        
        ptr = root
        solve(ptr)
        
        return root
