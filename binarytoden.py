def bin_den(bin_num):
    i1=0
    i2=1
    bin_list=[]
    while i1<len(bin_num):
        bin_char=int(bin_num[i1:i2])
        bin_list.append(bin_char)
        i1=i1+1
        i2=i2+1
    i3=len(bin_list)-1
    i4=0
    den_num=0
    while i3!=-1:
        den_num=(bin_list[i3])*(2**i4)+den_num
        i3=i3-1
        i4=i4+1
    return(den_num)


if __name__=="__main__":
    bin_den()
