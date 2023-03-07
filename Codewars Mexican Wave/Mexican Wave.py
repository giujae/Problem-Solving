def wave(people):
    word = list(people)
    lst = []
    for i in range(len(word)):
        if word[i] != ' ':
            word[i] = word[i].upper()
            lst.append(''.join(word))
            word[i] = word[i].lower()
        else:
            word[i] = ' '
    return lst