def bin_den(bin):
    result = 0
    for index in range(len(bin)):
        result = result + int(list(bin)[-index-1])*(2**index)
    return result
