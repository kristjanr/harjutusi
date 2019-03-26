def debt(apples, price, cash):
    cost = 0
    try:
        for i in range(1, apples + 1):
            cost += i * price
    except TypeError:
        return None
    return cost - cash
