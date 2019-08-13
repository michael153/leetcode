# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def traverse(node, path):
            if node.left:
                path[node.left] = node
                traverse(node.left, path)
            if node.right:
                path[node.right] = node
                traverse(node.right, path)
                
        def reversePath(root, target, path):
            node = target
            ret = [node]
            while node != root:
                node = path[node]
                ret.append(node)
            return ret
                
        parents = {}
        traverse(root, parents)
        pPath = reversePath(root, p, parents)
        qPath = reversePath(root, q, parents)
        visited = {}
        for node in pPath:
            visited[node] = True
        for node in qPath:
            if node in visited:
                return node            
