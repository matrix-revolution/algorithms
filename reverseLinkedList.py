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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        place_on_front = None
        top = None
        if head is None or head.next is None:
            return head
        while current_node is not None and current_node.next is not None:
            place_on_front = current_node.next
            next_node = place_on_front.next
            if top is not None:
                place_on_front.next = top
            else:
                place_on_front.next = current_node
            current_node.next = next_node
            top = place_on_front
        head = place_on_front
        return head


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
    out = sol.reverseList(head)
    sol.printTree(out)

if __name__ == '__main__':
    main()