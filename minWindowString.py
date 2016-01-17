class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s = len(s)
        len_t = len(t)
        alpha = [0 for i in range(0, 256)]
        len_output = pow(2, 31)
        output = ''
        count = 0
        sequence = []
        start_idx = 0
        end_idx = 0
        for i in range(0, len_t):
            alpha[ord(t[i])] += 1

        for j in range(0, len_s):
            if s[j] in alpha:
                if alpha[s[j]] != -1:
                    start_idx += 1
                else:
                    count += 1
                alpha[s[j]] = j
                sequence.append(j)
                end_idx = len(sequence) - 1
            if count == len_t:
                new_len_output = sequence[end_idx] - sequence[start_idx] + 1
                new_output = s[sequence[start_idx]:sequence[end_idx] + 1]
                if new_len_output < len_output:
                    len_output = new_len_output
                    output = new_output
                count -= 1
                start_idx += 1

        return output


def main():
    sol = Solution()
    #s = 'ADOBECODEBANC'
    s = 'babc'
    t = 'abc'
    output = sol.minWindow(s, t)
    print(output)

if __name__ == '__main__':
    main()