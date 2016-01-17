class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.idx = None
        self.min_val = []
        self.min_idx = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.min_stack.append(x)
        if self.idx is None:
            self.idx = 0
        else:
            self.idx += 1
        if self.min_idx is None or self.min_idx < 0:
            self.min_val.append(x)
            self.min_idx = 0
        else:
            if self.min_idx >= 0 and x <= self.min_val[self.min_idx]:
                self.min_val.append(x)
                self.min_idx += 1

    def pop(self):
        """
        :rtype: nothing
        """
        pop_ele = self.min_stack[self.idx]
        del self.min_stack[self.idx]
        self.idx -= 1
        if self.min_idx >= 0 and self.min_val[self.min_idx] == pop_ele:
            del self.min_val[self.min_idx]
            self.min_idx -= 1

    def top(self):
        """
        :rtype: int
        """
        val = self.min_stack[self.idx]
        return val

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_idx < 0:
            return None
        else:
            return self.min_val[self.min_idx]


def main():
    min_stack = MinStack()
    min_stack.push(6)
    min_stack.push(9)
    min_stack.push(7)
    min_stack.push(3)
    min_stack.pop()
    min_stack.pop()
    min_stack.pop()
    min_stack.pop()
    print(min_stack.getMin())



if __name__ == '__main__':
    main()

