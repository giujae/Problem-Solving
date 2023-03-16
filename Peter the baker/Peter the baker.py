def cakes(recipe, available):
    lst = []
    for ch in recipe.keys():
        if ch not in available:
            return 0
        else:
            lst.append((available.get(ch)//recipe.get(ch)))
    return min(lst)