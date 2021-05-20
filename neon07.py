import os
import os.path as ospath
import sys
import math
import time
try:
#	import gi	# post: pyGObject, GTK
	import tkinter as tk
	import tkinter.ttk as ttk
	import ttkthemes as tth
	import tkinter.filedialog as tkfd
except ImportError:
	print("ttkthemes не обнаружен. Он будет установлен через 2сек (Ctrl-Z для отмены)")
	time.sleep(2)
	osoutcode = os.system("pip3 install -U tkinter ttkthemes")
	print(f"Скаченно [{osoutcode}]: ttkthemes")
	import tkinter as tk
	import tkinter.ttk as ttk
	import ttkthemes as tth
	import tkinter.filedialog as tkfd
# Сокращенние relist (returnList) - выводимый функцией список

# Стороние функции
def xsleep(): time.sleep(0.01)
def cong(list1, list2 = ("", " ", "  ", "   ", "    ", "     ")):
	# Сравнение списков на одинаковые элементы
	var0 = 0
	list1 = (list1, "=====")
	for var1 in list1:
		for var2 in list2:
			xsleep
			if var2 == var1:
				var0 = 1
				return 1
	if var0 == 0: return 0
mathMax = 2147483647
def mathTower(x, a, b): # f(x) = ax + b
	try:
		global mathMax
		if cong(x) == 1: x = 0
		x = float(x)
		if cong(a) == 1: a = 0
		a = float(a)
		if cong(b) == 1: b = 0
		b = float(b)
		relist = [f"x={x}, a={a}, b={b}:", str(x)]
		if abs(a) >= 1 and x != 0 and x != a*x + b:
			while abs(x) < mathMax:
				xsleep
				x = a * x + b
				relist.append(str(x))
		elif x == 0: relist.append("[Цикл] x = 0 ")
		elif abs(a) <= 1: relist.append("[Цикл] Число a между 1 и -1")
		elif abs(x) == a*x + b: relist.append("[Цикл] x = ax + b")
		return relist
	except ValueError:
		return ["[Q] Данные - не числа"]
_re_a = 10
def sffCalc(a, b, char):
	global _re_a
	try:
		if cong(a) == 1: a = 0
		a = float(a)
		if cong(b) == 1: b = 0
		b = float(b)
		if char == "+": _re_a = a + b
		elif char == "-": _re_a = a - b
		elif char == "x" or char == "*": _re_a = a * b
		elif char == ":" or char == "/": _re_a = a / b
		else:
			_re_a = a
			char = "с"
		relist = [f"{a} {char} {b} = {_re_a}"]
	except ValueError:
		_re_a = a
		relist = ["[Q] Данные - не числа"]
	except ZeroDivisionError:
		_re_a = a
		relist = ["[:0] Нельзя делить на ноль"]
	return relist, _re_a
def findDivisors(invar):
	try:
		if cong(invar) == 1: invar = 0
		invar = abs(round(float(invar)))
		fd_a = 2
		fd_b = 3
		# Make D1 = i/D2 and D2 = i/D1
		fd_D1 = [1]
		fd_D2 = [invar]
		while fd_a < fd_b:
			xsleep
			fd_b, fd_cto = divmod(invar, fd_a)
			if fd_cto == 0:
				if fd_a != fd_b: fd_D1.append(fd_a)
				fd_D2.append(fd_b)
			fd_a += 1
		if invar == 0:
			relist = ["D0 = Z"]
		elif invar == 1:
			relist = ["D1 = [1]"]
		elif invar == 2:
			relist = ["D2 = [1, 2]"]
		else:
			fd_D2.reverse()
			relist = [f"D{invar} = {str(fd_D1 + fd_D2)}"]
	except ValueError:
		relist = ["[Q] Данные - не числа"]
	return relist
def findMultiplier(invar, meta=0):
	try:
		if cong(invar) == 1: invar = 0
		invar = abs(round(float(invar)))
		invarMirrow = str(invar) + " = "
		if meta != 0: invarMirrow = ""
		finder = 1
		inlist = []
		while invar > 1:
			xsleep
			finder += 1
			mod = invar % finder
			if mod == 0:
				invar /= finder
				inlist.append(finder)
				finder = 1
		if invarMirrow == 0: relist = [f"{str(invarMirrow)}0"]
		elif invarMirrow == 1: relist = [f"{str(invarMirrow)}1"]
		else:
			revar = ""
			for forvar in inlist:
				revar = revar + "x" + str(forvar)
			revar = revar[1:]
			relist = [f"{str(invarMirrow)}{revar}"]
		return relist
	except ValueError: return ["[Q] Данные - не числа"]
def sffCalcDeamon(a=0, b=0, ch="+"):
	if ch == "=":
		list1 = findDivisors(a)[0]
		list2 = findMultiplier(a, 1)[0]
		lists = [f"{list1}, {list2}"]
		return lists, a
	else:
		relist, A = sffCalc(a, b, ch)
		return relist, A
# Сама по себе программа
iconsize = 16
def main():
	sffVer = "7.0" # Версия sff
	sffName = f"Miniformulas neon {sffVer}"
	filepath = "tmp.txt"
	global mathMax
	global mylicense
	if 1:
		def textLabelRefresh():
			textLabelBig.after(80, textLabelRefresh)
			textIndex = mainText.index("insert")
			textList = list(textIndex)
			tlChar = ""
			tlIndex = 0
			tlBig = ""
			tlSmall = ""
			while tlChar != ".": 
				xsleep
				tlBig += tlChar
				tlChar = textList[tlIndex]
				tlIndex += 1
			while tlIndex < len(textList):
				xsleep
				tlChar = textList[tlIndex]
				tlSmall += tlChar
				tlIndex += 1
			textLabelBig.config(text=f"Строка: {str(tlBig)}")
			textLabelSmall.config(text=f"Символ: {str(tlSmall)}")
		def styling(non=0):
			if cong(themeBox.get(), style.theme_names()) == 1:
				style.set_theme(themeBox.get())
				themeBox.config(values=style.theme_names())
				imgRefresh()
		def cmdsSize(non=0):
			global iconsize
			if   iconsize == 32: iconsize = 16
			elif iconsize == 16: iconsize = 32
			imgRefresh()
		def xSizeMinus(non=0):
			global iconsize
			iconsize = 16
			imgRefresh()
		def xSizePlus(non=0):
			global iconsize
			iconsize = 32
			imgRefresh()
		def imgRefresh(non=0):
			global iconsize
			if   cong(style.current_theme, ("black", "equilux")) == 1:
				if  iconsize == 16:
					infoButton.config(image=infoImg16d)
					saveasButton.config(image=saveasImg16d)
					saveButton.config(image=saveImg16d)
					openButton.config(image=openImg16d)
					newButton.config(image=newImg16d)
					clearButton.config(image=trashImg16d)
				elif iconsize == 32:
					infoButton.config(image=infoImg32d)
					saveasButton.config(image=saveasImg32d)
					saveButton.config(image=saveImg32d)
					openButton.config(image=openImg32d)
					newButton.config(image=newImg32d)
					clearButton.config(image=trashImg32d)
			elif cong(style.current_theme, ("black", "equilux")) == 0:
				if   iconsize == 16:
					infoButton.config(image=infoImg16l)
					saveasButton.config(image=saveasImg16l)
					saveButton.config(image=saveImg16l)
					openButton.config(image=openImg16l)
					newButton.config(image=newImg16l)
					clearButton.config(image=trashImg16l)
				elif iconsize == 32:
					infoButton.config(image=infoImg32l)
					saveasButton.config(image=saveasImg32l)
					saveButton.config(image=saveImg32l)
					openButton.config(image=openImg32l)
					newButton.config(image=newImg32l)
					clearButton.config(image=trashImg32l)
		def xOpen(non=0):
			try:
				global filepath
				style = tth.ThemedStyle(mainwin)
				filepath = tkfd.askopenfilename(
					title="Открыть фаил",
					filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
				)
				if not filepath: return
				xfile = open(filepath, "r")
				xClear()
				mainText.insert("end", xfile.read())
				mainwin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
			except UnicodeDecodeError:
				mainText.insert("end", "[~] Нечитемый тип файла")
		def xSaveAs(non=0):
			global filepath
			style = tth.ThemedStyle(mainwin)
			filepath = tkfd.asksaveasfilename(
				title="Сохранить как",
				defaultextension=".txt", 
				filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
			)
			if not filepath: return
			xfile = open(filepath, "w")
			xfile.write(mainText.get("1.0", "end"))
			mainwin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
		def xSave(non=0):
			global filepath
			style = tth.ThemedStyle(mainwin)
			try:
				if filepath == None or cong(str(filepath), ("", "()")):
					xSaveAs()
					return
			except NameError:
				xSaveAs()
				return
			xfile = open(filepath, "w")
			xfile.write(mainText.get("1.0", "end"))
			mainwin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
		def xNew(non=0):
			global filepath
			style = tth.ThemedStyle(mainwin)
			filepath = tkfd.asksaveasfilename(
				title="Создать файл",
				defaultextension=".txt", 
				filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
			)
			if not filepath: return
			xfile = open(filepath, "w")
			mainText.delete("1.0", "end")
			mainwin.title(f"{sffName} [{filepath}]")
		def xInfo(non=0):
			infoWin = tk.Toplevel()
			infoWin.title("Справка")
			infoWin.geometry("500x600")
			infoBook = ttk.Notebook(master=infoWin)
			if 1:
				bookKeys = ttk.Frame(master=infoBook)
				if 1:
					keysLabel = ttk.Label(master=bookKeys, font="sans 12", text=\
"""Горячие клавиши:
    ^	Ctrl
    F1	Справка

    ^+	Зум иконок
    ^-	Зум иконок
    ^C	Очистить

    ^с	Копировать
    ^x	Вырезать
    ^v	Вставить

    ^s	Сохранить
    ^S	Сохранить как...
    ^o	Открыть
    ^n	Создать""")
					keysLabel.grid(sticky="nwe", columnspan=2, padx=8)
					keysGrip = ttk.Sizegrip(master=bookKeys)
					keysGrip.grid(sticky="s", row=1, column=1)
					bookKeys.rowconfigure(0, weight=1)
					bookKeys.columnconfigure(0, weight=1)
				infoBook.add(bookKeys, text="Горячие клавиши", sticky="nswe")
				bookAbout = ttk.Frame(master=infoBook)
				if 1:
					metaPy = sys.version_info
					metaTk = tk.TkVersion
					metaTheme = "[tth.version_info]"
					aboutLabel = ttk.Label(master=bookAbout, font="sans 12", text=\
f"""Использует:
    Python {metaPy[0]}.{metaPy[1]}.{metaPy[2]}-{sys.version_info[3]}
    tkinter {metaTk}
    ttkthemes {metaTheme}""")
					aboutLabel.grid(sticky="nwe", columnspan=2, padx=8)
					aboutGrip = ttk.Sizegrip(master=bookAbout)
					aboutGrip.grid(sticky="s", row=1, column=1)
					aboutRule = ttk.Label(master=bookAbout, font="sans 12", text="🄯 2020-2021 AntyElo")
					aboutRule.grid(sticky="we", row=1, padx=8)
					bookAbout.rowconfigure(0, weight=1)
					bookAbout.columnconfigure(0, weight=1)
				infoBook.add(bookAbout, text="Об программе", sticky="nswe")
				bookLicence = ttk.Frame(master=infoBook)
				if 1:
					licanceLicence = tk.Text(master=bookLicence, wrap="none", highlightthickness=0)
					licanceLicence.insert("end", mylicense)
					licanceScrollbarY = ttk.Scrollbar(master=bookLicence, orient="vertical", command=licanceLicence.yview)
					licanceScrollbarX = ttk.Scrollbar(master=bookLicence, orient="horizontal", command=licanceLicence.xview)
					licanceLicence.config(
						yscrollcommand=licanceScrollbarY.set, 
						xscrollcommand=licanceScrollbarX.set
					)
					licanceScrollbarY.grid(sticky="ns", column=1)
					licanceScrollbarX.grid(sticky="we", row=1)
					licanceGrip = ttk.Sizegrip(master=bookLicence)
					licanceGrip.grid(sticky="s", row=1, column=1)
					licanceLicence.grid(sticky="nswe", row=0)
					bookLicence.rowconfigure(0, weight=1)
					bookLicence.columnconfigure(0, weight=1)
				infoBook.add(bookLicence, text="Лицензия", sticky="nswe")
			infoBook.grid(row=1, padx=1, pady=1, sticky="nswe")
			infoImg = ttk.Label(master=infoWin, image=appImgB, background="#909090", text=f"v{sffVer}", width=10)
			infoImg.grid(row=0, sticky="nswe")
			infoWin.columnconfigure(0, weight=1)
			infoWin.rowconfigure(1, weight=1)
		def xClear(non=0): mainText.delete("1.0", "end")
	# Окно
	mainwin = tth.ThemedTk()
	mainwin.geometry("600x400")
	mainwin.title(sffName)
	style = tth.ThemedStyle(mainwin)
	comrel = "raised"

	rootMenu = tk.Menu(master=mainwin)
	fileMenu = tk.Menu(master=rootMenu)
	rootMenu.add_cascade(label="Файл", menu=fileMenu)
	fileMenu.add_command(label="Сохранить", command=xSave)
	fileMenu.add_command(label="Сохранить как", command=xSaveAs)
	fileMenu.add_command(label="Открыть", command=xOpen)
	fileMenu.add_command(label="Создать", command=xNew)
	rootMenu.add_cascade(label="Очистить", command=xClear)
	#mainwin["menu"] = rootMenu
	mainMenuframe = ttk.Frame(master=mainwin, borderwidth=1)
	if 1:
		def textOut(relist):
			reout = list(relist)
			for revar in reout:
				mainText.insert("end", str(revar)+"\n")
		calcFrame = ttk.Frame(master=mainMenuframe)
		if 1:
			def calcOut(non=0):
				relist, A = sffCalcDeamon(calcSpinboxA.get(), calcSpinboxB.get(), calcCombobox.get())
				textOut(relist)
				calcSpinboxA.set(A)
			calcButton = ttk.Button(master=calcFrame, text="calc", width=0, command=calcOut)
			calcButton.pack(side="left", fill="y")
			calcSpinboxA = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxA.set(0)
			calcSpinboxA.bind("<Return>", calcOut)
			calcSpinboxA.pack(side="left", padx=1)
			calcCombobox = ttk.Combobox(master=calcFrame, justify="center", values=("+", "-", "x", ":", "="), width=2)
			calcCombobox.set("+")
			calcCombobox.pack(side="left", fill="y", padx=1)
			calcSpinboxB = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxB.set(0)
			calcSpinboxB.pack(side="left", padx=1)
		calcFrame.pack(side="left", pady=1, padx=2)
		mtFrame = ttk.Frame(master=mainMenuframe)
		if 1:
			def mtOut(non=0): textOut(mathTower(mtSpinboxX.get(), mtSpinboxA.get(), mtSpinboxB.get()))
			mtButton = ttk.Button(master=mtFrame, text="mt", width=0, command=mtOut)
			mtButton.pack(side="left", fill="y")
			mtSpinboxX = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxX.set(0)
			mtSpinboxX.bind("<Return>", mtOut)
			mtSpinboxX.pack(side="left", padx=1)
			mtSpinboxA = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxA.set(0)
			mtSpinboxA.pack(side="left", padx=1)
			mtSpinboxB = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxB.set(0)
			mtSpinboxB.pack(side="left", padx=1)
		mtFrame.pack(side="left", pady=1, padx=2)
	mainMenuframe.grid(row=0, column=0, columnspan=2, sticky="we")
	mainPadFrame = ttk.Frame(master=mainwin, borderwidth=1)
	if 1:
		textLabelBig = ttk.Label(master=mainPadFrame, text="[big]")
		textLabelBig.pack(side="left", fill="y", padx=2)
		textLabelSmall = ttk.Label(master=mainPadFrame, text="[small]")
		textLabelSmall.pack(side="left", fill="y", padx=2)
		themeFrame = ttk.Frame(master=mainPadFrame)
		if 1:
			themeButton = ttk.Button(master=themeFrame, text="Тема: ", width=5, command=styling)
			themeButton.pack(side="left", fill="y", padx=1)
			themeBox = ttk.Combobox(master=themeFrame, width=10, height=6, values=style.theme_names())
			themeBox.set("plastik")
			themeBox.bind("<Return>", styling)
			themeBox.pack(side="right", fill="y", padx=1)
			style.theme_use("plastik")
		themeFrame.pack(side="right", fill="y", pady=1, padx=1)
		commandsFrame = ttk.Frame(master=mainPadFrame)
		if 1:
			if 1: # Иконки
				appImgP = tk.PhotoImage(data=\
"""R0lGODlhQABAAKECAAAA/wCq/5CQkJCQkCH+FmJ5IEFudHlFbG8gKyB3aXRoIEdJTVAAIfkEAQoA
AgAsAAAAAEAAQAAAAv6Uj6nL7Q+jnLTai7PeoPsPht5WieZJQufKdunSxuJryDZL3vqc7T5v+QlH
paHRNTkeKUojsymUQJWqqfNhvTqywy0oAA6LxaHxuGwOfxjo9PnrDrTTa5gnTr/j5Xp8XfGx99Yh
GLj3l2AIdkPG0rjC1scn83hSaRJJqGZzKdIZkgnwabm5MoqIoFjqeCjphnqguhhT6JqHBAj36tmq
6UeUKzuoGydsBlvDu6vacgqcqHwr2byKaUdd6ew7iXLNml0d3RKKza0tGg7qXc78zW0dTLt6fk7u
3m6aDhIqCD6b/69bvH7z9OETCG3br4Mm6nkjOIcdjgZcomCp6KMKRjUdGjfakOJxXJKQE0GSRNjx
pLonKp+xbAlAQ8scKmkIqGgzFZec6zLypKjlp9ChRIsaPVq0AAA7""")
				if 1:
					appImgB = tk.PhotoImage(data=\
"""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
EQR5RPn/Id5TMcUZm8wAAAAASUVORK5CYII=""")
				mainwin.iconphoto(1, appImgP)
				saveasImg16r = """#define saveas_width 16
#define saveas16_height 16
static unsigned char saveas16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x0f, 0x74, 0x14, 0x74, 0x24, 0x74, 0x24,
   0xf4, 0x27, 0x04, 0x20, 0x04, 0x00, 0xe4, 0x1b, 0x14, 0x18, 0x14, 0x7e,
   0x14, 0x7e, 0xf8, 0x18, 0x00, 0x18, 0x00, 0x00 };"""
				saveasImg32r = """#define saveas32_width 32
#define saveas32_height 32
static unsigned char saveas32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x00, 0xc0, 0xff, 0xff, 0x00,
   0x30, 0x3f, 0x30, 0x03, 0x30, 0x3f, 0x30, 0x03, 0x30, 0x3f, 0x30, 0x0c,
   0x30, 0x3f, 0x30, 0x0c, 0x30, 0x3f, 0x30, 0x0c, 0x30, 0x3f, 0x30, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00,
   0x30, 0xfc, 0xc7, 0x03, 0x30, 0xfc, 0xc7, 0x03, 0x30, 0x03, 0xc0, 0x03,
   0x30, 0x03, 0xc0, 0x03, 0x30, 0x03, 0xfc, 0x3f, 0x30, 0x03, 0xfc, 0x3f,
   0x30, 0x03, 0xfc, 0x3f, 0x30, 0x03, 0xfc, 0x3f, 0xc0, 0xff, 0xc0, 0x03,
   0xc0, 0xff, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				saveasImg16l = tk.BitmapImage(data=saveasImg16r, foreground="black")
				saveasImg16d = tk.BitmapImage(data=saveasImg16r, foreground="white")
				saveasImg32l = tk.BitmapImage(data=saveasImg32r, foreground="black")
				saveasImg32d = tk.BitmapImage(data=saveasImg32r, foreground="white")
				saveImg16r = """#define save_width 16
#define save16_height 16
static unsigned char save16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x0f, 0x74, 0x14, 0x74, 0x24, 0x74, 0x24,
   0xf4, 0x27, 0x04, 0x20, 0x04, 0x20, 0xe4, 0x27, 0x14, 0x28, 0x14, 0x28,
   0x14, 0x28, 0xf8, 0x1f, 0x00, 0x00, 0x00, 0x00 };"""
				saveImg32r = """#define save32_width 32
#define save32_height 32
static unsigned char save32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x00, 0xc0, 0xff, 0xff, 0x00,
   0x30, 0x3f, 0x30, 0x03, 0x30, 0x3f, 0x30, 0x03, 0x30, 0x3f, 0x30, 0x0c,
   0x30, 0x3f, 0x30, 0x0c, 0x30, 0x3f, 0x30, 0x0c, 0x30, 0x3f, 0x30, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x1f, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0xfc, 0x3f, 0x0c, 0x30, 0xfc, 0x3f, 0x0c, 0x30, 0x03, 0xc0, 0x0c,
   0x30, 0x03, 0xc0, 0x0c, 0x30, 0x03, 0xc0, 0x0c, 0x30, 0x03, 0xc0, 0x0c,
   0x30, 0x03, 0xc0, 0x0c, 0x30, 0x03, 0xc0, 0x0c, 0xc0, 0xff, 0xff, 0x03,
   0xc0, 0xff, 0xff, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				saveImg16l = tk.BitmapImage(data=saveImg16r, foreground="black")
				saveImg16d = tk.BitmapImage(data=saveImg16r, foreground="white")
				saveImg32l = tk.BitmapImage(data=saveImg32r, foreground="black")
				saveImg32d = tk.BitmapImage(data=saveImg32r, foreground="white")
				newImg16r = """#define new16_width 16
#define new16_height 16
static unsigned char new16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x0f, 0x04, 0x1c, 0x04, 0x3c, 0xf4, 0x3c,
   0x04, 0x20, 0xf4, 0x21, 0x04, 0x00, 0xf4, 0x19, 0x04, 0x18, 0xf4, 0x7e,
   0x04, 0x7e, 0xf8, 0x18, 0x00, 0x18, 0x00, 0x00 };"""
				newImg32r = """#define open32_width 32
#define new32_height 32
static unsigned char new32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x00, 0xc0, 0xff, 0xff, 0x00,
   0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x0f,
   0x30, 0x00, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xff, 0x03, 0x0c,
   0x30, 0xff, 0x03, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00,
   0x30, 0xff, 0xc3, 0x03, 0x30, 0xff, 0xc3, 0x03, 0x30, 0x00, 0xc0, 0x03,
   0x30, 0x00, 0xc0, 0x03, 0x30, 0xff, 0xfc, 0x3f, 0x30, 0xff, 0xfc, 0x3f,
   0x30, 0x00, 0xfc, 0x3f, 0x30, 0x00, 0xfc, 0x3f, 0xc0, 0xff, 0xc0, 0x03,
   0xc0, 0xff, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				newImg16l = tk.BitmapImage(data=newImg16r, foreground="black")
				newImg16d = tk.BitmapImage(data=newImg16r, foreground="white")
				newImg32l = tk.BitmapImage(data=newImg32r, foreground="black")
				newImg32d = tk.BitmapImage(data=newImg32r, foreground="white")
				openImg16r = """#define open16_width 16
#define open16_height 16
static unsigned char open16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x0f, 0x04, 0x1c, 0x04, 0x3c, 0xf4, 0x3c,
   0x04, 0x20, 0xf4, 0x27, 0x04, 0x20, 0xf4, 0x27, 0x04, 0x20, 0xf4, 0x27,
   0x04, 0x20, 0xf8, 0x1f, 0x00, 0x00, 0x00, 0x00 };"""
				openImg32r = """#define open32_width 32
#define open32_height 32
static unsigned char open32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x00, 0xc0, 0xff, 0xff, 0x00,
   0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x0f,
   0x30, 0x00, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xff, 0x3f, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x3f, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0xc0, 0xff, 0xff, 0x03,
   0xc0, 0xff, 0xff, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				openImg16l = tk.BitmapImage(data=openImg16r, foreground="black")
				openImg16d = tk.BitmapImage(data=openImg16r, foreground="white")
				openImg32l = tk.BitmapImage(data=openImg32r, foreground="black")
				openImg32d = tk.BitmapImage(data=openImg32r, foreground="white")
				trashImg16r = """#define trash16_width 16
#define trash16_height 16
static unsigned char trash16_bits[] = {
   0x00, 0x00, 0xc0, 0x01, 0x20, 0x02, 0xfc, 0x1f, 0x08, 0x08, 0xa8, 0x0a,
   0xa8, 0x0a, 0xa8, 0x0a, 0xa8, 0x0a, 0xa8, 0x0a, 0xa8, 0x0a, 0xa8, 0x0a,
   0x08, 0x08, 0xf0, 0x07, 0x00, 0x00, 0x00, 0x00 };"""
				trashImg32r = """#define trash32_width 32
#define trash32_height 32
static unsigned char trash32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x00,
   0x00, 0xf0, 0x0f, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00,
   0xf0, 0xff, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0x0f, 0xc0, 0x00, 0x00, 0x03,
   0xc0, 0x00, 0x00, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x03, 0x00, 0xff, 0xff, 0x00,
   0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				trashImg16l = tk.BitmapImage(data=trashImg16r, foreground="black")
				trashImg16d = tk.BitmapImage(data=trashImg16r, foreground="white")
				trashImg32l = tk.BitmapImage(data=trashImg32r, foreground="black")
				trashImg32d = tk.BitmapImage(data=trashImg32r, foreground="white")
				infoImg16r = """#define info16_width 16
#define info16_height 16
static unsigned char info16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x1f, 0x0c, 0x30, 0x84, 0x21, 0x84, 0x21,
   0x04, 0x20, 0xc4, 0x21, 0x84, 0x21, 0x84, 0x21, 0x84, 0x21, 0xc4, 0x23,
   0x0c, 0x30, 0xf8, 0x1f, 0x00, 0x00, 0x00, 0x00 };"""
				infoImg32r = """#define info32_width 32
#define info32_height 32
static unsigned char info32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x03, 0xc0, 0xff, 0xff, 0x03,
   0xf0, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00, 0x0f, 0x30, 0xc0, 0x03, 0x0c,
   0x30, 0xc0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xf0, 0x03, 0x0c,
   0x30, 0xf0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c,
   0x30, 0xc0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c, 0x30, 0xc0, 0x03, 0x0c,
   0x30, 0xc0, 0x03, 0x0c, 0x30, 0xf0, 0x0f, 0x0c, 0x30, 0xf0, 0x0f, 0x0c,
   0xf0, 0x00, 0x00, 0x0f, 0xf0, 0x00, 0x00, 0x0f, 0xc0, 0xff, 0xff, 0x03,
   0xc0, 0xff, 0xff, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				infoImg16l = tk.BitmapImage(data=infoImg16r, foreground="black")
				infoImg16d = tk.BitmapImage(data=infoImg16r, foreground="white")
				infoImg32l = tk.BitmapImage(data=infoImg32r, foreground="black")
				infoImg32d = tk.BitmapImage(data=infoImg32r, foreground="white")
			if 1: # Горячие клавиши
				mainwin.bind("<F1>", xInfo)
				mainwin.bind("<Control-C>", xClear)
				mainwin.bind("<Control-S>", xSaveAs)
				mainwin.bind("<Control-s>", xSave)
				mainwin.bind("<Control-o>", xOpen)
				mainwin.bind("<Control-n>", xNew)
				mainwin.bind("<Control-plus>", xSizePlus)
				mainwin.bind("<Control-equal>", xSizePlus)
				mainwin.bind("<Control-minus>", xSizeMinus)
			infoButton = ttk.Button(master=commandsFrame, image=infoImg16l, width=0, command=xInfo)
			infoButton.pack(side="right", fill="y", padx=1)
			saveasButton = ttk.Button(master=commandsFrame, image=saveasImg16l, width=0, command=xSaveAs)
			saveasButton.pack(side="right", fill="y", padx=1)
			saveButton = ttk.Button(master=commandsFrame, image=saveImg16l, width=0, command=xSave)
			saveButton.pack(side="right", fill="y", padx=1)
			newButton = ttk.Button(master=commandsFrame, image=newImg16l, width=0, command=xNew)
			newButton.pack(side="right", fill="y", padx=1)
			openButton = ttk.Button(master=commandsFrame, image=openImg16l, width=0, command=xOpen)
			openButton.pack(side="right", fill="y", padx=1)
			clearButton = ttk.Button(master=commandsFrame, image=trashImg16l, width=0, command=xClear)
			clearButton.pack(side="right", fill="y", padx=1)
		commandsFrame.pack(side="right", fill="y", pady=1, padx=1)
	mainPadFrame.grid(row=3, column=0, columnspan=2, sticky="we")
	mainScrollY = ttk.Scrollbar(master=mainwin, orient="vertical")
	mainScrollX = ttk.Scrollbar(master=mainwin, orient="horizontal")
	mainText = tk.Text(
		master=mainwin, 
		wrap="none", 
		highlightthickness=0, 
		yscrollcommand=mainScrollY.set, 
		xscrollcommand=mainScrollX.set
	)
	mainScrollY.config(command=mainText.yview)
	mainScrollX.config(command=mainText.xview)
	mainGrip = ttk.Sizegrip(mainwin)
	mainGrip.grid(column=1, row=2)
	mainScrollY.grid(column=1, row=1, sticky="ns")
	mainScrollX.grid(column=0, row=2, sticky="we")
	mainText.grid(column=0, row=1, sticky="nsew")

	mainwin.rowconfigure(1, weight=1) # Текст
	mainwin.columnconfigure(0, weight=1) # Текст

	textLabelBig.after_idle(textLabelRefresh)
	mainwin.mainloop()

mylicense = \
"""                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>."""

if __name__ == "__main__": main() # Конец файла
