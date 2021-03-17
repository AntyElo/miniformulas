#Sp Formula File 07 Commet lake, d=17.07.2020

# 2^48, ~2^-16, exit, x-search and two filter var's
toP48 = 281474976710656
toM16 = 0.000015
ex = ""
us = 0
lf = ("exit", "ex", "eof", "EXIT", "EX", "EOF")
lb = 0

# ssf-session door 1
while lb == 0: 
    ex = input()

    # Filter
    for lc in lf:
        if ex == lc:
            lb = 1

    # ssf-session door 2
    if lb == 0:

        # Inputs
        x = float(input("x ~"))
        a = float(input("a ~"))
        b = float(input("b ~"))
        print()

        # If x normal, us = True
        if x < toP48 and x > toM16:
            us = 1

        # "f( x ) = ax + b" ''while''
        while( 
            (x < toP48 and x > toM16) and 
            (a != 0 and a != 1)):
                print(str(x))
                x = a*x + b

        # Print of x&a|x|a numlock
        if us == 0 and (a == 0 or a == 1):
            print("[sys] x is big, and a gliched")
        elif us == 0:
            print("[sys] x is big")
        elif a == 0 or a == 1:
            print("[sys] a gliched")

        # Restart var "us"
        us = 0
