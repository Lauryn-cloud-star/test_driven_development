def tax(earnings):
    if earnings < 12000:
        return 0
    elif earnings <= 36000:
        return earnings * 0.20
    else:
        return earnings * 0.40