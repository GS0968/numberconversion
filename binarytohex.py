def bintohex(Initial_value):
    remainder = len(Initial_value) % 4
    if remainder != 0:
        Initial_value = "0" * (4 - remainder) + Initial_value
    val1 = ""
    final_val = ""
    Char = ""
    i = len(Initial_value)
    while i > 0:
        val1 = Initial_value[i-4 : i]
        match val1:
            case "0000":
                Char="0"
            case"0001":
                Char="1"
            case"0010":
                Char="2"
            case"0011":
                Char="3"
            case "0100":
                Char="4"
            case"0101":
                Char="5"
            case"0110":
                Char="6"
            case"0111":
                Char="7"
            case"1000":
                Char="8"
            case"1001":
                Char="9"
            case"1010":
                Char="A"
            case"1011":
                Char="B"
            case"1100":
                Char="C"
            case"1101":
                Char="D"
            case"1110":
                Char="E"
            case"1111":
                Char= "F"
        final_val = Char + final_val
        i = i - 4

    return(final_val)


    
      

