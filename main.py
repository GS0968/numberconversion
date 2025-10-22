import binarytoden
import dentobinary
import dentohex
import binarytohex
import hextobin
import hextoden

def main():
    fromconvert=input("The number system you want to convert from: (D|B|H)").upper()
    toconvert=input("The number system you want to convert to: (D|B|H)").upper()
    value=input("Value to convert: ")
    match fromconvert:
        case "D":
            match toconvert:
                case "D":
                    print(value)
                case "H":
                    print(dentohex.convert(value))
                case "B":
                    print(dentobinary.DenToBin(value))
                case _:
                    raise ValueError
        case "B":
            match toconvert:
                case "D":
                    print(binarytoden.bin_den(value))
                case "H":
                    print(binarytohex.bintohex(value))
                case "B":
                    print(value)
                case _:
                    raise ValueError
        case "H":
            match toconvert:
                case "D":
                    print(hextoden.convert(value))
                case "H":
                    print(value)
                case "B":
                    print(hextobin.convert(value))
                case _:
                    raise ValueError
        case _:
            raise ValueError
 



if __name__=="__main__":
    main()
