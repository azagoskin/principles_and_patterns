def lre_wrong(in_str: str) -> str:
    if not in_str:
        return ''

    res = [in_str[0], '1']

    for i in range(1, len(in_str)):
        if in_str[i-1] != in_str[i]:
            if res[-1] == '1':
                res.pop()
            res.append(in_str[i])
            res.append('1')
        else:
            res[-1] = str(int(res[-1]) + 1)

    if res[-1] == '1':
        res.pop()

    return ''.join(res)


def lre_correct(in_str: str) -> str:
    current_ch = None
    count = 1
    out_str = []

    for ch in list(in_str) + [None]:
        if not current_ch:
            current_ch = ch
        elif ch != current_ch:
            out_str.append(current_ch)
            current_ch = ch

            if count != 1:
                out_str.append(str(count))
            count = 1
        else:
            count += 1

    return ''.join(out_str)


s = 'AAAADDDCCBBBFFFA'
print(lre_wrong(s))
print(lre_correct(s))