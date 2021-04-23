import os
import os.path as ospath
import sys
import math
import time
try:
#	import gi	# post: pyGObject, GTk+3
	import tkinter as tk
	import tkinter.ttk as ttk
	import ttkthemes as tth
	import tkinter.filedialog as tkfd
except ImportError:
	print("ttkthemes не обнаружен. Он будет установлен через 2сек")
	time.sleep(2)
	osoutcode = os.system("pip3 install -U tkinter ttkthemes")
	print(f"Скаченно [{osoutcode}]: tkinter*, ttkthemes")
	import tkinter as tk
	import tkinter.ttk as ttk
	import ttkthemes as tth
	import tkinter.filedialog as tkfd
# Сокращенние relist (returnList) - выводимый функцией список

# Стороние функции
def xsleep(): time.sleep(0.005)
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
		if abs(a) > 1 and x != 0 and x != a*x + b:
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
		call(ValueError)
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
		invarMirrow = invar
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
		if invarMirrow == 0: relist = [f"{str(invarMirrow)} = 0"]
		elif invarMirrow == 1: relist = [f"{str(invarMirrow)} = 1"]
		else:
			revar = ""
			for forvar in inlist:
				revar = revar + "x" + str(forvar)
			revar = revar[1:]
			relist = [f"{str(invarMirrow)} = {revar}"]
		
	except ValueError:
		if meta == 0: relist = ["[Q] Данные - не числа"]
		else: relist = ["Ошибка!"]
	return relist
def reInt(invar):
	list1 = findDivisors(invar)[0]
	list2 = findMultiplier(invar, 1)[0]
	return f"{list2} <=> {list1}"
# Сама по себе программа
iconsize = 16
def main():
	sffVer = "tmp" # Версия sff
	sffSuph = "neon"
	sffName = f"Miniformulas {sffSuph}-{sffVer}"
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
				if   iconsize == 16:
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
			global filepath
			style = tth.ThemedStyle(mainwin)
			filepath = tkfd.askopenfilename(
				title="Открыть фаил",
				filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
			)
			if not filepath: return
			mainText.delete("1.0", "end")
			xfile = open(filepath, "r")
			mainText.insert("end", xfile.read())
			mainwin.title(f"{sffName} [{ospath.split(filepath)[1]}]") 
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
			filepath = str(filepath)
			if cong(filepath, ("", "()")):
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
			infoWin.geometry("400x500")
			infoImg = ttk.Label(master=infoWin, image=appImgP, width=10).grid(row=0, column=0)
			intoLbl = ttk.Label(master=infoWin, text=f"Miniformulas\n{sffSuph}-{sffVer}", font="sans 18 bold")
			intoLbl.grid(row=0, column=1, sticky="nswe")
			infoBook = ttk.Notebook(master=infoWin)
			if 1:
				bookKeys = ttk.Frame(master=infoBook)
				if 1:
					keysLabel = ttk.Label(master=bookKeys, font="sans 12", text=\
"""Горячие клавиши:
F1	Справка

ctrl-+	Зум иконок
ctrl--	Зум иконок
ctrl-C	Очистить

ctrl-с	Копировать
ctrl-x	Вырезать
ctrl-v	Вставить

ctrl-s	Сохранить
ctrl-S	Сохранить как...
ctrl-o	Открыть
ctrl-n	Создать""")
					keysLabel.grid(sticky="nswe", padx=8)
				infoBook.add(bookKeys, text="Горячие клавиши", sticky="nswe")
				bookAbout = ttk.Frame(master=infoBook)
				if 1:
					metaPy = sys.version_info
					metaTk = tk.TkVersion
					metaTheme = "[tth.version_info]"
					aboutLabel = ttk.Label(master=bookAbout, font="sans 12", text=\
f"""🄯 2020-2021 AntyElo

Использует:
    Python {metaPy[0]}.{metaPy[1]}.{metaPy[2]}-{sys.version_info[3]}
    tkinter {metaTk}
    ttkthemes {metaTheme}
    
Лицензия: """)
					aboutLabel.grid(sticky="nwe", padx=8, columnspan=2)
					aboutLicence = tk.Text(master=bookAbout, wrap="none")
					aboutLicence.insert("end", mylicense)
					aboutScrollbarY = ttk.Scrollbar(master=bookAbout, orient="vertical", command=aboutLicence.yview)
					aboutScrollbarX = ttk.Scrollbar(master=bookAbout, orient="horizontal", command=aboutLicence.xview)
					aboutLicence.config(
						yscrollcommand=aboutScrollbarY.set, 
						xscrollcommand=aboutScrollbarX.set
					)
					aboutScrollbarY.grid(sticky="ns", column=1)
					aboutScrollbarX.grid(sticky="we", row=2)
					aboutGrip = ttk.Sizegrip(master=bookAbout).grid(row=2, column=1)
					aboutLicence.grid(sticky="nswe", row=1)
					bookAbout.rowconfigure(1, weight=1)
					bookAbout.columnconfigure(0, weight=1)
				infoBook.add(bookAbout, text="Об программе", sticky="nswe")
			infoBook.grid(row=1, column=0, columnspan=2, sticky="nswe")
			infoWin.columnconfigure(1, weight=1)
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
	#mainwin["menu"] = rootMenu
	mainMenuframe = ttk.Frame(master=mainwin, borderwidth=1, relief="raised")
	if 1:
		def textOut(relist):
			reout = list(relist)
			for revar in reout:
				mainText.insert("end", str(revar)+"\n")
		reFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def reOut(non=0): textOut([reInt(reSpinbox.get())])
			reButton = ttk.Button(master=reFrame, text="re", width=0, command=reOut)
			reButton.pack(side="left", fill="y")
			reSpinbox = ttk.Spinbox(master=reFrame, from_=-mathMax, to=mathMax, width=4)
			reSpinbox.set(0)
			reSpinbox.bind("<Return>", reOut)
			reSpinbox.pack(side="right")
		reFrame.pack(side="left", pady=1)
		calcFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def calcOut(non=0):
				relist, re_a = sffCalc(calcSpinboxA.get(), calcSpinboxB.get(), calcCombobox.get())
				textOut(relist)
				calcSpinboxA.set(re_a)
				reSpinbox.set(abs(round(re_a)))
			calcButton = ttk.Button(master=calcFrame, text="calc", width=0, command=calcOut)
			calcButton.pack(side="left", fill="y")
			calcSpinboxA = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxA.set(0)
			calcSpinboxA.bind("<Return>", calcOut)
			calcSpinboxA.pack(side="left")
			calcCombobox = ttk.Combobox(master=calcFrame, justify="center", values=("+", "-", "x", ":"), width=2)
			calcCombobox.set("+")
			calcCombobox.pack(side="left", fill="y")
			calcSpinboxB = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxB.set(0)
			calcSpinboxB.pack(side="left")
		calcFrame.pack(side="left", pady=1, padx=1)
		mtFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def mtOut(non=0): textOut(mathTower(mtSpinboxX.get(), mtSpinboxA.get(), mtSpinboxB.get()))
			mtButton = ttk.Button(master=mtFrame, text="mt", width=0, command=mtOut)
			mtButton.pack(side="left", fill="y")
			mtSpinboxX = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxX.set(0)
			mtSpinboxX.bind("<Return>", mtOut)
			mtSpinboxX.pack(side="left")
			mtSpinboxA = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxA.set(0)
			mtSpinboxA.pack(side="left")
			mtSpinboxB = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxB.set(0)
			mtSpinboxB.pack(side="left")
		mtFrame.pack(side="left", pady=1, padx=1)
	mainMenuframe.grid(row=0, column=0, columnspan=2, sticky="we")
	mainPadFrame = ttk.Frame(master=mainwin, borderwidth=1, relief="raised")
	if 1:
		themeFrame = ttk.Frame(master=mainPadFrame, borderwidth=1, relief=comrel)
		if 1:
			themeButton = ttk.Button(master=themeFrame, text="Тема: ", width=5, command=styling)
			themeButton.pack(side="left", fill="y")
			themeBox = ttk.Combobox(master=themeFrame, width=10, height=6, values=style.theme_names())
			themeBox.set("scidblue")
			themeBox.bind("<Return>", styling)
			themeBox.pack(side="right", fill="y")
			style.theme_use("scidblue")
		themeFrame.pack(side="right", fill="y", pady=1, padx=2)
		commandsFrame = ttk.Frame(master=mainPadFrame, borderwidth=1, relief=comrel)
		if 1:
			if 1: # Иконки
				appImgP = tk.PhotoImage(data=\
"""R0lGODlhQABAAMIHAEBAQEBAwMBAQMBAwEDAQMDAQMDAwHBwcCH+FWJ5IEFudHlFbG8sIHdpdGgg
R0lNUAAh+QQBCgAHACwAAAAAQABAAAAD/ni63P4wykmrvTjrzbv/YCiOZGmepKCubNsCcCzPM+je
N63rNu6ru2Cs98MJhZyiUnBsAjDLovMIjfqmyIv1it1VXYSweEwui7vflnnNRmtv7DjZbcHJ7wR6
xY6P6yl8fWt/E4GCZYQShodjiRE4BZGSkQOVlpUBmZqbnAFeby6Tk5eXnaaan3U3opKklqenqXur
rAWumLCdsoC0rLcDubo8oC21trfBnLuFvaK/yZvLis2jyNCZ0hE7awbd3t2DWBjbZt/f4VPjOtzm
4GaOEORl7e6I4hfyZPQG6E7qNOza9Wvyb0ZAcwOp4FtXjl7CLKpC1Xp2zdOwiMUmWruWbA0CJI2u
KlqkkYaFMYocL86S6GsjtI4PPrYMWRGmA5nOXCaz2QBnNZopSS4EaCZWF5UU8o0xerTGUINFTTUV
akGpGKZTYXCQsQYrvKddpU4FwTWqsKZkY4Q9exSF27dw48qdS7eu3bt485pIAAA7""")
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
			infoButton.pack(side="right", fill="y")
			saveasButton = ttk.Button(master=commandsFrame, image=saveasImg16l, width=0, command=xSaveAs)
			saveasButton.pack(side="right", fill="y")
			saveButton = ttk.Button(master=commandsFrame, image=saveImg16l, width=0, command=xSave)
			saveButton.pack(side="right", fill="y")
			newButton = ttk.Button(master=commandsFrame, image=newImg16l, width=0, command=xNew)
			newButton.pack(side="right", fill="y")
			openButton = ttk.Button(master=commandsFrame, image=openImg16l, width=0, command=xOpen)
			openButton.pack(side="right", fill="y")
			clearButton = ttk.Button(master=commandsFrame, image=trashImg16l, width=0, command=xClear)
			clearButton.pack(side="right", fill="y")
		commandsFrame.pack(side="right", fill="y", pady=1, padx=1)
		textLabelBig = ttk.Label(master=mainPadFrame, text="[big]")
		textLabelBig.pack(side="left", fill="y", padx=2)
		textLabelSmall = ttk.Label(master=mainPadFrame, text="[small]")
		textLabelSmall.pack(side="left", fill="y", padx=2)
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
