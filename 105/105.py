# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        rank = {}                       
        inorder_index = {}
        for i, val in enumerate(preorder):
            rank[val] = i
        for i, val in enumerate(inorder):
            inorder_index[val] = i
       
        def solve(l, r):
            """l, r => inclusive, exclusive"""
            if r - l <= 0:
                return None
            if r - l == 1:
                return TreeNode(inorder[l])
            index = -1
            for p in preorder:
                if inorder_index[p] >= l and inorder_index[p] < r:
                    index = inorder_index[p]
                    break
            preorder.remove(p)
            root = TreeNode(inorder[index])
            root.left = solve(l, index)
            root.right = solve(index + 1, r)
            return root
            
        tree = solve(0, len(inorder))
        return tree

            
                
         
                
                    
            
        