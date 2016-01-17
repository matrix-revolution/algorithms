class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip().rstrip()
        start_pointer = -1
        end_pointer = -1
        space = ord(' ')
        len_str = len(s)
        k = 0
        if len_str <= 0:
            return 0
        while k < len_str:
            if ord(s[k]) == space:
                start_pointer = -1
                end_pointer = -1
            else:
                if start_pointer == -1:
                    start_pointer = k
            k += 1
        end_pointer = k-1
        return end_pointer - start_pointer + 1


def main():
    sol = Solution()
    s = 'Hello World'
    output = sol.lengthOfLastWord(s)
    print(output)

if __name__ == '__main__':
    main()
