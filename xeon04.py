#Sp Formula File 04 PEP8, d=xx.07.2020

# Basic var's - 2^32, ~2^-16
toP32 = 4294967296
toM16 = 0.000015

# Сycle & exit var's
s = int(input("s ~"))
e = ""

# Cycle of formula's tower
while s != 0 and e != "exit": 
    e = input()
    if e != "exit":
        s = s - 1

        # Inputs
        x = float(input("x ~"))
        a = float(input("a ~"))
        b = float(input("b ~"))
        print("")

        # "f( x ) = ax + b" while
        while( 
            (x < toP32 and x > toM16) and 
            (a != 0 and a != 1)):
                print(str(x))
                x = a*x + b

        # If x big, activate x's numlock
        if x > toP32 or x < toM16:
            print("[sys] X big")
        # If a is 0 or 1, activate a's numlock
        elif a == 0 or a == 1:
            print("[sys] a gliched")
