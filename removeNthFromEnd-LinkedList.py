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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr_node = head
        node_one = head

        i = 1
        if curr_node.next is None:
            if n == 1:
                return None
            else:
                return head
        while i <= n:
            if curr_node.next is not None:
                curr_node = curr_node.next
            else:
                if i == n:
                    head = head.next
                    return head
            i += 1
        node_two = curr_node
        prev_to_one = None
        while node_two is not None:
            prev_to_one = node_one
            node_one = node_one.next
            node_two = node_two.next

        remove_node = node_one
        if prev_to_one is not None:
            prev_to_one.next = remove_node.next
        else:
            head = remove_node.next
        remove_node.next = None

        return head


def main():
    sol = Solution()
    n = 2
    head = ListNode(1)
    node = head
    i = 2
    while i <= 5:
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
        i += 1
    node.next = None
    # sol.printTree(head)
    output = sol.removeNthFromEnd(head, n)
    sol.printTree(output)

if __name__ == '__main__':
    main()