def currency_exchange(kursid):
    if not kursid:
        return None
    return list(sorted(kursid.items(), key=lambda k: k[1]))[0][0]
