class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    def stringToListNode(self, input):
        # Generate list from the input
        numbers = [int(s) for s in input.split()]
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
    
input_string = input("Enter a list of numbers separated by space: ")
val = int(input("Enter a value to remove: "))