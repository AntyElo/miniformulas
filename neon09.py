import os
import os.path as ospath
import sys
import math
import time
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
yetPanels = True
meta = ""
def main():
	import tkinter as tk
	import tkinter.ttk as ttk
	import tkinter.filedialog as tkfd
	import tkinter.messagebox as tkmb
	import tkinter.colorchooser as tkcc
	import tkinter.font as tkfont
	try: 
		import ttkthemes as tth
		ttkyet = True
	except ImportError:
		ttkyet = False
	sffVer = "9.0" # Версия sff
	sffName = f"Miniformulas neon {sffVer}"
	filepath = "tmp.txt"
	filetypes = [("Все файлы", "*.*"), ("Текстовые файлы", "*.txt"), ("Файлы Python", "*.py")]
	global mathMax
	global mylicense
	if 1:
		def get_ttkthemes():
			if ttkyet == False:
				osoutcode = os.system("pip3 install -U ttkthemes")
				print(f"Скаченно [{osoutcode}]: ttkthemes\n")
				import ttkthemes as tth
				styling()
			else:
				print("ttkthemes уже установлен")
		def xInfo():
			infoWin = tk.Toplevel()
			infoWin.title("Справка")
			infoWin.geometry("500x500")
			infoFR = ttk.Frame(master=infoWin)
			if 1:
				infoBook = ttk.Notebook(master=infoFR)
				if 1:
					bookKeys = ttk.Frame(master=infoBook)
					if 1:
						keysLabel1 = ttk.Label(master=bookKeys, font=("terminal", 10), text=\
"""F1  Справка
^   Ctrl
^r  Зум иконок
^w  Мини-режим

^с  Копировать
^x  Вырезать
^v  Вставить

^A  Выделеть всё
^d  Очистить
^D  Очистить всё""")
						keysLabel1.grid(sticky="new", row=0, rowspan=2, column=0, padx=8, pady=8)
						keysLabel2 = ttk.Label(master=bookKeys, font=("terminal", 10), text=\
"""^s  Сохранить
^S  Сохранить как...
^o  Открыть
^n  Создать

^z  Назад
^Z  Вперёд
^q  Выход""")
						keysLabel2.grid(sticky="new", row=0, column=1, pady=8)
						keysGrip = ttk.Sizegrip(master=bookKeys)
						keysGrip.grid(sticky="nsew", row=1, column=1)
						bookKeys.rowconfigure(0, weight=1)
						bookKeys.columnconfigure(0, weight=1)
						bookKeys.columnconfigure(1, weight=1)
					infoBook.add(bookKeys, text="Горячие клавиши", sticky="nswe")
					bookAbout = ttk.Frame(master=infoBook)
					if 1:
						svi = sys.version_info
						metaPy = f"{svi[0]}.{svi[1]}.{svi[2]}-{svi[3]}"
						metaTk = tk.TkVersion
						metaTheme = "[tth.version_info]"
						aboutLabel = ttk.Label(master=bookAbout, font=("terminal", 10), text=\
f"""Использует:
    Python {metaPy}
    tkinter {metaTk}
    ttkthemes {metaTheme}


Версия:
    neon {sffVer}""")
						aboutLabel.grid(sticky="new", columnspan=2, padx=8, pady=8)
						aboutGrip = ttk.Sizegrip(master=bookAbout)
						aboutGrip.grid(sticky="nsew", row=1, column=1)
						aboutRule = ttk.Label(master=bookAbout, font=("terminal", 10), text="(c) 2020-2021 AntyElo")
						aboutRule.grid(sticky="nsew", row=1, padx=8)
						bookAbout.rowconfigure(0, weight=1)
						bookAbout.columnconfigure(0, weight=1)
					infoBook.add(bookAbout, text="Об программе", sticky="nswe")
					bookLicence = ttk.Frame(master=infoBook)
					if 1:
						licanceLicence = tk.Text(
							master=bookLicence, 
							wrap="none", 
							highlightthickness=False, 
							relief="flat", 
							bg = "#efefef"
						)
						licanceLicence.insert("end", mylicense)
						licanceScrollbarY = ttk.Scrollbar(master=bookLicence, orient="vertical", command=licanceLicence.yview)
						licanceScrollbarX = ttk.Scrollbar(master=bookLicence, orient="horizontal", command=licanceLicence.xview)
						licanceLicence.config(
							yscrollcommand=licanceScrollbarY.set, 
							xscrollcommand=licanceScrollbarX.set
						)
						licanceScrollbarY.grid(sticky="nswe", column=1)
						licanceScrollbarX.grid(sticky="nswe", row=1)
						licanceGrip = ttk.Sizegrip(master=bookLicence)
						licanceGrip.grid(sticky="nswe", row=1, column=1)
						licanceLicence.grid(sticky="nswe", row=0)
						bookLicence.rowconfigure(0, weight=1)
						bookLicence.columnconfigure(0, weight=1)
					infoBook.add(bookLicence, text="Лицензия", sticky="nswe")
				infoBook.grid(row=1, padx=1, pady=1, sticky="nswe")
				infoImgFr = tk.Frame(master=infoFR, background="#efefef", borderwidth=0)
				if 1:
					infoImgTop = ttk.Label(master=infoImgFr, background="#efefef", image=appTopImg, borderwidth=0)
					infoImgTop.grid(row=0, sticky="nse")
					infoImgPerl = ttk.Label(master=infoImgFr, background="#efefef", image=appPerlImg, borderwidth=0)
					infoImgPerl.grid(row=1, sticky="nswe")
				infoImgFr.columnconfigure(0, weight=1)
				infoImgFr.rowconfigure(0, weight=1)
				infoImgFr.grid(row=0, sticky="nswe")
			infoFR.columnconfigure(0, weight=1)
			infoFR.rowconfigure(1, weight=1)
			infoFR.pack(fill="both", expand=True)
		def xPanels():
			global yetPanels
			if   yetPanels == True:
				yetPanels = False
				mainMenuFrame.grid_forget()
				mainPadFrame.grid_forget()
				mainMiniFrame.grid(row=0, column=0, sticky="we")
			elif yetPanels == False:
				yetPanels = True
				mainMiniFrame.grid_forget()
				mainMenuFrame.grid(row=1, column=0, sticky="we")
				mainPadFrame.grid(row=3, column=0, sticky="we")
			else: print("TypeErorr: Не TRUE, и не FALSE")
		def reTLabel():
			textLabelStr.after(80, reTLabel)
			tlBigIns, tlSmallIns = str.split(mainText.index("insert"), ".")
			tlBigEnd = str(int(str.split(mainText.index("end"), ".")[0]) - 1)
			tlSmallEnd = str.split(mainText.index(f"{tlBigIns}.end"), ".")[1]
			textLabelStr.config(text=f"Строка: {tlBigIns} / {tlBigEnd}")
			textLabelLit.config(text=f"Символ: {tlSmallIns} / {tlSmallEnd}")
			minLabelBig.config(text=f"Строка: {tlBigIns} / {tlBigEnd}")
			minLabelSmall.config(text=f"Символ: {tlSmallIns} / {tlSmallEnd}")
			try:
				global filepath
				if cong(str(filepath), ("()", "")) == 0:
					if mainText.edit_modified(): mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]*")
					else: mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
			except NameError:
				pass
		def styling(invar="plastik"):
			if cong(invar, style.theme_names()) == 1:
				style.theme_use(invar)
				themeBox.config(values=sorted(style.theme_names(), key=str.lower))
				themeBox.set(invar)
				reImg()
		def reSize():
			global iconsize
			if   iconsize == 32: iconsize = 16
			elif iconsize == 16: iconsize = 32
			reImg()
		def reImg():
			global iconsize
			if ttkyet: sp = cong(style.current_theme, ("black", "equilux"))
			else: sp = 0
			if   sp == 1:
				if   iconsize == 16:
					infoButton.config(image=infoImg16d)
					popupButton.config(image=popupImg16d)
					saveasButton.config(image=saveasImg16d)
					saveButton.config(image=saveImg16d)
					openButton.config(image=openImg16d)
					newButton.config(image=newImg16d)
					clearButton.config(image=trashImg16d)
					clearallButton.config(image=trashallImg16d)
					undoButton.config(image=undoImg16d)
					redoButton.config(image=redoImg16d)
					minPopupButton.config(image=popupImg16d)
					minSaveasButton.config(image=saveasImg16d)
					minSaveButton.config(image=saveImg16d)
					minNewButton.config(image=newImg16d)
					minOpenButton.config(image=openImg16d)
					minRedoButton.config(image=redoImg16d)
					minUndoButton.config(image=undoImg16d)
				elif iconsize == 32:
					infoButton.config(image=infoImg32d)
					popupButton.config(image=popupImg32d)
					saveasButton.config(image=saveasImg32d)
					saveButton.config(image=saveImg32d)
					openButton.config(image=openImg32d)
					newButton.config(image=newImg32d)
					clearButton.config(image=trashImg32d)
					clearallButton.config(image=trashallImg32d)
					undoButton.config(image=undoImg32d)
					redoButton.config(image=redoImg32d)
					minPopupButton.config(image=popupImg32d)
					minSaveasButton.config(image=saveasImg32d)
					minSaveButton.config(image=saveImg32d)
					minNewButton.config(image=newImg32d)
					minOpenButton.config(image=openImg32d)
					minRedoButton.config(image=redoImg32d)
					minUndoButton.config(image=undoImg32d)
			elif sp == 0:
				if   iconsize == 16:
					infoButton.config(image=infoImg16l)
					popupButton.config(image=popupImg16l)
					saveasButton.config(image=saveasImg16l)
					saveButton.config(image=saveImg16l)
					openButton.config(image=openImg16l)
					newButton.config(image=newImg16l)
					clearButton.config(image=trashImg16l)
					clearallButton.config(image=trashallImg16l)
					undoButton.config(image=undoImg16l)
					redoButton.config(image=redoImg16l)
					minPopupButton.config(image=popupImg16l)
					minSaveasButton.config(image=saveasImg16l)
					minSaveButton.config(image=saveImg16l)
					minNewButton.config(image=newImg16l)
					minOpenButton.config(image=openImg16l)
					minRedoButton.config(image=redoImg16l)
					minUndoButton.config(image=undoImg16l)
				elif iconsize == 32:
					infoButton.config(image=infoImg32l)
					popupButton.config(image=popupImg32l)
					saveasButton.config(image=saveasImg32l)
					saveButton.config(image=saveImg32l)
					openButton.config(image=openImg32l)
					newButton.config(image=newImg32l)
					clearButton.config(image=trashImg32l)
					clearallButton.config(image=trashallImg32l)
					undoButton.config(image=undoImg32l)
					redoButton.config(image=redoImg32l)
					minPopupButton.config(image=popupImg32l)
					minSaveasButton.config(image=saveasImg32l)
					minSaveButton.config(image=saveImg32l)
					minNewButton.config(image=newImg32l)
					minOpenButton.config(image=openImg32l)
					minRedoButton.config(image=redoImg32l)
					minUndoButton.config(image=undoImg32l)
		def reBg():
			(triple, hexstr) = tkcc.askcolor(title="Цвет фона")
			if hexstr: mainText["bg"]=hexstr
		def reFg():
			(triple, hexstr) = tkcc.askcolor(title="Цвет текста")
			if hexstr: mainText["fg"]=hexstr
		def xOpen(path=""):
			try:
				global filepath
				style = tth.ThemedStyle(mainWin)
				if path != "":
					filepath = path
				else:
					filepath = tkfd.askopenfilename(
						title="Открыть фаил",
						filetypes=filetypes
					)
					if not filepath: return
				xfile = open(filepath, "r")
				xClearAll()
				mainText.insert("end", xfile.read())
				mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
			except UnicodeDecodeError:
				mainText.insert("end", "[~] Нечитемый тип файла")
			mainText.edit_reset()
			mainText.edit_modified(0)
		def xSaveAs():
			global filepath
			style = tth.ThemedStyle(mainWin)
			filepath = tkfd.asksaveasfilename(
				title="Сохранить как",
				defaultextension=".txt", 
				filetypes=filetypes
			)
			if not filepath: return 0
			try:
				xfile = open(filepath, "w")
				xfile.write(mainText.get("1.0", "end"))
				mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
				mainText.edit_reset()
				mainText.edit_modified(0)
				return 1
			except:
				mainText.insert("end", "[~] Невозможно сохранить файл")
				return 0
		def xSave():
			global filepath
			style = tth.ThemedStyle(mainWin)
			try:
				if filepath == None or cong(str(filepath), ("", "()")):
					return xSaveAs()
			except NameError:
				return xSaveAs()
			xfile = open(filepath, "w")
			xfile.write(mainText.get("1.0", "end"))
			mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
			mainText.edit_modified(0)
			return 1
		def xNew():
			global filepath
			style = tth.ThemedStyle(mainWin)
			filepath = tkfd.asksaveasfilename(
				title="Новый файл",
				defaultextension=".txt", 
				filetypes=filetypes
			)
			if not filepath: return 0
			xfile = open(filepath, "w")
			mainText.delete("1.0", "end")
			mainText.edit_reset()
			mainText.edit_modified(0)
			mainWin.title(f"{sffName} [{ospath.split(filepath)[1]}]")
			return 1
		def xKill():
			ask = tkmb.askyesnocancel(title="Выйти", message="Сохранить данные?")
			if ask == True:
				if xSave() == True:
					mainWin.destroy()
			elif ask == False:
				mainWin.destroy()
		def xPopup(event):
			rootMenu.tk_popup(event.x_root, event.y_root, 0)
			rootMenu.grab_release()
		def xCopy():
			try:
				global meta
				meta = mainText.selection_get()
				return 1
			except: 
				print("[xCopy except]")
				return 0
		def xCut():
			try:
				global meta
				if cong(1, (xCopy(), xClear())) == 1: print("[xCopy, xClear - xCut except]")
				return 1
			except: 
				return 0
		def xPaste():
			try:
				global meta
				mainText.insert("insert", meta)
				return 1
			except: 
				print("[xPaste except]")
				return 0
		def xUndo(): 
			try: 
				mainText.edit_undo()
				return 1
			except: 
				print("[xUndo except]")
				return 0
		def xRedo(): 
			try: 
				mainText.edit_redo()
				return 1
			except: 
				print("[xRedo except]")
				return 0
		def xSelect(): 
			mainText.tag_add("sel", "1.0", "end")
			mainText.mark_set(0.0, "end")
			mainText.see("insert")
		def xClearAll(): mainText.delete("1.0", "end")

		def xClear(): 
			try: 
				mainText.delete(tk.SEL_FIRST, tk.SEL_LAST)
				return 1
			except: 
				print("[xClear except]")
				return 0


	# Окно
	if ttkyet:
		mainWin = tth.ThemedTk()
		style = tth.ThemedStyle(mainWin)
	else:
		mainWin = tk.Tk()
		style = ttk.Style(mainWin)
	mainWin.geometry("600x400")
	mainWin.title(sffName)
	mainMenuFrame = ttk.Frame(master=mainWin)
	if 1:
		def textOut(relist):
			reout = list(relist)
			for revar in reout:
				mainText.insert("end", str(revar)+"\n")
		calcFrame = ttk.Frame(master=mainMenuFrame)
		if 1:
			def calcOut():
				relist, A = sffCalcDeamon(calcSpinboxA.get(), calcSpinboxB.get(), calcCombobox.get())
				textOut(relist)
				calcSpinboxA.set(A)
			calcButton = ttk.Button(master=calcFrame, text="calc", width=0, command=calcOut)
			calcButton.pack(side="left", fill="y")
			calcSpinboxA = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxA.set(0)
			calcSpinboxA.bind("<Return>", lambda non: calcOut())
			calcSpinboxA.pack(side="left", padx=1)
			calcCombobox = ttk.Combobox(master=calcFrame, justify="center", values=("+", "-", "x", ":", "="), width=2)
			calcCombobox.set("+")
			calcCombobox.pack(side="left", fill="y", padx=1)
			calcSpinboxB = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxB.set(0)
			calcSpinboxB.pack(side="left", padx=1)
		calcFrame.pack(side="left", pady=1, padx=2)
		mtFrame = ttk.Frame(master=mainMenuFrame)
		if 1:
			def mtOut(): textOut(mathTower(mtSpinboxX.get(), mtSpinboxA.get(), mtSpinboxB.get()))
			mtButton = ttk.Button(master=mtFrame, text="mt", width=0, command=mtOut)
			mtButton.pack(side="left", fill="y")
			mtSpinboxX = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxX.set(0)
			mtSpinboxX.bind("<Return>", lambda non: mtOut())
			mtSpinboxX.pack(side="left", padx=1)
			mtSpinboxA = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxA.set(0)
			mtSpinboxA.pack(side="left", padx=1)
			mtSpinboxB = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxB.set(0)
			mtSpinboxB.pack(side="left", padx=1)
		mtFrame.pack(side="left", pady=1, padx=2)
	mainMenuFrame.grid(row=1, column=0, sticky="we")
	mainPadFrame = ttk.Frame(master=mainWin)
	if 1:
		textLabelFr = ttk.Frame(master=mainPadFrame)
		if 1:
			textLabelStr = ttk.Label(master=textLabelFr, text="[big]")
			textLabelStr.pack(side="top", fill="x", expand=1, padx=1, pady=1)
			textLabelLit = ttk.Label(master=textLabelFr, text="[small]")
			textLabelLit.pack(side="bottom", fill="x", expand=1, padx=1, pady=1)
		textLabelFr.pack(side="left", fill="y", padx=3, pady=1)
		viewFrame = ttk.Frame(master=mainPadFrame, borderwidth=1)
		if 1:
			themeBox = ttk.Combobox(master=viewFrame, width=15, values=sorted(style.theme_names(), key=str.lower))
			if ttkyet: 
				themeBox.set("plastik")
				style.theme_use("plastik")
			else: themeBox.set("default")
			themeBox.bind("<Return>", lambda non: styling(themeBox.get()))
			themeButton = ttk.Button(master=viewFrame, text="Тема: ", width=7, command=lambda: styling(themeBox.get()))
			themeButton.grid(sticky="nswe", row=0, column=0, pady=1, padx=1)
			themeBox.grid(sticky="nswe", row=0, column=1, columnspan=2, pady=1, padx=1)

			mainFont = tkfont.Font(family="mono", size=12)
			fontBox = ttk.Combobox(master=viewFrame, width=10, values=sorted(tkfont.families(mainWin), key=str.lower))
			fontBox.set("mono")
			fontBox.bind("<Return>", lambda non: mainText.config(font=(fontBox.get(), sizeBox.get())))
			sizeBox = ttk.Combobox(master=viewFrame, width=3, values=list(range(32)))
			sizeBox.set("12")
			sizeBox.bind("<Return>", lambda non: mainText.config(font=(fontBox.get(), sizeBox.get())))
			fontButton = ttk.Button(master=viewFrame, text="Шрифт: ", width=7, command=lambda: mainText.config(font=(fontBox.get(), sizeBox.get())))
			fontButton.grid(sticky="nswe", row=1, column=0, pady=1, padx=1)
			fontBox.grid(sticky="nswe", row=1, column=1, pady=1, padx=1)
			sizeBox.grid(sticky="nswe", row=1, column=2, pady=1, padx=1)

			viewFrame.rowconfigure(0, weight=1)
			viewFrame.rowconfigure(1, weight=1)
			viewFrame.columnconfigure(0, weight=1)
			viewFrame.columnconfigure(1, weight=1)
			viewFrame.columnconfigure(2, weight=1)
		viewFrame.pack(side="right", fill="y")
		commandsFrame = ttk.Frame(master=mainPadFrame, borderwidth=1)
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
					appTopImg = tk.PhotoImage(data=\
"""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
HJ94QPHYQyFr1/jU1ihicY3raDRmg3Uma8oonTnr8K3vRXhxn5iVUXEcWLQw5PHHUrx7i+Rip8vB
Qy579jvs3Cd5+1xRJWkPDl+Gw//gcOBwnC/+gcN7H0hPuSjlbeGhpNKCpF9qUGbzko7P8kr63Jb7
BSyzk4GqKkUiBiO50ELKh4FBiVYCplkyRSnBwKDMFzAFSMTMgVW3m0ERAurr4JHVxhjGY8yohMyE
Sdy4YwiyPvN2T9TwsORXv47wu0MifxSEK+FfPhPyqU+kaW4OrjnzX9woeeNNlxf3zk11CymhulpR
XZ2l/S6fJx6XXLjgsGuPxxtvObyyW9KXJF+U8he7BP1DJkPl4QfTN9VTmVMPJZUS+VkkMOsTxMYL
dzI08fRpeyiTlM/Weh678fOsvTU1ioYaTcfYiZ3KHOiVzUI8Pr1r+T50dhadMwI01mpqam6/beOJ
hOLP/mmSICwMd02tmqUyM6cCFqewD4+Im7t2KSa+73Mlz909Dtt3l1Zg+PTDis99KkVLSzBlPYW4
Pl6c62pqEiE1iZC7230ef9Thye0RfvoLj+ffFnmj8uYJwbe+F6GlOeDu9puXCjunBiWTofCiarOg
PmuDUuxCqkLIa7r61R03eQjD+Tvrmm/trUkoljVr3j5bOCPkxCmzHyAen97uz8EhyfF3ZEnK+rJm
TU3i9jMonqdZvHhud/o6DlRWlL5gPf25oq83UZ6d6yTPPT2S05eKFtUcuO/dIYsX33q7iiMRTdOS
gKc+ErJ6VUDjd2L8/VjlbRde2CX4wNsRlrYFN81LmbOkM63NWdrFVtqZdchLF4quYYxUJivQWkz7
OtGYLjlRbzRl4vDzM0w0v9pbWalYu6p0M+KeI5LTZ6ZX70xrczjXnqOypK7VmpWKyipb2Mq8s5q6
WlWYago43y3o6nJu2uY6IcyZ6cXynEzPPkFHa1POKVmUSFQdgfoFatahw+ttWFatzPIHn07zQHtp
hY0TJ+VNXRaYQ4NidrIXG5TZeigAjizqMD0zD0VKqKrUlBcdl9s9JOgfkPOyntF8a28sptm8MeCu
+sJnx7rgd1sjDA5NXYQHBhxe/Z3HicuFz+6qh80bA2JRu+lnTHaWLFYsqSh81jEIh4+4ZG5S2GtM
niuK5XlQMDAw++dx3dJD6lIBt8XOdCGguSlk5XJdcoLj4JC4qQV058ygKMUED8UsyutZddoEDyUj
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""")
					appPerlImg = tk.PhotoImage(data=\
"""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
rkJggg==""")
				mainWin.iconphoto(1, appImgP)
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
				trashallImg16r = """#define trashall16_width 16
#define trashall16_height 16
static unsigned char trashall16_bits[] = {
   0x00, 0x00, 0xc0, 0x01, 0x20, 0x02, 0xfc, 0x1f, 0x08, 0x08, 0xa8, 0x0a,
   0xa8, 0x0a, 0xa8, 0x0a, 0xa8, 0x02, 0xa8, 0x1a, 0xa8, 0x18, 0xa8, 0x7e,
   0x08, 0x7e, 0xf0, 0x18, 0x00, 0x18, 0x00, 0x00 };"""
				trashallImg32r = """#define trashall32_width 32
#define trashall32_height 32
static unsigned char trashall32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x0f, 0x00,
   0x00, 0xf0, 0x0f, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00,
   0xf0, 0xff, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0x0f, 0xc0, 0x00, 0x00, 0x03,
   0xc0, 0x00, 0x00, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x31, 0x03,
   0xc0, 0x8c, 0x31, 0x03, 0xc0, 0x8c, 0x01, 0x00, 0xc0, 0x8c, 0x01, 0x00,
   0xc0, 0x8c, 0xc1, 0x03, 0xc0, 0x8c, 0xc1, 0x03, 0xc0, 0x0c, 0xc0, 0x03,
   0xc0, 0x0c, 0xc0, 0x03, 0xc0, 0x0c, 0xfc, 0x3f, 0xc0, 0x0c, 0xfc, 0x3f,
   0xc0, 0x00, 0xfc, 0x3f, 0xc0, 0x00, 0xfc, 0x3f, 0x00, 0xff, 0xc0, 0x03,
   0x00, 0xff, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03, 0x00, 0x00, 0xc0, 0x03,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				trashallImg16l = tk.BitmapImage(data=trashallImg16r, foreground="black")
				trashallImg16d = tk.BitmapImage(data=trashallImg16r, foreground="white")
				trashallImg32l = tk.BitmapImage(data=trashallImg32r, foreground="black")
				trashallImg32d = tk.BitmapImage(data=trashallImg32r, foreground="white")
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
				popupImg16r = """#define popup16_width 16
#define popup16_height 16
static unsigned char popup16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xf8, 0x1f, 0x04, 0x20, 0xd4, 0x21, 0x04, 0x20,
   0xd4, 0x23, 0x04, 0x20, 0xd4, 0x21, 0x04, 0x20, 0xd4, 0x27, 0x04, 0x20,
   0xf8, 0x23, 0x00, 0x1c, 0x00, 0x00, 0x00, 0x00 };"""
				popupImg32r = """#define popup32_width 32
#define popup32_height 32
static unsigned char popup32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x03, 0xc0, 0xff, 0xff, 0x03,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xf3, 0x03, 0x0c,
   0x30, 0xf3, 0x03, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0xf3, 0x0f, 0x0c, 0x30, 0xf3, 0x0f, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0xf3, 0x03, 0x0c, 0x30, 0xf3, 0x03, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xf3, 0x3f, 0x0c,
   0x30, 0xf3, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0xc0, 0xff, 0x0f, 0x0c, 0xc0, 0xff, 0x0f, 0x0c, 0x00, 0x00, 0xf0, 0x03,
   0x00, 0x00, 0xf0, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				popupImg16l = tk.BitmapImage(data=popupImg16r, foreground="black")
				popupImg16d = tk.BitmapImage(data=popupImg16r, foreground="white")
				popupImg32l = tk.BitmapImage(data=popupImg32r, foreground="black")
				popupImg32d = tk.BitmapImage(data=popupImg32r, foreground="white")
				undoImg16r = """#define undo16_width 16
#define undo16_height 16
static unsigned char undo16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x1f, 0x10, 0x20,
   0x08, 0x20, 0x04, 0x20, 0x04, 0x20, 0x08, 0x20, 0x10, 0x20, 0xe0, 0x1f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				undoImg32r = """#define undo32_width 32
#define undo32_height 32
static unsigned char undo32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfc, 0xff, 0x03,
   0x00, 0xfc, 0xff, 0x03, 0x00, 0x03, 0x00, 0x0c, 0x00, 0x03, 0x00, 0x0c,
   0xc0, 0x00, 0x00, 0x0c, 0xc0, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0xc0, 0x00, 0x00, 0x0c, 0xc0, 0x00, 0x00, 0x0c, 0x00, 0x03, 0x00, 0x0c,
   0x00, 0x03, 0x00, 0x0c, 0x00, 0xfc, 0xff, 0x03, 0x00, 0xfc, 0xff, 0x03,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				undoImg16l = tk.BitmapImage(data=undoImg16r, foreground="black")
				undoImg16d = tk.BitmapImage(data=undoImg16r, foreground="white")
				undoImg32l = tk.BitmapImage(data=undoImg32r, foreground="black")
				undoImg32d = tk.BitmapImage(data=undoImg32r, foreground="white")
				redoImg16r = """#define redo16_width 16
#define redo16_height 16
static unsigned char redo16_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x07, 0x04, 0x08,
   0x04, 0x10, 0x04, 0x20, 0x04, 0x20, 0x04, 0x10, 0x04, 0x08, 0xf8, 0x07,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""
				redoImg32r = """#define redo32_width 32
#define redo32_height 32
static unsigned char redo32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0x3f, 0x00,
   0xc0, 0xff, 0x3f, 0x00, 0x30, 0x00, 0xc0, 0x00, 0x30, 0x00, 0xc0, 0x00,
   0x30, 0x00, 0x00, 0x03, 0x30, 0x00, 0x00, 0x03, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x03, 0x30, 0x00, 0x00, 0x03, 0x30, 0x00, 0xc0, 0x00,
   0x30, 0x00, 0xc0, 0x00, 0xc0, 0xff, 0x3f, 0x00, 0xc0, 0xff, 0x3f, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };"""

				redoImg16l = tk.BitmapImage(data=redoImg16r, foreground="black")
				redoImg16d = tk.BitmapImage(data=redoImg16r, foreground="white")
				redoImg32l = tk.BitmapImage(data=redoImg32r, foreground="black")
				redoImg32d = tk.BitmapImage(data=redoImg32r, foreground="white")
			comTopFrame = ttk.Frame(master=commandsFrame)
			if 1:
				popupButton = ttk.Button(master=comTopFrame, image=popupImg16l, width=0)
				popupButton.bind("<Button-1>", xPopup)
				popupButton.pack(side="right", fill="y", padx=1)
				clearallButton = ttk.Button(master=comTopFrame, image=trashallImg16l, width=0, command=xClearAll)
				clearallButton.pack(side="right", fill="y", padx=1)
				clearButton = ttk.Button(master=comTopFrame, image=trashImg16l, width=0, command=xClear)
				clearButton.pack(side="right", fill="y", padx=1)
				redoButton = ttk.Button(master=comTopFrame, image=redoImg16l, width=0, command=xRedo)
				redoButton.pack(side="right", fill="y", padx=1)
				undoButton = ttk.Button(master=comTopFrame, image=undoImg16l, width=0, command=xUndo)
				undoButton.pack(side="right", fill="y", padx=1)
			comTopFrame.pack(side="top", fill="y", expand=1, pady=1, padx=1)
			comBtmFrame = ttk.Frame(master=commandsFrame)
			if 1:
				infoButton = ttk.Button(master=comBtmFrame, image=infoImg16l, width=0, command=xInfo)
				infoButton.pack(side="right", fill="y", padx=1)
				saveasButton = ttk.Button(master=comBtmFrame, image=saveasImg16l, width=0, command=xSaveAs)
				saveasButton.pack(side="right", fill="y", padx=1)
				saveButton = ttk.Button(master=comBtmFrame, image=saveImg16l, width=0, command=xSave)
				saveButton.pack(side="right", fill="y", padx=1)
				newButton = ttk.Button(master=comBtmFrame, image=newImg16l, width=0, command=xNew)
				newButton.pack(side="right", fill="y", padx=1)
				openButton = ttk.Button(master=comBtmFrame, image=openImg16l, width=0, command=xOpen)
				openButton.pack(side="right", fill="y", padx=1)
			comBtmFrame.pack(side="bottom", fill="y", expand=1, pady=1, padx=1)
		commandsFrame.pack(side="right", fill="y")
	mainPadFrame.grid(row=3, column=0, sticky="we")
	mainMiniFrame = ttk.Frame(master=mainWin)
	if 1:
		minCommandsFrame = ttk.Frame(master=mainMiniFrame, borderwidth=1)
		if 1:
			minPopupButton = ttk.Button(master=minCommandsFrame, image=popupImg16l, width=0)
			minPopupButton.bind("<Button-1>", xPopup)
			minPopupButton.pack(side="right", fill="y", padx=1)
			minSaveasButton = ttk.Button(master=minCommandsFrame, image=saveasImg16l, width=0, command=xSaveAs)
			minSaveasButton.pack(side="right", fill="y", padx=1)
			minSaveButton = ttk.Button(master=minCommandsFrame, image=saveImg16l, width=0, command=xSave)
			minSaveButton.pack(side="right", fill="y", padx=1)
			minNewButton = ttk.Button(master=minCommandsFrame, image=newImg16l, width=0, command=xNew)
			minNewButton.pack(side="right", fill="y", padx=1)
			minOpenButton = ttk.Button(master=minCommandsFrame, image=openImg16l, width=0, command=xOpen)
			minOpenButton.pack(side="right", fill="y", padx=1)
			minRedoButton = ttk.Button(master=minCommandsFrame, image=redoImg16l, width=0, command=xRedo)
			minRedoButton.pack(side="right", fill="y", padx=1)
			minUndoButton = ttk.Button(master=minCommandsFrame, image=undoImg16l, width=0, command=xUndo)
			minUndoButton.pack(side="right", fill="y", padx=1)
		minCommandsFrame.pack(side="right", fill="y", pady=1, padx=2)
		minLabelFrame = ttk.Frame(master=mainMiniFrame, borderwidth=1)
		if 1:
			minLabelBig = ttk.Label(master=minLabelFrame, text="[big]")
			minLabelBig.pack(side="left", fill="y", padx=2)
			minLabelSmall = ttk.Label(master=minLabelFrame, text="[small]")
			minLabelSmall.pack(side="left", fill="y", padx=2)
		minLabelFrame.pack(side="left", fill="y", pady=1, padx=2)
	# mainMiniFrame END

	mainTextFrame = ttk.Frame(master=mainWin)
	if 1:
		mainScrollY = ttk.Scrollbar(master=mainTextFrame, orient="vertical")
		mainScrollX = ttk.Scrollbar(master=mainTextFrame, orient="horizontal")
		mainText = tk.Text(
			master=mainTextFrame, 
			wrap="none", 
			undo=True, 
			font=mainFont, 
			highlightthickness=False, 
			relief="flat", 
			bg="#f9f9fb", 
			tabs="30p", 
			selectbackground="skyblue", 
			selectforeground="black", 
			yscrollcommand=mainScrollY.set, 
			xscrollcommand=mainScrollX.set
		)
		mainScrollY.config(command=mainText.yview)
		mainScrollX.config(command=mainText.xview)
		mainGrip = ttk.Sizegrip(mainTextFrame)
		mainGrip.grid(column=1, row=1, sticky="nsew")
		mainScrollY.grid(column=1, row=0, sticky="nsew")
		mainScrollX.grid(column=0, row=1, sticky="nsew")
		mainText.grid(column=0, row=0, sticky="nsew")

	mainTextFrame.rowconfigure(0, weight=1) # Текст
	mainTextFrame.columnconfigure(0, weight=1) # Текст
	mainTextFrame.grid(row=2, column=0, sticky="nsew")

	mainWin.rowconfigure(2, weight=1)
	mainWin.columnconfigure(0, weight=1)

	rootMenu = tk.Menu(master=mainWin)

	fileMenu = tk.Menu(master=rootMenu, tearoff=0)
	rootMenu.add_cascade(label="Файл", menu=fileMenu)
	fileMenu.add_separator()
	fileMenu.add_command(label="Сохранить", command=xSave, accelerator="Ctrl-S")
	fileMenu.add_command(label="Сохранить как...", command=xSaveAs, accelerator="Ctrl-Shift-S")
	fileMenu.add_command(label="Открыть", command=xOpen, accelerator="Ctrl-O")
	fileMenu.add_command(label="Создать", command=xNew, accelerator="Ctrl-N")
	fileMenu.add_separator()
	fileMenu.add_command(label="Выход", command=xKill, accelerator="Ctrl-Q")

	editMenu = tk.Menu(master=rootMenu, tearoff=0)
	rootMenu.add_cascade(label="Правка", menu=editMenu)
	editMenu.add_separator()
	editMenu.add_command(label="Назад", command=xUndo, accelerator="Ctrl-Z")
	editMenu.add_command(label="Вперёд", command=xRedo, accelerator="Ctrl-Shift-Z")
	editMenu.add_separator()
	editMenu.add_command(label="Вырезать", command=xClear, accelerator="Ctrl-X")
	editMenu.add_command(label="Копировать", command=xClear, accelerator="Ctrl-C")
	editMenu.add_command(label="Вставить", command=xClear, accelerator="Ctrl-V")
	editMenu.add_separator()
	editMenu.add_command(label="Выделеть всё", command=xSelect, accelerator="Ctrl-Shift-A")
	editMenu.add_command(label="Очистить", command=xClear, accelerator="Ctrl-D")
	editMenu.add_command(label="Очистить всё", command=xClearAll, accelerator="Ctrl-Shift-D")

	viewMenu = tk.Menu(master=rootMenu, tearoff=0)
	rootMenu.add_cascade(label="Вид", menu=viewMenu)
	viewMenu.add_separator()
	viewMenu.add_command(label="Выбрать цвет фона...", command=reBg)
	viewMenu.add_command(label="Выбрать цвет текста...", command=reFg)
	viewMenu.add_separator()
	themesMenu = tk.Menu(master=rootMenu, tearoff=0)
	for oneTheme in sorted(style.theme_names(), key=str.lower):
		themesMenu.add_command(label=oneTheme, command=lambda oneTheme=oneTheme: styling(oneTheme))
	viewMenu.add_cascade(label="Выбрать тему", menu=themesMenu)
	fontFamilyMenu = tk.Menu(master=rootMenu, tearoff=0)
	for option in sorted(tkfont.families(mainWin), key=str.lower):
		fontFamilyMenu.add_command(label=option, command=(lambda option=option: mainFont.config(family=option), fontBox.set(option)))
	viewMenu.add_cascade(label="Выбрать шрифт", menu=fontFamilyMenu)
	fontSizeMenu = tk.Menu(master=rootMenu, tearoff=0)
	for value in list(range(32)):
		fontSizeMenu.add_command(label=str(value), command=lambda value=value: mainFont.config(size=value))
	viewMenu.add_cascade(label="Выбрать кегль", menu=fontSizeMenu)
	viewMenu.add_separator()
	viewMenu.add_command(label="+/- размер значков", command=reSize, accelerator="Ctrl-R")
	viewMenu.add_command(label="Мини-режим", command=xPanels, accelerator="Ctrl-W")
	if ttkyet == 0: viewMenu.add_command(label="Установить ttkthemes", command=get_ttkthemes)

	rootMenu.add_command(label="Справка", command=xInfo, accelerator="F1")
	mainWin.bind("<Button-3>", xPopup)


	mainWin.bind("<F1>", lambda non: xInfo())
	mainWin.bind("<Control-S>", lambda non: xSaveAs())
	mainWin.bind("<Control-s>", lambda non: xSave())
	mainWin.bind("<Control-o>", lambda non: xOpen())
	mainWin.bind("<Control-n>", lambda non: xNew())
	mainWin.bind("<Control-q>", lambda non: xKill())
	mainWin.bind("<Control-r>", lambda non: reSize())
	mainWin.bind("<Control-w>", lambda non: xPanels())
	mainText.bind("<Control-D>", lambda non: xClearAll())
	mainText.bind("<Control-d>", lambda non: xClear())
	mainText.bind("<Control-x>", lambda non: xCut())
	mainText.bind("<Control-c>", lambda non: xCopy())
	mainText.bind("<Control-v>", lambda non: xPaste())
	mainText.bind("<Control-A>", lambda non: xSelect())
	mainText.bind("<Control-z>", lambda non: xUndo())
	mainText.bind("<Control-Z>", lambda non: xRedo())


	textLabelStr.after_idle(reTLabel)
	mainWin.mainloop()

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
