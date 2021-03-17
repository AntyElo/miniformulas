#Sp Formula File 05 infinity, d=xx.07.2020

# Basic var's - 2^48, ~2^-16
toP48 = 281474976710656
toM16 = 0.000015

# Сycle, exit and x-search var's
cl = int(input("cls ~"))
ex = ""
us = 0

# Cycle of formula's tower
while cl != 0 and ex != "exit": 
    ex = input()
    if ex != "exit":
        cl = cl - 1

        # Inputs
        x = float(input("x ~"))
        a = float(input("a ~"))
        b = float(input("b ~"))
        print("")

        # "f( x ) = ax + b" while
        while( 
            (x < toP48 and x > toM16) and 
            (a != 0 and a != 1)):
                if 1:
                    print(str(x))
                    x = a*x + b
                    us = 1

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
