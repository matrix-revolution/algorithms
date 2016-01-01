# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def print_list(self, node):
        while node is not None:
            print(node.val)
            node = node.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = head
        next_node = None
        prev_node = None
        first_pointer = head
        second_pointer = head.next

        is_first = True

        while second_pointer is not None:
            next_node = second_pointer.next
            second_pointer.next = first_pointer
            first_pointer.next = next_node
            if prev_node is not None:
                prev_node.next = second_pointer
            prev_node = first_pointer
            if is_first:
                root = second_pointer
                is_first = False
            first_pointer = next_node
            if first_pointer is None:
                return root
            second_pointer = first_pointer.next
        return root


def main():
    sol = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(4)
    node2.next = node3
    #sol.print_list(head)
    output = sol.swapPairs(head)
    sol.print_list(output)

if __name__ == '__main__':
    main()