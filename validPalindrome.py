class Solution(object):

    def remove_extras(self, s):
        s = s.lstrip().rstrip()
        out = ''
        len_s = len(s)
        k = 0
        while k < len_s:
            if s[k].isalnum():
                out += s[k]
                k += 1
            else:
                k += 1
        return out

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        s = s.lower()
        len_s = len(s)
        left_pointer = 0
        right_pointer = len_s - 1
        while left_pointer < right_pointer:
            while left_pointer < len_s and not s[left_pointer].isalnum():
                left_pointer += 1
            while right_pointer >= 0 and not s[right_pointer].isalnum():
                right_pointer -= 1
            if left_pointer >= len_s or right_pointer < 0:
                return True
            if ord(s[left_pointer]) == ord(s[right_pointer]):
                left_pointer += 1
                right_pointer -= 1
            else:
                return False
        return True


def main():
    sol = Solution()
    s = 'A man, a plan, a canal: Panama'
    out = sol.isPalindrome(s)
    print(out)

if __name__ == '__main__':
    main()