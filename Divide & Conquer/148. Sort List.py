# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummy = ListNode()
            tail = dummy
            while head1 and head2:
                if head1.val <= head2.val:
                    tail.next, head1 = head1, head1.next
                else:
                    tail.next, head2 = head2, head2.next
                tail = tail.next
            tail.next = head1 or head2
            return dummy.next

        def divide(heado):
            if not heado or not heado.next: return heado
            slow, fast = heado, heado.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            head1 = divide(heado)
            head2 = divide(right)
            return merge(head1, head2)

        return divide(head)
