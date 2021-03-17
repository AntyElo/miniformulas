# Hello in Anty's mathDemo SpFormulaFile//Miniformulas!
mainV = "2"# Date of relise = 21.12.20, use to base Neon-20w52a
# [For beta] year-w-week-part e.g.: 20w51a - 2020th year, 52th week, 1st part
uniLang = "ru" # Interface language
def exscan(inp): # Exit-verbs searh, EXit BooLean
	exbl=0 
	if (inp=='exit'or inp=='ex'or inp=='eof'or inp=='quit'or inp=='q'):exbl = 1
	return exbl 
def uList(sList, sV):
	ulCyc = 0 # Correct work
	exV = "" # exit verb
	for exV in sList:
		if sV == exV:
			return 0
			ulCyc = 1
	if ulCyc == 0:
		return 1
# Main session (greeting)
unknowlang = 0 # languge select
while unknowlang == 0:
	unknowlang = 1
	langInp = input("language ~")
	if langInp == "ru" or langInp == "rus": uniLang = "ru"
	elif langInp == "en" or langInp == "eng": uniLang = "en"
	else: unknowlang = 0, print("unknow languge")
if uniLang == "ru":
	print('\nПривет! Это Miniformulas ' + mainV + '.')
	print('Напиши "set" для настроек, или ')
	print('Напиши "help" для прочтения информации')
else:
	print('\nHello! This is Miniformulas ' + mainV + '.')
	print('Write "set" to settings, or ')
	print('Write "help" to get information')
# Main session (shell)
mainInp = "" # Main session's input
while exscan(mainInp) == 0:
	mainInp = input(">>> ")
	if exscan(mainInp) == 0:
		mainInsMod = 0 # Initialisation of mods
		# The MathTow
		towNm = ("mathtow", "tow", "mt") # MathTow all names
		if uList(towNm, mainInp) == 0:
			# MathTow-session
			if uniLang == "ru": print("\nПривет от МатБашни")
			else: print("\nHello by MathTow")
			towInp = "" # MathTow session's exit
			while exscan(towInp) == 0:
				mainInsMod = 1
				towInp = input()
				if exscan(towInp) == 0:
					try:
						# Inputs
						tow_x = float(input("x ~"))
						tow_a = float(input("a ~"))
						if tow_a > 1: tow_b = float(input("b ~"))
						print()
						towLtl_x = 0.00000000023283 # Minimum of litle x (2^-32)
						towBig_x = 18446744073709552000 # Maximum of big x (2^64)
						tow_xDbg = 1 # Bool of x-debug
						if towBig_x > tow_x > towLtl_x: tow_xDbg = 0 # If x good, tow_xDbg is false
						tow_aDbg = 0 # Bool of a-debug
						if tow_a == 0 or tow_a == 1: tow_aDbg = 1 # If a good, tow_aDbg is false
						tow_aPtl = 1 # Protocoling "a"
						if tow_a > 1: tow_aPtl = 0 # If a > 1, store b as a addendum
						# x's cycle
						while(towBig_x > tow_x > towLtl_x and tow_aDbg == 0):
							print(str(tow_x))
							if tow_aPtl == 0: tow_x = tow_a*tow_x + tow_b
							if tow_aPtl == 1: tow_x = tow_a*tow_x
						# Print of incorrected ints
						if tow_xDbg == 1:
							if uniLang == "ru": print("[sys] x вне рамок (" + str(tow_x) + ")")
							else: print("[sys] x went beyond (" + str(tow_x) + ")")
						if tow_aDbg == 1:
							if uniLang == "ru": print("[sys] a глючная   (" + str(tow_a) + ")")
							else: print("[sys] a gliched     (" + str(tow_a) + ")")
					# Except global MT's error
					except ValueError:
						if uniLang == "ru": print("[sys] плохое число")
						else: print("[sys] bad float")
			print()
		# The calculator
		calcNm = ("calculator", "calc", "sc") # Calc all names
		if uList(calcNm, mainInp) == 0:
			# Calculator-session: Filter, Exit, Bool, Detector
			if uniLang == "ru": print('\nПривет от Калькулятора')
			else: print('\nHello by Calculator')
			calcInp = "" # Calculator session's input
			while exscan(calcInp) == 0:
				mainInsMod = 1
				calcInp = input()
				if exscan(calcInp) == 0:
					calcNegBl = 0 # Negaive bool
					calcNmNeg = ("not", "no", "n", "N") # Negaive all names
					try:
						# Inputs
						calc_a = float(input("a ~"))
						while exscan(calcInp) == 0 and calcNegBl == 0:
							calc_ch = input("* ~")
							calc_b = float(input("b ~"))
							# Analysis
							calc_chCrr = 0
							if calc_ch == "+": calc_a = calc_a + calc_b
							elif calc_ch == "-": calc_a = calc_a - calc_b
							elif calc_ch == "x" or calc_ch == "*": calc_a = calc_a * calc_b
							elif calc_ch == "^" or calc_ch == "**": calc_a = calc_a ** calc_b
							elif calc_ch == "%": calc_a = calc_a % calc_b
							elif calc_ch == "/" or calc_ch == ":": calc_a = calc_a / calc_b
							else: calc_chCrr = 1
							# Prints
							if calc_chCrr == 0:
								if uniLang == "ru": print("ит. число: " + str(calc_a))
								else: print("int is: " + str(calc_a))
							elif calc_chCrr == 1:
								calc_chCrr = 0
								if uniLang == "ru": print("знак неверный")
								else: print("char incorrect")
							if uniLang == "ru": calcInp = input("добавить число? ~")
							else: calcInp = input("add new int? ~")
							# Restart
							for calcExNeg in calcNmNeg:
								if calcInp == calcExNeg:
									calcNegBl = 1
									calcInp = "ea"
						calcNegBl = 0
						for calcExNeg in calcNmNeg: 
							if calcInp != calcExNeg: 
								calcInp = "ea"
					# Except global SC's error
					except ValueError:
						if uniLang == "ru": print("[sys] плохое число")
						else: print("[sys] bad float")
			print()
		# The set
		setNm = ("set", "settings") # Set all names
		if uList(setNm, mainInp) == 0:
			# Set-session
			if uniLang == "ru": print('\nПривет от Настроек Интерфейса')
			else: print('\nHello by InterFace Settings')
			setInp = "" # Set session's input
			while exscan(setInp) == 0:
				mainInsMod = 1
				setInp = input(uniLang + "| ")
				if exscan(setInp) == 0:
					# Language settings
					if setInp == "lang_ru": uniLang = "ru"
					if setInp == "lang_en": uniLang = "en"
					if setInp == "local":
						setInp = input("local# ")
						if setInp == "ru" or setInp == "rus": uniLang = "ru"
						if setInp == "en" or setInp == "eng": uniLang = "en"
						setInp = ""
			print()
		# The MaxInt
		miNm = ("maxint", "mi") # MaxInt all names
		if uList(miNm, mainInp) == 0:
			# mi-session
			if uniLang == "ru": print('\nПривет от МаксЧисла')
			else: print('\nHello by MaxInt')
			miInp = "" # mi session's input
			while exscan(miInp) == 0:
				mainInsMod = 1
				miInp = input()
				if exscan(miInp) == 0:
					try:
						i = int(input("int ~"))
						a = 2
						b = 3
						# Make D1 = i/D2 and D2 = i/D1
						D1 = [1]
						D2 = [i]
						while a < b:
							b = i // a
							d = i % a
							if d == 0:
								if a != b:
									D1.append(a)
								D2.append(b)
							a += 1
						if i == 0:
							print('D0=["inf"]')
						elif i == 1:
							print("D1=[1]")
						else:
							print("   " + str(D1))
							print("   " + str(D2))
					except ValueError:
						if uniLang == "ru": print("[sys] Число некорректно!")
						else: print("[sys] Number incorrect!")
			print()
		# Print help	"\n"" """, )
		if mainInp == "help" or mainInp == "h" or mainInp == "info":
			mainInsMod = 1
			if uniLang == "ru": print(
				"\n""=-=-= Справка =-=-=""",  
				"\n"" """, 
				"\n""   0. Пример""", 
				"\n""<команда>          Как это работает?""", 
				"\n""   1. Оболочка""", 
				"\n""tow, mt            Перейти в МатБашню""", 
				"\n""calc, sc           Перейти в Калькулятор""", 
				"\n""set                Перейти в Настроки""",
				"\n""maxint, mi         Перейти в МаксЧисло""", 
				"\n""exit, quit, eof    Выход из программы""", 
				"\n""   2. МатБашня""", 
				"\n""<enter>            Начать делать матбашни""", 
				"\n""exit, quit, eof    Выход в Оболочку""", 
				"\n""   3. Калькулятор""", 
				"\n""<enter>            Начать работать с Калькулятором""", 
				"\n""exit, quit, eof    Выход в Оболочку""", 
				"\n""   4. Настроки""", 
				"\n""lang_ru            Переход на Русский язык""", 
				"\n""lang_en            Переход на Английский язык""", 
				"\n""exit, quit, eof    Выход в Оболочку""", 
				"\n"" """, )
			else: print(
				"\n""=-=-= Info =-=-=""",  
				"\n"" """, 
				"\n""   0. Example""", 
				"\n""<command>          That is?""", 
				"\n""   1. Shell""", 
				"\n""tow, mt            Play to MathTow""", 
				"\n""calc, sc           Play to Calculator""", 
				"\n""set, fc            Play to Settings""",
				"\n""maxint, mi         Play to MaxInt""", 
				"\n""exit, quit, eof    Exit the Miniformulas""", 
				"\n""   2. MathTow""", 
				"\n""<enter>            Start to bild tower""", 
				"\n""exit, quit, eof    Exit to Shell""", 
				"\n""   3. Calculator""", 
				"\n""<enter>            Start to calculate""", 
				"\n""exit, quit, eof    Exit to Shell""", 
				"\n""   4. Settings""", 
				"\n""lang_ru            Language_Russion change""", 
				"\n""lang_en            Language_English change""", 
				"\n""exit, quit, eof    Exit to Shell""", 
				"\n""   5. MaxInt""", 
				"\n""<enter>            Start to search divisors""", 
				"\n""exit, quit, eof    Exit to Shell""", 
				"\n"" """,)
		# Main/Shell/sys: If mod no defined
		if mainInsMod == 0 and mainInp != '' and mainInp != ' ' and mainInp != '  ':
			if uniLang == "ru": print("\nЧто ты имеешь ввиду?")
			else: print("\nWhat do you mean?")
