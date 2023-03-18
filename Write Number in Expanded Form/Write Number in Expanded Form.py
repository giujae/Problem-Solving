def expanded_form(num):
    lst = []
    for i in range(len(list(str(num)))):
        lst.append((num % 10) * (10 ** i))
        num = num // 10
    lst = lst[::-1]
    result = []
    for i in lst:
        if i != 0:
            result.append(i)
    return ' + '.join(map(str, result))