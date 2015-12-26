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

    def find_middle(self, head):
        output = []
        one_step = head
        two_step = head

        if one_step is None:
            return [None, 0]
        if one_step.next is None:
            return [one_step, 1]
        if one_step.next.next is None:
            return [one_step.next, 2]

        len_list = 1
        while two_step.next is not None and two_step.next.next is not None:
            one_step = one_step.next
            two_step = two_step.next.next
            len_list += 2
        if two_step.next is not None and two_step.next.next is None:
            len_list += 1
        return [one_step, len_list]

    def reverseList(self, mid):
        head = mid.next
        current_node = head
        place_on_front = None
        top = None
        if head is None or head.next is None:
            return mid
        mid.next = None
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
        mid.next = head
        return mid

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        params = self.find_middle(head)
        mid = params[0]
        len_list = params[1]

        if len_list == 0:
            return True
        if len_list == 1:
            return True
        if len_list == 2:
            if head.val == head.next.val:
                return True
            else:
                return False

        first_pointer = head
        print 'first'
        self.printTree(first_pointer)
        second_pointer = self.reverseList(mid)
        print 'second'
        self.printTree(second_pointer)
        if len_list % 2 == 0:
            stop = second_pointer.next
        else:
            stop = second_pointer
        second_pointer = second_pointer.next

        while first_pointer is not stop and second_pointer is not None:
            if first_pointer.val == second_pointer.val:
                first_pointer = first_pointer.next
                second_pointer = second_pointer.next
            else:
                return False
        return True


def main():
    sol = Solution()
    head = ListNode(1)
    new1 = ListNode(0)
    new2 = ListNode(0)
    head.next = new1
    new1.next = new2
    sol.printTree(head)
    output = sol.find_middle(head)
    print 'params'
    print output[0].val
    print output[1]
    out = sol.isPalindrome(head)
    print out

if __name__ == '__main__':
    main()
