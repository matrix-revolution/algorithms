# remove duplicate and print lexicographically


def small_lexico(s, o):
    out = []
    i = 0
    while i < len(s) - len(o):
        pos = ''
        for n in range(i, len(s)):
            if s[n] not in pos:
                pos = pos+s[n]
        out.append(pos)
        i = i+1
    return sorted(out)


def remove_duplicate_letters(s):
    letters_dic = {}
    for letter in s:
        if letter not in letters_dic.keys():
            letters_dic[letter] = 1
        else:
            print('do nothing')
    output = sorted(letters_dic.keys())
    return output


def main():
    # s = 'bcabc'
    s = 'cbacdcbc'
    output = remove_duplicate_letters(s)
    str_out = ''
    for ch in output:
        str_out = str_out + ch
    sol = small_lexico(s, str_out)
    print sol[0]


if __name__ == '__main__':
    main()

