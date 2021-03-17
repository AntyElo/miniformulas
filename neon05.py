try:
	import os.path as ospath
	import tkinter as tk
	import tkinter.ttk as ttk
	from tkinter.filedialog import askopenfilename, asksaveasfilename
	from tkinter.messagebox import showinfo
	from ttkthemes import ThemedStyle
except:
	input("Надо предварительно скачать: \ntkinter* ttkthemes\n")
	quit()
# Сокращенние relist (returnList) - выводимый функцией список

# Стороние функции
def cong(list1, list2 = ("", " ", "  ", "   ", "    ", "     ")):
	# Сравнение списков на одинаковые элементы
	var0 = 0
	list1 = (list1, "=====")
	for var1 in list1:
		for var2 in list2:
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
		relist = [f"mathTower x={x}, a={a}, b={b}:", str(x)]
		if abs(a) > 1 and x != 0 and x != a*x + b:
			while abs(x) < mathMax:
				x = a * x + b
				relist.append(str(x))
		elif x == 0: relist.append("Ошибка mt_x   ~ [Защита от цикличного умножения] x = 0 ")
		elif abs(a) <= 1: relist.append("Ошибка mt_a   ~ [Защита от цикличного умножения] Число a между 1 и -1")
		elif x == a*x + b: relist.append("Ошибка mt_abx ~ [Защита от цикличного умножения] x = ax + b")
		return relist
	except ValueError:
		return ["Ошибка mtInt  ~ [Q] Данные - не числа"]
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
		relist = [f"sffCalc a={a} {char} b={b}:", f"=  {_re_a}"]
	except ValueError:
		_re_a = a
		relist = ["Ошибка clInt  ~ [Q] Данные - не числа"]
	except ZeroDivisionError:
		_re_a = a
		relist = ["Ошибка clZero ~ [:0] Нельзя делить на ноль"]
	return relist, _re_a
def findDivisors(invar):
	try:
		if cong(invar) == 1: invar = 0
		invar = round(abs(float(invar)))
		fd_a = 2
		fd_b = 3
		# Make D1 = i/D2 and D2 = i/D1
		fd_D1 = [1]
		fd_D2 = [invar]
		while fd_a < fd_b:
			fd_b, fd_cto = divmod(invar, fd_a)
			if fd_cto == 0:
				if fd_a != fd_b: fd_D1.append(fd_a)
				fd_D2.append(fd_b)
			fd_a += 1
		if invar == 0:
			relist = ['findDivisors: D0 = Z']
		elif invar == 1:
			relist = ["findDivisors: D1 = [1]"]
		elif invar == 2:
			relist = ["findDivisors: D2 = [1, 2]"]
		else:
			fd_D2.reverse()
			relist = [f"findDivisors: D{invar} = " + str(fd_D1 + fd_D2)]
	except ValueError:
		relist = ["Ошибка fdInt  ~ [Q] Данные - не числа"]
	return relist
def findMultiplier(invar):
	try:
		if cong(invar) == 1: invar = 0
		invar = round(abs(float(invar)))
		invarMirrow = invar
		finder = 1
		inlist = []
		while invar > 1:
			finder += 1
			mod = invar % finder
			if mod == 0:
				invar /= finder
				inlist.append(finder)
				finder = 1
		if invarMirrow == 0: relist = [f"findMultiplier: {str(invarMirrow)} = 0"]
		elif invarMirrow == 1: relist = [f"findMultiplier: {str(invarMirrow)} = 1"]
		else:
			revar = ""
			for forvar in inlist:
				revar = revar + "x" + str(forvar)
			revar = revar[1:]
			relist = [f"findMultiplier: {str(invarMirrow)} = {revar}"]
		
	except ValueError:
		relist = ["Ошибка fmInt  ~ [Q] Данные - не числа"]
	return relist
# Сама по себе программа
usedtheme = "-"
filepath = ""
iconsize = 16
def main():
	sffVer = "5" # Версия sff
	sffSuph = "neon"
	sffName = f"Miniformulas {sffSuph}-{sffVer}"
	global mathMax
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
				tlBig += tlChar
				tlChar = textList[tlIndex]
				tlIndex += 1
			while tlIndex < len(textList):
				tlChar = textList[tlIndex]
				tlSmall += tlChar
				tlIndex += 1
			textLabelBig.config(text=f"Строка: {str(tlBig)}")
			textLabelSmall.config(text=f"Символ: {str(tlSmall)}")
		def styling(non=0):
			if cong(themeBox.get(), style.theme_names()) == 1:
				global usedtheme
				usedtheme = themeBox.get()
				style.set_theme(usedtheme)
				themeBox.config(values=style.theme_names())
				imgRefresh()
		def xSizeMinus(non=0):
			global iconsize
			iconsize = 16
			imgRefresh()
		def xSizePlus(non=0):
			global iconsize
			iconsize = 32
			imgRefresh()
		def cmdsSize(non=0):
			global iconsize
			if   iconsize == 32: iconsize = 16
			elif iconsize == 16: iconsize = 32
			imgRefresh()
		def imgRefresh(non=0):
			global usedtheme
			global iconsize
			if   cong(usedtheme, ("black", "equilux")) == 1:
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
			elif cong(usedtheme, ("black", "equilux")) == 0:
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
			style = ThemedStyle(mainwin)
			filepath = askopenfilename(
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
			style = ThemedStyle(mainwin)
			filepath = asksaveasfilename(
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
			style = ThemedStyle(mainwin)
			if filepath == "":
				xSaveAs()
				return
			xfile = open(filepath, "w")
			xfile.write(mainText.get("1.0", "end"))
			mainwin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
		def xNew(non=0):
			global filepath
			style = ThemedStyle(mainwin)
			filepath = asksaveasfilename(
				title="Создать файл",
				defaultextension=".txt", 
				filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
			)
			if not filepath: return
			xfile = open(filepath, "w")
			mainText.delete("1.0", "end")
			mainwin.title(f"{sffName} [{filepath}]")
		def xInfo(non=0):
			showinfo(
				f"Справка",
				f"""Miniformulas\n{sffSuph}-{sffVer}
				Горячие клавиши:\nF1	Справка
				ctrl-[+/-]	Зум иконок\nctrl-C	Очистить
				ctrl-с	Копировать\nctrl-x	Вырезать\nctrl-v	Вставить
				ctrl-s	Сохранить\nctrl-S	Сохранить как...\nctrl-o	Открыть\nctrl-n	Создать
				🄯 2020-2021 AntyElo\nСделано на Python 3 и Tkinter"""
			)
		def xClear(non=0): mainText.delete("1.0", "end")
	# Окно
	mainwin = tk.Tk()
	mainwin.geometry("600x400")
	mainwin.title(sffName)
	style = ThemedStyle(mainwin)
	comrel = "raised"
	mainMenuframe = ttk.Frame(master=mainwin, borderwidth=1, relief="raised")
	if 1:
		def textOut(relist):
			reout = list(relist)
			for revar in reout:
				mainText.insert("end", str(revar)+"\n")
		fdFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def fdOut(non=0): textOut(findDivisors(fdSpinbox.get()))
			fdButton = ttk.Button(master=fdFrame, text="fd", width=0, command=fdOut)
			fdButton.pack(side="left", fill="y")
			fdSpinbox = ttk.Spinbox(master=fdFrame, from_=-mathMax, to=mathMax, width=4)
			fdSpinbox.set(0)
			fdSpinbox.bind("<Return>", fdOut)
			fdSpinbox.pack(side="right")
		fdFrame.pack(side="left", pady=1, padx=2)
		fmFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def fmOut(non=0): textOut(findMultiplier(fmSpinbox.get()))
			fmButton = ttk.Button(master=fmFrame, text="fm", width=0, command=fmOut)
			fmButton.pack(side="left", fill="y")
			fmSpinbox = ttk.Spinbox(master=fmFrame, from_=-mathMax, to=mathMax, width=4)
			fmSpinbox.set(0)
			fmSpinbox.bind("<Return>", fmOut)
			fmSpinbox.pack(side="right")
		fmFrame.pack(side="left", pady=1, padx=1)
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
		calcFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief=comrel)
		if 1:
			def calcOut(non=0):
				relist, re_a = sffCalc(calcSpinboxA.get(), calcSpinboxB.get(), calcCombobox.get())
				textOut(relist)
				calcSpinboxA.set(re_a)
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
"""R0lGODlhIAAgAMIBAAAA/wBE/wCI/wCZ/wC7/wDd/wBE/wBE/yH+FmJ5IEFudHlFbG8gKyB3aXRo
IEdJTVAAIfkEAQoABwAsAAAAACAAIAAAA6N4utz+MMoJib3YUpd73sdVFF45WeNYmhWRkivLpXH8
oHC9zqq+MyhBYDgEXITFI9FIABKQSyYUII1qFpZhSZvhYpzebqATviqyZfRSnWxi2eMLMUBl191n
+VxPjn/fYnFpaU59aIYfgGKHi4l5c2sEdGRMf4+QlXcYdwMDZnk+Hp2eHKGinniFphajqaqho6gR
q7GfN7CorrOmIK8evcDBwhAJADs=""")
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

if __name__ == "__main__": main() # Конец файла
