def elements_sum(integer):
    if integer is None:
        return None
    return sum((i for i in range(integer + 1)))

