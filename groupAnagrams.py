class Solution(object):
    def valid_anagram(self, s, t):
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

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        while len(strs) > 0:
            s = strs[0]
            inner_list = []
            new_list = []
            inner_list.append(s)
            for i in range(1, len(strs)):
                t = strs[i]
                if self.valid_anagram(s, t):
                    inner_list.append(t)
                else:
                    new_list.append(t)
            inner_list.sort()
            output.append(inner_list)
            strs = new_list
        return output


def main():
    sol = Solution()
    strs = ['ate', 'tan', 'bat', 'eat', 'nat', 'tea']
    out = sol.groupAnagrams(strs)
    print(out)

if __name__ == '__main__':
    main()