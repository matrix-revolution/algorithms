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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        new_val = next_node.val
        node.val = new_val
        node.next = next_node.next


def main():
    sol = Solution()
    head = ListNode(1)
    node = head
    i = 2
    while i <= 5:
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
        i += 1
    node.next = None
    sol.deleteNode(head.next.next)
    sol.printTree(head)

if __name__ == '__main__':
    main()