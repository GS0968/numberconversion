def convert(s):
    hexlist= ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hexstring=""
    remainder=[]
    quotient= int(int(s)/16)
    remainder.append(int(s)%16)
    while quotient!=0:
        remaindervalue=quotient%16
        quotient=int(quotient/16)
        remainder.append(remaindervalue)
    length=len(remainder)
    while length>0:
        length-=1
        remaindervalue=int(remainder[length])
        hexstring=hexstring+hexlist[remaindervalue]
    return hexstring
