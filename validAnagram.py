class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        store = [0 for i in range(0, 26)]

        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        for m in range(0, len_s):
            k = ord(s[m]) - ord('a')
            store[k] += 1

        for n in range(0, len_t):
            k = ord(t[n]) - ord('a')
            store[k] -= 1

        for j in range(0, len(store)):
            if store[j] >= 1:
                return False
        return True


def main():
    sol = Solution()
    s = 'rat'
    t = 'car'
    out = sol.isAnagram(s, t)
    print(out)

if __name__ == '__main__':
    main()