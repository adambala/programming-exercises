# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        blank_node = ListNode()
        l3_pointer = l3 = ListNode()

        carry = 0
        while True:
            l3_pointer.val = l1.val + l2.val + carry
            
            carry = 0
            if (l3_pointer.val >= 10):
                carry = 1
                l3_pointer.val -= 10

            if (l1.next is None) and (l2.next is None):
                if (carry > 0):
                    l3_pointer.next = ListNode(val=carry)
                break
            elif (l1.next is None):
                l1, l2 = blank_node, l2.next
            elif (l2.next is None):
                l1, l2 = l1.next, blank_node
            else:
                l1, l2 = l1.next, l2.next
            
            l3_pointer.next = ListNode(val=carry)
            l3_pointer = l3_pointer.next
            
        return l3
