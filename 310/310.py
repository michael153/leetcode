class Solution(object):
    
    def findLeaves(self, adjList):
        leaves = []
        for node in adjList:
            if len(adjList[node]) == 1:
                leaves.append(node)
        return leaves
    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        leaves = self.findLeaves(adj)
        while len(adj) > 2:
            for node in leaves:
                if len(adj[node]) == 1:
                    adj[adj[node][0]].remove(node)
                    adj.pop(node, None)
            leaves = self.findLeaves(adj)
        return [node for node in adj]
