# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Dummy node to start the result list
        current = dummy     # Pointer to build the new list
        carry = 0           # Carry for sums >= 10

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Value from l1, or 0 if None
            val2 = l2.val if l2 else 0  # Value from l2, or 0 if None

            # Add the values and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)  # Add node with the digit
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the head of the summed list
