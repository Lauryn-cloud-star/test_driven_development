def tax(earnings):
    if earnings < 12000:
        return 0
    elif earnings <= 36000:
        return earnings * 0.20
    else:
        return earnings * 0.40
    

"""def tax(earnings):
    if earnings <= 12000:
        return 0
    elif earnings <= 36000:
        return (earnings - 12000) * 0.20
    else:
        return (36000 - 12000) * 0.20 + (earnings - 36000) * 0.40"""