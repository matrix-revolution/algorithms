class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        len_val = len(str)
        if len_val <= 0:
            return 0
        int_val = 0
        k = 0
        first_char = True
        placeholder = 0
        while k < len_val:
            curr = str[k]
            curr_ascii = ord(curr)
            if ord('0') <= curr_ascii <= ord('9'):
                curr_int = curr_ascii - ord('0')
                int_val = int_val*10 + curr_int
            elif first_char and curr_ascii == ord('-'):
                placeholder = -1
            elif first_char and curr_ascii == ord('+'):
                placeholder = 1
            else:
                break
            first_char = False
            k += 1
        if placeholder == -1:
            if int_val > pow(2, 31):
                int_val = pow(2, 31)
            return placeholder * int_val
        else:
            if int_val > pow(2, 31) - 1:
                int_val = pow(2, 31) - 1
            return int_val


def main():
    sol = Solution()
    val = '2147483648'
    out = sol.myAtoi(val)
    print(out)

if __name__ == '__main__':
    main()