from collections import Counter

def count(string):
    lst = list(string)
    num = Counter(lst)
    dict_num = dict(num)
    return dict_num