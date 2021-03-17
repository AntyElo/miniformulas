#Sp Formula File 08 Harmony, d=18.07.20

# 2^64, two filter, x-search and exit var's
x64 = 18446744073709552000
sf = ("exit", "ex", "eof", "EXIT", "EX", "EOF")
se = ""
sb = 0
xs = 0

# sff-session, Filter, Exit, Bool, Detector
while sb == 0: 
    se = input()
    for sd in sf:
        if se == sd:
            sb = 1
    if sb == 0:

        # Inputs
        x = float(input("x ~"))
        a = float(input("a ~"))
        b = float(input("b ~"))
        print()

        # If x is not big, xs = True
        if x < x64:
            xs = 1

        # "f( x ) = ax + b" ''while''
        while(x < x64 and (a != 0 and a != 1)):
                print(str(x))
                x = a*x + b

        # Print of x&a|x|a numlock
        if xs == 0 and (a == 0 or a == 1):
            print("[sys] x is big, and a gliched")
        elif xs == 0:
            print("[sys] x is big")
        elif a == 0 or a == 1:
            print("[sys] a gliched")

        # Restart var "xs"
        xs = 0
