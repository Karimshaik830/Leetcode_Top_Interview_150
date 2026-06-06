class Solution:

    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        def find_left_node(head, left):

            dummy = ListNode(0)
            dummy.next = head

            prev = dummy
            curr = head

            pos = 1

            while pos < left:

                prev = curr
                curr = curr.next

                pos += 1

            return prev, curr

        def reverse_k_nodes(head, k):

            prev = None
            curr = head

            count = 0

            while curr and count < k:

                next_node = curr.next

                curr.next = prev

                prev = curr

                curr = next_node

                count += 1

            return prev, head, curr

        before_left, left_node = find_left_node(head, left)

        k = right - left + 1

        reversed_head, reversed_tail, after_right = reverse_k_nodes(
            left_node,
            k
        )

        before_left.next = reversed_head

        reversed_tail.next = after_right

        dummy = ListNode(0)
        dummy.next = head

        return dummy.next if left != 1 else reversed_head