# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        odd = head
        if odd and odd.next:
            bridge = odd.next
        while ptr:
            if odd and odd.next and bridge:
                odd = bridge.next
                if bridge.next:
                    bridge.next = bridge.next.next
                    bridge = bridge.next
                    odd.next = ptr.next
                    ptr.next = odd
                else:
                    break
            else:
                break
            if ptr:
                odd = ptr.next
                ptr = ptr.next
            else:
                break
            
        return head
