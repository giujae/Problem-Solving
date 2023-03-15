def move_zeros(lst):
    Zero = []
    None_zero = []
    for i in lst:
        if i != 0:
            None_zero.append(i)
        else:
            Zero.append(i)
    for i in Zero:
        None_zero.append(i)
    return None_zero