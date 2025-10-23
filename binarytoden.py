def BinToDen(A):
    Denary = 0
    for i in range(len(A)):
        Denary = Denary + (2**i)*int(A[-i-1])
    return Denary
