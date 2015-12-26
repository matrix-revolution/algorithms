class Solution(object):
    def is_open(self, s):
        if s == '{' or s == '[' or s == '(':
            return True
        else:
            return False

    def match(self, st1, st2):
        if st1 == '{' and st2 == '}':
            return True
        elif st1 == '[' and st2 == ']':
            return True
        elif st1 == '(' and st2 == ')':
            return True
        else:
            return False

    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_str = len(s)
        valid = True
        if len_str % 2 != 0:
            return False
        stack = []

        for element in s:
            if self.is_open(element):
                stack.append(element)
            else:
                if len(stack) > 0:
                    val = stack.pop()
                    valid = valid and self.match(val, element)
        if len(stack) > 0:
            return False
        return valid


def main():
    sol = Solution()
    s = '{[}]'
    # s = '{[()]}'
    out = sol.is_valid(s)
    print out

if __name__ == '__main__':
    main()