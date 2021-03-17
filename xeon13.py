#Sp Formula File Argon-1 Baseology, d=01.12.20
if 1:
	if 1:
# allVariables
		mainInp = "" # Main session's input
		mainInsMod = 0 # Initialisation of mods
		uniLang = "ru" # Interface language
		towInp = "" # MathTow session's exit
		towExToMainBl = 0 # Main -> tow bool
		towDbg = 0 # Debug bool
		tow_xDbg = 1 # Bool of x-debug
		tow_aDbg = 0 # Bool of a-debug
		tow_aPtl = 0 # Protocoling "a"
		towLtl_x = 0.00000000023283 # Minimum of litle x (2^-32)
		towBig_x = 18446744073709552000 # Maximum of big x (2^64)
		calcInp = "" # Calculator session's input
		calcExToMainBl = 0 # Main -> calc bool
		calcNegBl = 0 # Negaive bool
		setInp = "" # Set session's input
		setExToMainBl = 0 # Main -> set bool
		setInfoBl = 1 # Info bool
		towNm = ("mathtow", "tow", "mt") # MathTow all names
		calcNm = ("calculator", "calc", "sc") # Calc all names
		calcNmNeg = ("not", "no", "n", "N") # Negaive all names
		setNm = ("""set""", """settings""") # Set all names
		setNmInfo = ("info", "information") # Set info all names
		# Exit-verbs searh, EXit BooLean
		def exscan(inp):
			if inp == 'exit': exbl = 1
			elif inp == 'ex': exbl = 1
			elif inp == 'eof': exbl = 1
			elif inp == 'quit': exbl = 1
			elif inp == 'q': exbl = 1
			else: exbl = 0
			return exbl

# Main session (greeting)
	uniLang = input("language ~")
	if uniLang == "en":
		print('\nHello! This is sff commet. Write "set" to settings')
		print('In Set write "info" to get information')
	if uniLang == "ru":
		print('\nПривет! Это sff commet. Напиши "set" для настроек')
		print('После напиши "info" для прочтения информации')

# Main session (shell)
	while exscan(mainInp) == 0:
		mainInp = input(">>> ")
		if exscan(mainInp) == 0:

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
				while exscan(towInp) == 0:
					mainInsMod = 1
					towInp = input()
					if towInp == "tdb1":
						print("[sys] Debug activate")
						towDbg = 1
						towInp = input()
					if towInp == "tdb0":
						print("[sys] Debug deactivate")
						towDbg = 0
						towInp = input()
					if exscan(towInp) == 0:
						try:
						# Inputs
							tow_x = float(input("x ~"))
							tow_a = float(input("a ~"))
							if tow_a > 1:
								tow_b = float(input("b ~"))
							print()
							if tow_x < towBig_x and tow_x > towLtl_x: tow_xDbg = 0 # If x good, tow_xDbg is false
							if tow_a == 0 or tow_a == 1: tow_aDbg = 1 # If a good, tow_aDbg is false
							if tow_a > 1: tow_aPtl = 0 # Alpha protocol (b ~ fl)
							if tow_a < 1: tow_aPtl = 1 # Proxima protocol (b ~ 0)
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
							if tow_xDbg == 1:
								if uniLang == "ru": print("[sys] x большой")
								else: print("[sys] x is big")
							if tow_aDbg == 1:
								if uniLang == "ru": print("[sys] a глючная")
								else: print("[sys] a gliched")
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
						# Restart sp-vars
							tow_aDbg = 0
							tow_xDbg = 1
					# Except global MT's error
						except ValueError:
							if uniLang == "ru": print("[sys] плохое число")
							else: print("[sys] bad float")
				# "mt -> main" print
				towExToMainBl = 0
				towInp = ''
				print()

		# The calculator
			for mainToCalcEx in calcNm: 
				if mainInp == mainToCalcEx: 
					calcExToMainBl = 1
			if calcExToMainBl == 1:
			# Calculator-session: Filter, Exit, Bool, Detector
				if uniLang == "ru": print('\nПривет от Змейкулятора')
				else: print('\nHello by Snakeculator')
				while exscan(calcInp) == 0:
					mainInsMod = 1
					calcInp = input()
					if exscan(calcInp) == 0:
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
						# Restart sp-vars
							calcNegBl = 0
							for calcExNeg in calcNmNeg: 
								if calcInp != calcExNeg: 
									calcInp = "ea"
					# Except global SC's error
						except ValueError:
							if uniLang == "ru": print("[sys] плохое число")
							else: print("[sys] bad float")
				# "calc -> main" print
				calcExToMainBl = 0
				calcInp = ''
				print()

		# The set
			for mainToSetEx in setNm: 
				if mainInp == mainToSetEx: 
					setExToMainBl = 1
			if setExToMainBl == 1:
			# Set-session
				if uniLang == "ru": print('\nПривет от Настроек Интерфейса')
				else: print('\nHello by InterFace Settings')
				while exscan(setInp) == 0:
					mainInsMod = 1
					setInp = input(uniLang + "| ")
					if exscan(setInp) == 0:
					# Language settings
						if setInp == "lang_en": uniLang = "en"
						if setInp == "lang_ru": uniLang = "ru"
					# Info  "\n"" """, )
						for setInfo in setNmInfo: 
							if setInp == setInfo: 
								setInfoBl = 0
						if setInfoBl == 0:
							if uniLang == "ru":
								print(
									"\n""=-=-= Справка =-=-=""",  
									"\n"" """, 
									"\n""   0. Пример""", 
									"\n""<команда>          Как это работает?""", 
									"\n""   1. Оболочка""", 
									"\n""exit, quit, eof    Выход в ОС // Консоль""", 
									"\n""tow, mt            Перейти в МатБашню""", 
									"\n""calc, sc           Перейти в Змейкулятор""", 
									"\n""set                Перейти в Настроки""",
									"\n""   2. МатБашня""", 
									"\n""exit, quit, eof    Выход в Оболочку""", 
									"\n""<enter>            Начать делать матбашни""", 
									"\n""tdb0               Выключить Дебаг""", 
									"\n""tdb1               Включить Дебаг""", 
									"\n""   3. Змейкулятор""", 
									"\n""exit, quit, eof    Выход в Оболочку""", 
									"\n""<enter>            Начать работать с Змейкулятором""", 
									"\n""   4. Настроки""", 
									"\n""exit, quit, eof    Выход в Оболочку""", 
									"\n""lang_en            Переход на Английский язык""", 
									"\n""lang_ru            Переход на Русский язык""", 
									"\n"" """, )
							else:
								print(
									"\n""=-=-= Info =-=-=""",  
									"\n"" """, 
									"\n""   0. Example""", 
									"\n""<command>          That is?""", 
									"\n""   1. Shell""", 
									"\n""exit, quit, eof    Exit in OS // Consle""", 
									"\n""tow, mt            Play to MathTow""", 
									"\n""calc, sc           Play to Snakeculator""", 
									"\n""set, fc            Play to Settings""",
									"\n""   2. MathTow""", 
									"\n""exit, quit, eof    Exit to Shell""", 
									"\n""<enter>            Start to bild tower""", 
									"\n""tdb0               Debug off""", 
									"\n""tdb1               Debug on""", 
									"\n""   3. Snakeculator""", 
									"\n""exit, quit, eof    Exit to Shell""", 
									"\n""<enter>            Start to calculate""", 
									"\n""   4. Settings""", 
									"\n""exit, quit, eof    Exit to Shell""", 
									"\n""lang_en            Language_English change""", 
									"\n""lang_ru            Language_Russion change""", 
									"\n"" """,)
							setInfoBl = 1
				# "set -> main" print
				setExToMainBl = 0
				setInp = ''
				print()

		# If mod no defined
			if mainInsMod == 0:
				if uniLang == "ru": print("\nЧто ты имеешь ввиду?")
				else: print("\nWhat do you mean?")
			elif mainInsMod == 1: mainInsMod = 0
# End
