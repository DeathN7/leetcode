class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        p, q, curr, carry = l1, l2, dummyHead, 0
        while p or q or carry:
            if p:
                carry += p.val
                p = p.next
            if q:
                carry += q.val
                q = q.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return dummyHead.next
