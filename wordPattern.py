class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        val_store_str = {}
        val_store_pat = {}
        str_array = str.split(' ')

        for ch in pattern:
            val_store_str[ch] = 0

        for ele in str_array:
            val_store_pat[ele] = 0
        print val_store_pat

        len_str = len(str_array)
        len_pattern = len(pattern)

        if len_str != len_pattern:
            return False

        for i in range(0, len_str):
            val_str = str_array[i]
            val_pattern = pattern[i]
            if val_store_str[val_pattern] != 0:
                if val_store_str[val_pattern] != val_str:
                    return False
            else:
                val_store_str[val_pattern] = val_str

        for j in range(0, len_pattern):
            val_pattern = pattern[j]
            val_str = str_array[j]
            if val_store_pat[val_str] != 0:
                if val_store_pat[val_str] != val_pattern:
                    return False
            else:
                val_store_pat[val_str] = val_pattern

        return True






def main():
    pattern = 'abba'
    str = 'dog dog dog dog'
    new_obj = Solution()
    output = new_obj.wordPattern(pattern, str)
    print output

if __name__ == '__main__':
    main()