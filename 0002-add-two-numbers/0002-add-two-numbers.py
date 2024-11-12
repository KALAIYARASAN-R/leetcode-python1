class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 is not None or l2 is not None or carry!=0:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            cur_sum = sum%10
            carry = sum//10
            current.next=ListNode(cur_sum)
            current = current.next
        return dummy.next