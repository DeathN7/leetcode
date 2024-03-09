class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def stringToListNode(self, input):
        # Generate list from the input
        numbers = json.loads(input)

        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr
    
    def listNodeToString(self, node):
        if not node:
            return "[]"

        result = ""
        while node:
            result += str(node.val) + ", "
            node = node.next
        return "[" + result[:-2] + "]"
    
    def stringToListNode(self, input):
        # Generate list from the input
        numbers = json.loads(input)

        # Now convert that list into linked list
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr
    
print("Enter a list of numbers separated by space: ")
head = input()
head = Solution().stringToListNode(head)

ret = Solution().reverseList(head)
out = (Solution().listNodeToString(ret))
print(out)
