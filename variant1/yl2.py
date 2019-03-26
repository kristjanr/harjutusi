def total_amount(amount, percentage, duration):
    total = amount
    if amount is None or percentage is None or duration is None:
        return None
    try:
        for _ in range(duration):
            interest = total * (percentage / 100)
            total = total + interest
    except TypeError:
        return None
    return total
