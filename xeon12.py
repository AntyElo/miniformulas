#Sp Formula File 12 Ambrosia, d=07.08.20
if 1:
    if 1:
# Variables
    # Main vars
        mainInp = ""                    # Main session's input
        mainExBl = 0                    # Main session's bool
        mainInsMod = 0                  # Initialisation of mods
        uniLang = "ru"                  # Interface language
    # MathTow vars
        towInp = ""                     # MathTow session's exit
        towExBl = 0                     # MathTow session's bool
        towExToMainBl = 0               # Main -> tow bool
        towEas = 0                      # Easter egg
        towDbg = 0                      # Debug bool
        tow_xDbg = 1                    # Bool of x-debug
        tow_aDbg = 0                    # Bool of a-debug
        tow_aPtl = 0                    # Protocoling "a"
        towLtl_x = 0.00000000023283     # Minimum of litle x (2^-32)
        towBig_x = 18446744073709552000 # Maximum of big x (2^64)
    # Calculator vars
        calcInp = ""                    # Calculator session's input
        calcExBl = 0                    # Calculator session's bool
        calcExToMainBl = 0              # Main -> calc bool
        calcEas = 0                     # Easter egg
        calcNegBl = 0                   # Negaive bool
        calc_chCrr = 0                  # ch's correct?
        calc_ch = ""
    # Set vars
        setInp = ""                    # Set session's input
        setExBl = 0                    # Set session's bool
        setExToMainBl = 0              # Main -> set bool
        setInfoBl = 1                  # Info bool
    # Filters
        if 1:
        # United filter of exit
            uniFl = (
            """EXIT""", 
            """EX""", 
            """EOF""", 
            """exit""", 
            """ex""", 
            """eof""")
        # MathTow alt-names
            towNm = (
            """mathtow""", 
            """MATHTOW""", 
            """tow""", 
            """TOW""", 
            """mt""", 
            """MT""")
        # Calc alt-names
            calcNm = (
            """calculator""", 
            """CALCULATOR""", 
            """calc""", 
            """CALC""", 
            """sc""", 
            """SC""")
        # Negaive alt-names
            calcNmNeg = (
            """not""", 
            """NOT""", 
            """no""", 
            """NO""", 
            """n""", 
            """N""")
        # Set alt-names
            setNm = (
            """set""", 
            """SET""", 
            """settings""", 
            """SETTINGS""")
        # Set info alt-names
            setNmInfo = (
            """info""", 
            """INFO""", 
            """information""", 
            """INFORMATION""")

# Main session (greeting)
    uniLang = input("language ~")
    if uniLang == "en":
        print('\nHello! This is sff commet. Write "set" to settings')
        print('In Set write "info" to get information')
    if uniLang == "ru":
        print('\nПривет! Это sff commet. Напиши "set" для настроек')
        print('После напиши "info" для прочтения информации')

# Main session (shell)
    while mainExBl == 0:
        mainInp = input(">>> ")
        for mainEx in uniFl:
            if mainInp == mainEx:
                mainExBl = 1
        if mainExBl == 0:

        # The MathTow
            for towExToMain in towNm:
                if mainInp == towExToMain:
                    towExToMainBl = 1
            if towExToMainBl == 1:
            # MathTow-session
                if uniLang == "en":
                    print("\nHello by MathTow")
                if uniLang == "ru":
                    print("\nПривет от МатБашни")
                while towExBl == 0:
                    mainInsMod = 1
                    if towEas == 1:
                        print("[sys} Easter egg!")
                    towInp = input()
                    if towInp == "anty":
                        calcEas = 1
                    if towInp == "tdb1":
                        print("[sys] Debug activate")
                        towDbg = 1
                        towInp = input()
                    if towInp == "tdb0":
                        print("[sys] Debug deactivate")
                        towDbg = 0
                        towInp = input()
                    for towEx in uniFl:
                        if towInp == towEx:
                            towExBl = 1
                    if towInp == "exex":
                        mainExBl = 1
                        towExBl = 1
                    if towExBl == 0:
                    # Inputs
                        tow_x = float(input("x ~"))
                        tow_a = float(input("a ~"))
                        if tow_a > 1:
                            tow_b = float(input("b ~"))
                        print()
                    # If x good, tow_xDbg is false
                        if tow_x < towBig_x and tow_x > towLtl_x:
                            tow_xDbg = 0
                    # If a good, tow_aDbg is false
                        if tow_a == 0 or tow_a == 1:
                            tow_aDbg = 1
                    # Alpha protocol (b ~ fl)
                        if tow_a > 1:
                            tow_aPtl = 0
                    # Proxima protocol (b ~ 0)
                        if tow_a < 1:
                            tow_aPtl = 1
                    # "f( x ) = ax + b" ''while''
                        while((tow_x < towBig_x and tow_x > towLtl_x) and
                        (tow_aDbg == 0 and tow_aPtl == 0)):
                            print(str(tow_x))
                            tow_x = tow_a*tow_x + tow_b
                    # "f( x ) = ax" ''while''
                        while((tow_x < towBig_x and tow_x > towLtl_x) and
                        (tow_aDbg == 0 and tow_aPtl == 1)):
                            print(str(tow_x))
                            tow_x = tow_a * tow_x
                    # Print of x&a|x|a numlock
                        if tow_xDbg == 1 and tow_aDbg == 1:
                            if uniLang == "en":
                                print("[sys] x is big and a gliched")
                            if uniLang == "ru":
                                print("[sys] x большой и a глючная")
                        elif tow_xDbg == 1:
                            if uniLang == "en":
                                print("[sys] x is big")
                            if uniLang == "ru":
                                print("[sys] x большой")
                        elif tow_aDbg == 1:
                            if uniLang == "en":
                                print("[sys] a gliched")
                            if uniLang == "ru":
                                print("[sys] a глючная")
                    # Debug info
                        if towDbg == 1:
                            print("\n[dbg] Floats (a is int)")
                            print("tow_x = " + str(tow_x))
                            print("tow_a = " + str(tow_a))
                            print("tow_b = " + str(tow_b))
                            print("[dbg] Float-Debug Bools (1 is bad)")
                            print("tow_xDbg = " + str(tow_xDbg))
                            print("tow_aDbg = " + str(tow_aDbg))
                            print("tow_aPtl = " + str(tow_aPtl))
                            print("[dbg] Debug-print bool")
                            print("towDbg = " + str(towDbg))
                            print("[dbg] Exit vars")
                            print("towInp = " + '"' + str(towInp) + '"')
                            print("towExBl = " + str(towExBl))
                            print("[dbg] Easter egg")
                            print("towEas = " + str(towEas))
                            print("calcEas = " + str(calcEas))
                    # Restart sp-vars
                        towEas = 0
                        tow_aDbg = 0
                        tow_xDbg = 1
                # "mt -> main" print
                    elif towExBl == 1:
                        print()
                        towExToMainBl = 0
                towExBl = 0

        # The calculator
            for mainToCalcEx in calcNm:
                if mainInp == mainToCalcEx:
                    calcExToMainBl = 1
            if calcExToMainBl == 1:
            # Calculator-session: Filter, Exit, Bool, Detector
                if uniLang == "en":
                    print('\nHello by Snakeculator')
                if uniLang == "ru":
                    print('\nПривет от Змейкулятора')
                while calcExBl == 0:
                    mainInsMod = 1
                    if calcEas == 1:
                        print("[sys} Easter egg!")
                    calcInp = input()
                    if calcInp == "anty":
                        towEas = 1
                    for calcEx in uniFl:
                        if calcInp == calcEx:
                            calcExBl = 1
                    if calcInp == "exex":
                        mainExBl = 1
                        calcExBl = 1
                    if calcExBl == 0:
                    # Inputs
                        calc_a = float(input("a ~"))
                        while calcExBl == 0 and calcNegBl == 0:
                            if uniLang == "en":
                                calc_ch = input("char ~")
                            if uniLang == "ru":
                                calc_ch = input("знак ~")
                            calc_b = float(input("b ~"))
                        # Analysis
                            if calc_ch == "+":
                                calc_a = calc_a + calc_b
                            elif calc_ch == "-":
                                calc_a = calc_a - calc_b
                            elif calc_ch == "x" or calc_ch == "*":
                                calc_a = calc_a * calc_b
                            elif calc_ch == "^" or calc_ch == "**":
                                calc_a = calc_a ** calc_b
                            elif calc_ch == "%":
                                calc_a = calc_a % calc_b
                            elif calc_ch == "/" or calc_ch == ":":
                                calc_a = calc_a / calc_b
                            else:
                                calc_chCrr = 1
                        # Prints
                            if calc_chCrr == 0:
                                if uniLang == "en":
                                    print("int is: " + str(calc_a))
                                if uniLang == "ru":
                                    print("ит. число: " + str(calc_a))
                            elif calc_chCrr == 1:
                                if uniLang == "en":
                                    print("char incorrect")
                                if uniLang == "ru":
                                    print("знак неверный")
                                calc_chCrr = 0
                            if uniLang == "en":
                                calcInp = input("add new int? ~")
                            elif uniLang == "ru":
                                calcInp = input("добавить число? ~")
                            else: 
                                calcInp = input("ERORR ")
                                calcNegBl = 1
                        # Restart
                            for calcExNeg in calcNmNeg:
                                if calcInp == calcExNeg:
                                    calcNegBl = 1
                                    calcInp = "ea"
                            for calcExToMain in uniFl:
                                if calcInp == calcExToMain:
                                    calcExBl = 1
                    # Restart sp-vars
                        calcEas = 0
                        calcNegBl = 0
                        for calcExNeg in calcNmNeg:
                            if calcInp != calcExNeg:
                                calcInp = "ea"
                # "calc -> main" print
                    elif calcExBl == 1:
                        print()
                        calcExToMainBl = 0
                calcExBl = 0

        # The set
            for mainToSetEx in setNm:
                if mainInp == mainToSetEx:
                    setExToMainBl = 1
            if setExToMainBl == 1:
            # Set-session
                if uniLang == "en":
                    print('\nHello by InterFace Settings')
                if uniLang == "ru":
                    print('\nПривет от Настроек Интерфейса')
                while setExBl == 0:
                    mainInsMod = 1
                    setInp = input(uniLang + "| ")
                    for setEx in uniFl:
                        if setInp == setEx:
                            setExBl = 1
                    if setInp == "exex":
                        mainExBl = 1
                        setExBl = 1
                    if setExBl == 0:
                    # Language settings
                        if setInp == "lang_en":
                            uniLang = "en"
                        if setInp == "lang_ru":
                            uniLang = "ru"
                    # Info
                    # "\n"" """, )
                        for setInfo in setNmInfo:
                            if setInp == setInfo:
                                setInfoBl = 0
                        if setInfoBl == 0:
                            if uniLang == "en":
                                print(
                                    "\n""=-=-= Info =-=-=""",  
                                    "\n"" """, 
                                    "\n""   0. Example""", 
                                    "\n""canWrite, writeble That is?""", 
                                    "\n""   1. Shell""", 
                                    "\n""exit, ex, eof      Exit in OS // Consle""", 
                                    "\n""tow, mt            Play to MathTow""", 
                                    "\n""calc, sc           Play to Snakeculator""", 
                                    "\n""set, fc           Play to Settings""",
                                    "\n""   2. MathTow""", 
                                    "\n""exit, ex, eof      Exit to Shell""", 
                                    "\n""exex               Exit in OS // Consle""", 
                                    "\n""<enter>            Start to bild tower""", 
                                    "\n""tdb0               Debug off""", 
                                    "\n""tdb1               Debug on""", 
                                    "\n""   3. Snakeculator""", 
                                    "\n""exit, ex, eof      Exit to Shell""", 
                                    "\n""exex               Exit in OS // Consle""", 
                                    "\n""<enter>            Start to calculate""", 
                                    "\n""anty               ???""", 
                                    "\n""   4. Settings""", 
                                    "\n""exit, ex, eof      Exit to Shell""", 
                                    "\n""exex               Exit in OS // Consle""", 
                                    "\n""lang_en            Language_English change""", 
                                    "\n""lang_ru            Language_Russion change""", 
                                    "\n"" """,)
                            elif uniLang == "ru":
                                print(
                                    "\n""=-=-= Справка =-=-=""",  
                                    "\n"" """, 
                                    "\n""   0. Пример""", 
                                    "\n""<команда>,writeble Как это работает?""", 
                                    "\n""   1. Оболочка""", 
                                    "\n""exit, ex, eof      Выход в ОС // Консоль""", 
                                    "\n""tow, mt            Перейти в МатБашню""", 
                                    "\n""calc, sc           Перейти в Змейкулятор""", 
                                    "\n""set                Перейти в Настроки""",
                                    "\n""   2. МатБашня""", 
                                    "\n""exit, ex, eof      Выход в Оболочку""", 
                                    "\n""exex               Выход в ОС // Консоль""", 
                                    "\n""<enter>            Начать делать матбашни""", 
                                    "\n""tdb0               Выключить Дебаг""", 
                                    "\n""tdb1               Включить Дебаг""", 
                                    "\n""   3. Змейкулятор""", 
                                    "\n""exit, ex, eof      Выход в Оболочку""", 
                                    "\n""exex               Выход в ОС // Консоль""", 
                                    "\n""<enter>            Начать работать с Змейкулятором""", 
                                    "\n""anty               ???""", 
                                    "\n""   4. Настроки""", 
                                    "\n""exit, ex, eof      Выход в Оболочку""", 
                                    "\n""exex               Выход в ОС // Консоль""", 
                                    "\n""lang_en            Переход на Английский язык""", 
                                    "\n""lang_ru            Переход на Русский язык""", 
                                    "\n"" """, )
                            else:
                                print("ERORR!!! ERORR!!! ERORR!!! ERORR!!! ERORR!!!")
                            setInfoBl = 1
                # "set -> main" print
                    elif setExBl == 1:
                        setExToMainBl = 0
                setExBl = 0
                setInp = ""

        # If mod no defined
            if mainInsMod == 0:
                if uniLang == "en":
                    print("\nWhat do you mean?")
                if uniLang == "ru":
                    print("\nЧто ты имеешь ввиду?")
            elif mainInsMod == 1:
                mainInsMod = 0

# End
