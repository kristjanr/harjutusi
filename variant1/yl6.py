def list_sum(elements):
    if type(elements) != list:
        return None
    summa = 0
    for el in elements:
        try:
            summa += el
        except TypeError:
            continue
    return summa
