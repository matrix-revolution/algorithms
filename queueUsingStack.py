class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_v = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.list_v.append(x)

    def pop(self):
        """
        :rtype: nothing
        """

        if len(self.list_v) == 1 or len(self.list_v) == 0:
            self.list_v = []
        else:
            for i in range(0, len(self.list_v)-1):
                temp = self.list_v[i+1]
                self.list_v[i] = temp
            del self.list_v[len(self.list_v) - 1]

    def peek(self):
        """
        :rtype: int
        """
        front = self.list_v[0]
        return front

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.list_v) == 0:
            return True
        else:
            return False


def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    peek_v = queue.peek()
    print(peek_v)
    queue.pop()
    queue.pop()
    if queue.empty():
        print 'queue is empty'
    else:
        print 'not empty'

if __name__ == '__main__':
    main()
