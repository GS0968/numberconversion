def main():
    Denary = int(input("Input the denary number you want to convert: "))
    print(f"The binary of {Denary} is: {DenToBin(Denary)}")

def DenToBin(A):
    A=int(A)
    Binary = str(A%2)
    while True:
        A = int(A/2)
        Binary = str(A%2) + Binary
        if int(A/2) == 0:
            break
    return(Binary)

if __name__=="__main__":
    main()
