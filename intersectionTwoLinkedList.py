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

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_A = headA
        curr_B = headB

        len_A = 0
        len_B = 0
        while curr_A is not None:
            curr_A = curr_A.next
            len_A += 1
        while curr_B is not None:
            curr_B = curr_B.next
            len_B += 1

        if len_A > len_B:
            diff = len_A - len_B
            k = 0
            curr_A = headA
            curr_B = headB
            while k < diff:
                curr_A = curr_A.next
                k += 1
        elif len_B > len_A:
            diff = len_B - len_A
            k = 0
            curr_A = headA
            curr_B = headB
            while k < diff:
                curr_B = curr_B.next
                k += 1
        else:
            curr_A = headA
            curr_B = headB

        while curr_A is not None and curr_B is not None:
            if curr_A.val == curr_B.val:
                return curr_A
            else:
                curr_A = curr_A.next
                curr_B = curr_B.next
        return None


def main():
    sol = Solution()
    head1 = ListNode(3)
    #new1 = ListNode(2)
    #new2 = ListNode(3)
    #new3 = ListNode(4)
    #new4 = ListNode(5)
    #head1.next = new1
    #new1.next = new2
    #new2.next = new3
    #new3.next = new4

    head2 = ListNode(2)
    new11 = ListNode(3)
    #new21 = ListNode(3)
    #new31 = ListNode(4)
    #new41 = ListNode(5)
    head2.next = new11
    #new11.next = new21
    #new21.next = new31
    #new31.next = new41

    # sol.printTree(head1)
    # sol.printTree(head2)

    output = sol.getIntersectionNode(head1, head2)
    print output
    sol.printTree(output)
if __name__ == '__main__':
    main()