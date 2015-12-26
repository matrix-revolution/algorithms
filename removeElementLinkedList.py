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

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr_node = head
        prev_node = None
        while curr_node is not None:
            if curr_node.val == val:
                if prev_node is not None:
                    next_node = curr_node.next
                    prev_node.next = next_node
                    curr_node.next = None
                    curr_node = next_node
                else:
                    head = curr_node.next
                    curr_node.next = None
                    curr_node = head
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return head



def main():
    sol = Solution()
    val = 6
    head1 = ListNode(1)
    new1 = ListNode(2)
    new2 = ListNode(6)
    new3 = ListNode(3)
    new4 = ListNode(4)
    new5 = ListNode(5)
    new6 = ListNode(6)
    head1.next = new1
    new1.next = new2
    new2.next = new3
    new3.next = new4
    new4.next = new5
    new5.next = new6
    output = sol.removeElements(head1, val)
    sol.printTree(output)
if __name__ == '__main__':
    main()