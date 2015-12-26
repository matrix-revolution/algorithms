class Solution(object):

    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        str1_store = {}
        str2_store = {}

        for ch in s:
            str1_store[ch] = 0
        for ch in t:
            str2_store[ch] = 0

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        count_t = 0
        count_s = 0

        for val_t in t:
            if str1_store[s[count_s]] != 0:
                if str1_store[s[count_s]] != val_t:
                    return False
            else:
                str1_store[s[count_s]] = val_t
            count_s += 1

        for val_s in s:
            if str2_store[t[count_t]] != 0:
                if str2_store[t[count_t]] != val_s:
                    return False
            else:
                str2_store[t[count_t]] = val_s
            count_t += 1

        return True


def main():
    new_obj = Solution()
    s = 'bar'
    t = 'foo'
    output = new_obj.is_isomorphic(s, t)
    print output

if __name__ == '__main__':
    main()