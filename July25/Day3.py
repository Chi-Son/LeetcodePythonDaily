class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next    
            curr.next = prev          
            prev = curr               
            curr = next_node

        return prev 
    def create_linked_list(values):
        head = ListNode(values[0])
        current = head
        for v in values[1:]:
            current.next = ListNode(v)
            current = current.next
        return head
    def print_linked_list(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")
        

head = Solution.create_linked_list([1, 2, 3, 4])
Solution.print_linked_list(head)
solution = Solution()
reversed_head = solution.reverseList(head)
Solution.print_linked_list(reversed_head)
