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
        digit = 0
        for j in range(len(val1)):
            digit = digit + int(list(val1)[-j-1])*(2**j)
        if digit >= 10:
            chars = ["A","B","C","D","E","F"]
            Char = chars[digit-10]
        else:
            Char = str(digit)
        final_val = Char + final_val
        i = i - 4

    return(final_val)
