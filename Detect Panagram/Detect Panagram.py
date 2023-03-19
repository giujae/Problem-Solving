def is_pangram(s):
    lst = list(set(list(s.lower())))
    print(lst)
    removed = []
    for i in lst:
        if i.isalpha() == True and i != ' ':
            removed.append(i)
    if len(removed) == 26:
        return True
    else:
        return False