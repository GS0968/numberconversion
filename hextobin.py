def convert(s):
    stringlist=[]
    charlist=["A","B","C","D","E","F"]
    binarylist=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    hexstring=""
    for i in range(len(s)):
        char=s[i]
        try:
            char=int(char)
            stringlist.append(char)
        except ValueError:
            for counter in range(len(charlist)):
                if charlist[counter]==char:
                    counter+=10
                    stringlist.append(counter)
                    break
                else:
                    counter+=1
        i+=1
    for u in range(len(stringlist)):
        num=stringlist[u]
        hexchar=binarylist[num]
        hexstring=hexstring+hexchar
        u+=1
    return(hexstring)
