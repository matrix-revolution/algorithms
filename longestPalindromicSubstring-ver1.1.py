class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        go_left = -1
        go_right = -1
        max_len = -1
        max_str = ''
        len_s = len(s)
        k = 0
        if len_s <= 1:
            return s

        while k < len_s:
            go_left = k
            go_right = k+1
            while go_left >= 0 and go_right < len_s:
                go_left = k-1
                prev_s = go_left
                prev_e = go_right
                if go_left >= 0 and ord(s[go_left]) == ord(s[go_right]):
                    new_len = go_right - go_left + 1
                    new_str = s[go_left:go_right + 1]
                    go_left -= 1
                    go_right += 1
                    if new_len > max_len:
                        max_len = new_len
                        max_str = new_str

                elif ord(s[k]) == ord(s[go_right]):
                    go_left = k
                    new_len = go_right - go_left + 1
                    new_str = s[go_left:go_right + 1]
                    go_left -= 1
                    go_right += 1
                    if new_len > max_len:
                        max_len = new_len
                        max_str = new_str
                else:
                    break
            if go_right == len_s - 1:
                break
            k += 1
        return max_str


def main():
    sol = Solution()
    #s = '13133123'
    #s = '1213312133'
    s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" \
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    print(len(s))
    output = sol.longestPalindrome(s)
    print len(output)
    print output


if __name__ == '__main__':
    main()
