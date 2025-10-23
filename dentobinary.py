def DenToBin(A):
    den=int(A)
    Binary = str(den%2)
    while int(den/2)!=0:
        den = int(den/2)
        Binary = str(den%2) + Binary
    return Binary
