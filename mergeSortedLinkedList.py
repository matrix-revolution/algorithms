# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def printTree(self, head):
        node = head
        while node is not None:
            print(node.val)
            node = node.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        head = l1
        prev_l1 = None
        next
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                prev_l1 = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                next_l2 = l2.next
                if prev_l1 is None:
                    head = l2
                    prev_l1 = head
                else:
                    prev_l1.next = l2
                    prev_l1 = prev_l1.next
                l2.next = l1
                l2 = next_l2

        if l1 is None:
            prev_l1.next = l2
        return head


def main():
    sol = Solution()
    head1 = ListNode(2)
    node = head1
    i = 4
    while i <= 10:
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
        i += 2
    node.next = None
    #sol.printTree(head1)

    # -------------------

    head2 = ListNode(1)
    node = head2
    i = 3
    while i <= 10:
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
        i += 2
    node.next = None
    #sol.printTree(head2)

    # -------------------

    output = sol.mergeTwoLists(head1, head2)
    sol.printTree(output)

if __name__ == '__main__':
    main()