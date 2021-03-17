#Sp Formula File 11 Novation, d=23.07.20
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
        ci = ""                      # Calculator session's input
        cb = 0                       # Calculator session's bool
        mcb = 0                      # Main -> calc bool
        cee = 0                      # Easter egg
        nb = 0                       # Negaive bool
        cc = 0                       # ch's correct?
    # Filters
        uf1 = ("EXIT", "EX", "EOF")  # United filter of exit, p1
        uf2 = ("Exit", "Ex", "Eof")  # United filter of exit, p2
        uf3 = ("exit", "ex", "eof")  # United filter of exit, p3
        tn1 = ("MathTow", "mATHtOW") # MathTow alt-names filter, p1
        tn2 = ("mathtow", "MATHTOW") # MathTow alt-names filter, p2
        tn3 = ("mt", "MT")           # MathTow alt-names filter, p3
        cn1 = ("calculator", "sc")   # Calc alt-names filter, p1
        cn2 = ("CALCULATOR", "SC")   # Calc alt-names filter, p2
        cn3 = ("calc", "CALC")       # Calc alt-names filter, p3
        nn1 = ("no", "non", "not")   # Negaive names, p1
        nn2 = ("NO", "NON", "NOT")   # Negaive names, p2
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
                        tfx = float(input("x ~"))
                        tfa = float(input("a ~"))
                        tfb = float(input("b ~"))
                        print()
                    # If x good, xd is false
                        if tfx < bx and tfx > lx:
                            xd = 0
                    # If a good, ad is false
                        if tfa == 0 or tfa == 1:
                            ad = 1
                    # Alpha protocol (b ~ fl)
                        if tfa > 1:
                            ap = 0
                    # Proxima protocol (b ~ 0)
                        if tfa < 1:
                            ap = 1
                    # "f( x ) = ax + b" ''while''
                        while((tfx < bx and tfx > lx) and
                        (ad == 0 and ap == 0)):
                            print(str(tfx))
                            tfx = tfa*tfx + tfb
                    # "f( x ) = ax" ''while''
                        while((tfx < bx and tfx > lx) and
                        (ad == 0 and ap == 1)):
                            print(str(tfx))
                            tfx = tfa * tfx
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
                            print("tfx = " + str(tfx))
                            print("tfa = " + str(tfa))
                            print("tfb = " + str(tfb))
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
                print('\nHello in snakeculator! Print "exit" to exit')
                while cb == 0:
                    im = 1
                    if cee == 1:
                        print("[sys} Easter egg!")
                    ci = input()
                    if ci == "easter egg" or ci == "ee":
                        tee = 1
                    if ci == "erorr":
                        pyValuErorr = int("erorr")
                    for cd in uf1:
                        if ci == cd:
                            cb = 1
                    for cd in uf2:
                        if ci == cd:
                            cb = 1
                    for cd in uf3:
                        if ci == cd:
                            cb = 1
                    if ci == "exex":
                        mb = 1
                        cb = 1
                    for en in nn1:
                        if ci == en:
                            nb = 1
                            ci = "ea"
                    for en in nn2:
                        if ci == en:
                            nb = 1
                            ci = "ea"
                    if cb == 0:
                    # Inputs
                        cfa = float(input("a ~"))
                        while cb == 0 and nb == 0:
                            ch = input("ch ~")
                            cfb = float(input("b ~"))
                        # Analysis
                            if ch == "+":
                                cfa = cfa + cfb
                            elif ch == "-":
                                cfa = cfa - cfb
                            elif ch == "x" or ch == "*":
                                cfa = cfa * cfb
                            elif ch == "^" or ch == "**":
                                cfa = cfa - cfb
                            elif ch == "%":
                                cfa = cfa % cfb
                            elif ch == "/" or ch == ":":
                                cfa = cfa / cfb
                            else:
                                cc = 1
                            if cc == 0:
                                print("int is: " + str(cfa))
                            elif cc == 1:
                                print("char incorrect")
                                cc = 0
                            ci = input("add new int? ~")
                            for en in nn1:
                                if ci == en:
                                    nb = 1
                                    ci = "ea"
                            for en in nn2:
                                if ci == en:
                                    nb = 1
                                    ci = "ea"
                            for ed in uf1:
                                if ci == cd:
                                    cb = 1
                            for ed in uf2:
                                if ci == cd:
                                    cb = 1
                            for ed in uf3:
                                if ci == cd:
                                    cb = 1
                    # Restart sp-vars
                        cee = 0
                        nb = 0
                        for en in nn1:
                            if ci != en:
                                ci = "ea"
                        for en in nn2:
                            if ci != en:
                                ci = "ea"
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
