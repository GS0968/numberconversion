import hextobin
import binarytoden

def convert(s):
    value=hextobin.convert(s)
    denaryvalue=binarytoden.bin_den(value)
    return denaryvalue
