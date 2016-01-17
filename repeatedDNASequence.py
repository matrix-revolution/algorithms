class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        total_len = 10
        len_s = len(s)
        if len_s < total_len:
            return []
        i = 0
        dict_store = {}
        val = ''
        while i < len_s:
            k = i
            val = ''
            while k < (total_len + i) <= len_s:
                val += s[k]
                k += 1
            if val != '':
                if val not in dict_store:
                    dict_store[val] = 1
                else:
                    dict_store[val] += 1
            else:
                break
            i += 1
        output = []
        for key in dict_store:
            if dict_store[key] >= 2:
                output.append(key)
        return output


def main():
    sol = Solution()
    #s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    s = "AAAAAAAAAAA"
    output = sol.findRepeatedDnaSequences(s)
    print(output)

if __name__ == '__main__':
    main()