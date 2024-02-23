class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        current = head
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
input_string = input("nhap so: ")
input_list = input_string.split(',')
print("Ket Qua:", Solution().deleteDuplicates(input_list))