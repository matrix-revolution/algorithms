class Solution(object):
    def check_palindrome(self, s, start_pointer, end_pointer):
        output = True
        i = start_pointer
        j = end_pointer
        while i < j:
            if ord(s[i]) == ord(s[j]):
                i += 1
                j -= 1
            else:
                output = False
                break
        return output

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_pointer = -1
        end_pointer = -1
        max_str = ''
        max_len = 0
        len_s = len(s)
        k = 0
        j = 0
        if len_s <= 0:
            return max_str
        while j < len_s:
            k = j
            while k < len_s:
                if start_pointer == -1:
                    start_pointer = k
                if k == 0:
                    start_pointer = k
                else:
                    if ord(s[k]) == ord(s[start_pointer]):
                        if self.check_palindrome(s, start_pointer, k):
                            end_pointer = k
                            new_len = end_pointer - start_pointer + 1
                            new_str = s[start_pointer:end_pointer+1]
                        if new_len > max_len:
                            max_len = new_len
                            max_str = new_str
                            start_pointer = -1
                k += 1
            if end_pointer == len_s - 1:
                break
            j += 1

        return max_str


def main():
    sol = Solution()
    # s = '1213321233'
    s = '1213312133'
    output = sol.longestPalindrome(s)
    print(output)

if __name__ == '__main__':
    main()
