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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        prev_node = None
        while curr_node is not None:
            if prev_node is not None:
                if curr_node.val == prev_node.val:
                    next_node = curr_node.next
                    prev_node.next = next_node
                    curr_node.next = None
                    curr_node = next_node
                else:
                    prev_node = curr_node
                    curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return head


def main():
    sol = Solution()
    head = ListNode(1)
    new1 = ListNode(1)
    new2 = ListNode(2)
    new3 = ListNode(3)
    new4 = ListNode(3)
    head.next = new1
    new1.next = new2
    new2.next = new3
    new3.next = new4
    # sol.printTree(head)

    output = sol.deleteDuplicates(head)
    sol.printTree(output)

if __name__ == '__main__':
    main()