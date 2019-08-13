"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mp = {}
        copy = None
        if head:
            copy = Node(None, None, None)
        ptr = copy
        ref = head
        while ref:
            ptr.val = ref.val
            if ref.next:
                ptr.next = Node(None, None, None)
            mp[ref] = ptr
            ptr = ptr.next
            ref = ref.next

        ptr = copy
        ref = head
        while ref:
            if ref.random:
                ptr.random = mp[ref.random]
            ptr = ptr.next
            ref = ref.next

        return copy
