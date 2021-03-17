#Sp Formula File 10 Symphony, d=22.07.20
if True:
    if True:
# Variables
    # Main vars
        mi = ""                      # Main session's input
        mb = 0                       # Main session's bool
        im = 0                       # Initialisation of mods
    # MathTow vars
        te = ""                      # MathTow session's exit
        tb = 0                       # MathTow session's bool
        mtb = 0                      # Main -> tow bool
        tee = 0                      # Easter egg
        tdb = 0                      # Debug bool
        xd = 1                       # Bool of x-debug
        ad = 0                       # Bool of a-debug
        ap = 0                       # Protocoling "a"
        lx = 0.00000000023283        # Minimum of litle x (2^-32)
        bx = 18446744073709552000    # Maximum of big x (2^64)
    # Calculator vars
        ce = ""                      # Calculator session's exit
        cb = 0                       # Calculator session's bool
        mcb = 0                      # Main -> calc bool
        cee = 0                      # Easter egg
    # Filters
        uf1 = ("EXIT", "EX", "EOF")  # United filter of exit, part 1
        uf2 = ("Exit", "Ex", "Eof")  # United filter of exit, part 2
        uf3 = ("exit", "ex", "eof")  # United filter of exit, part 3
        tn1 = ("MathTow", "mATHtOW") # MathTow alt-names filter, p1
        tn2 = ("mathtow", "MATHTOW") # MathTow alt-names filter, p2
        tn3 = ("mt", "MT")           # MathTow alt-names filter, p3
        cn1 = ("calculator", "cl")   # Calc alt-names filter, p1
        cn2 = ("CALCULATOR", "CL")   # Calc alt-names filter, p2
        cn3 = ("calc", "CALC")       # Calc alt-names filter, p3
# Main session (greeting)
    print('\nHello in sff commet! Print "MathTow" to start MathTow,')
    print('print "calc" to start calc, or print "exit" to exit\n')
# Main session (shell)
    while mb == 0:
        mi = input(">>> ")
        for md in uf1:
            if mi == md:
                mb = 1
        for md in uf2:
            if mi == md:
                mb = 1
        for md in uf3:
            if mi == md:
                mb = 1
        if mb == 0:
            if mi == "erorr":
                pyValuErorr = int("erorr")

        # The MathTow
            for mtd in tn1:
                if mi == mtd:
                    mtb = 1
            for mtd in tn2:
                if mi == mtd:
                    mtb = 1
            for mtd in tn3:
                if mi == mtd:
                    mtb = 1
            if mtb == 1:
            # MathTow-session: Filter, Exit, Bool, Detector
                print("\nHello in MathTow! Press [enter] to start")
                print('Or print "exit" to exit')
                while tb == 0:
                    im = 1
                    if tee == 1:
                        print("[sys} Easter egg!")
                    te = input()
                    if te == "easter egg" or te == "ee":
                        cee = 1
                    if te == "erorr":
                        pyValuErorr = int("erorr")
                    for td in uf1:
                        if te == td:
                            tb = 1
                    for td in uf2:
                        if te == td:
                            tb = 1
                    for td in uf3:
                        if te == td:
                            tb = 1
                    if te == "exex":
                        mb = 1
                        tb = 1
                    if tb == 0:
                    # TowDeBug//TowDebugBool
                        if te == "debug" or te == "tdb1":
                            print("[sys] Debug activate")
                            tdb = 1
                            te = input()
                        if te == "debugout" or te == "tdb0":
                            print("[sys] Debug deactivate")
                            tdb = 0
                            te = input()
                    # Inputs
                        x = float(input("x ~"))
                        a = float(input("a ~"))
                        b = float(input("b ~"))
                        print()
                    # If x good, xd is false
                        if x < bx and x > lx:
                            xd = 0
                    # If a good, ad is false
                        if a == 0 or a == 1:
                            ad = 1
                    # Alpha protocol (b ~ fl)
                        if a > 1:
                            ap = 0
                    # Proxima protocol (b ~ 0)
                        if a < 1:
                            ap = 1
                    # "f( x ) = ax + b" ''while''
                        while((x < bx and x > lx) and
                        (ad == 0 and ap == 0)):
                            print(str(x))
                            x = a*x + b
                    # "f( x ) = ax" ''while''
                        while((x < bx and x > lx) and
                        (ad == 0 and ap == 1)):
                            print(str(x))
                            x = a * x
                    # Print of x&a|x|a numlock
                        if xd == 1 and ad == 1:
                            print("[sys] x is big, and a gliched")
                        elif xd == 1:
                            print("[sys] x is big")
                        elif ad == 1:
                            print("[sys] a gliched")
                    # Debug info
                        if tdb == 1:
                            print("\n[dbg] Floats (a is int)")
                            print("x = " + str(x))
                            print("a = " + str(a))
                            print("b = " + str(b))
                            print("[dbg] Float-Debug Bools (1 is bad)")
                            print("xd = " + str(xd))
                            print("ad = " + str(ad))
                            print("ap = " + str(ap))
                            print("[dbg] Debug-print bool")
                            print("tdb = " + str(tdb))
                            print("[dbg] Exit vars")
                            print("te = " + '"' + str(te) + '"')
                            print("tb = " + str(tb))
                            print("[dbg] Easter egg")
                            print("tee = " + str(tee))
                            print("cee = " + str(cee))
                    # Restart sp-vars
                        tee = 0
                        ad = 0
                        xd = 1
                # "mt -> main" print
                    elif tb == 1:
                        print()
                        mtb = 0
                tb = 0

        # The calculator
            for mcd in cn1:
                if mi == mcd:
                    mcb = 1 
            for mcd in cn2:
                if mi == mcd:
                    mcb = 1
            for mcd in cn3:
                if mi == mcd:
                    mcb = 1
            if mcb == 1:
            # Calculator-session: Filter, Exit, Bool, Detector
                print('\nCalculator as coming soon! Print "exit" to exit')
                while cb == 0:
                    im = 1
                    if cee == 1:
                        print("[sys} Easter egg!")
                    ce = input()
                    if ce == "easter egg" or ce == "ee":
                        tee = 1
                    if ce == "erorr":
                        pyValuErorr = int("erorr")
                    for cd in uf1:
                        if ce == cd:
                            cb = 1
                    for cd in uf2:
                        if ce == cd:
                            cb = 1
                    for cd in uf3:
                        if ce == cd:
                            cb = 1
                    if ce == "exex":
                        mb = 1
                        cb = 1
                    if cb == 0:
                        print("[sys] Commet soon")
                    # Restart sp-vars
                        cee = 0
                # "calc -> main" print
                    elif cb == 1:
                        print()
                        mcb = 0
                cb = 0

        # If mod no defined
            if im == 0:
                print("\nWhat do you mean?")
            elif im == 1:
                im = 0
