#Sp Formula File 06 Cycle, d=xx.07.2020

# Basic var's - 2^48, ~2^-16
toP48 = 281474976710656
toM16 = 0.000015

# Exit, x-search and list-bool&filter var's
ex = ""
us = 0
lf = ("exit", "ex", "eof", "EXIT", "EX", "EOF")
lb = 0

# Cycle of formula's tower
while lb == 0: 
    ex = input()
    # List-filter in ⇡FTC⇡
    if ex == lf[0]:
        lb = 1
    elif ex == lf[1]:
        lb = 1
    elif ex == lf[2]:
        lb = 1
    elif ex == lf[3]:
        lb = 1
    elif ex == lf[4]:
        lb = 1
    elif ex == lf[5]:
        lb = 1
    else:
        lb = 0

    if lb == 0:

        # Inputs
        x = float(input("x ~"))
        a = float(input("a ~"))
        b = float(input("b ~"))
        print("")

        # If x normal, us = True
        if x < toP48 and x > toM16:
            us = 1

        # "f( x ) = ax + b" while
        while( 
            (x < toP48 and x > toM16) and 
            (a != 0 and a != 1)):
                print(str(x))
                x = a*x + b

        # If x&a erorr, print of a&x numlock
        if us == 0 and (a == 0 or a == 1):
            print("[sys] x is big, and a gliched")
        # If x big, print of x numlock
        elif us == 0:
            print("[sys] x is big")
        # If a is 0 or 1, print of a numlock
        elif a == 0 or a == 1:
            print("[sys] a gliched")

        # Restart var "us"
        us = 0
