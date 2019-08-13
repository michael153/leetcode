# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = 0
        ans = ListNode(0)
        carry = 0
        ptr = ans
        while not (l1 is None and l2 is None and carry == 0):
            dig1 = 0
            dig2 = 0
            newcarry = 0 
            if l1 is not None:
                dig1 = l1.val
                l1 = l1.next
            if l2 is not None:
                dig2 = l2.val
                l2 = l2.next
            if carry + dig1 + dig2 >= 10:
                newcarry = (carry + dig1 + dig2) / 10
            ptr.val = (carry + dig1 + dig2) % 10
            carry = newcarry
            if not (l1 is None and l2 is None and carry == 0):
                ptr.next = ListNode(0)
                ptr = ptr.next
        return ans
