def convert(s):
    denary=0
    for index in range(len(s)):
        digit = s[-index-1]
        if s[-index-1] not in range(9):
            digit = ["A","B","C","D","E","F"].index(s[-index-1])+10
        denary = denary + int(digit)*(16**index)
    return denary
