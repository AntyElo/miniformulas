#Sp Formula File 09 Fantasy, d=19.07.20

    # Main vars
mb = 0                      # Main session's bool
mi = ""                     # Main session's input

    # MathTow vars
tb = 0                      # MathTow session's bool
te = ""                     # MathTow session's exit
bx = 18446744073709552000   # Maximum of big x (2^64)
lx = 0.00000000023283       # Minimum of litle x (2^-32)
xs = 0                      # x-search bool

    # United filter of exit
uf = ("exit", "ex", "eof", "Exit", "Ex", "Eof", "EXIT", "EX", "EOF")

# Main session
print("Hello in sff commet!")
print("Print \"MathTow\" to start MathTow,")
print("or print \"exit\" to exit")
while mb == 0:
    mi = input(">>>")
    for md in uf:
        if mi == md:
            mb = 1
    if mb == 0:


        # The MathTow
        if mi == "MathTow":

            # mt-session: Filter, Exit, Bool, Detector
            print("Hello in MathTow! Press [enter] to start")
            print("Or print \"exit\" to exit")
            while tb == 0: 
                te = input()
                for td in uf:
                    if te == td:
                        tb = 1
                if tb == 0:

                    # Inputs
                    x = float(input("x ~"))
                    a = float(input("a ~"))
                    b = float(input("b ~"))
                    print()

                    # If x is not big, xs = True
                    if x < bx and x > lx:
                        xs = 1

                    # "f( x ) = ax + b" ''while''
                    while((x < bx and x > lx) and
                    (a != 0 and a != 1)):
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

        # If mod no defined
        else:
            print("What do you want?")
