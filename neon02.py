import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.filedialog import askopenfilename, asksaveasfilename
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
		invar = round(float(invar))
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
		invar = round(float(invar))
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
filepath = "text.txt"
xpadnew = 0
def main():
	sffVer = "neon 2" # Версия sff
	sffName = "Miniformulas "+sffVer
	global mathMax
	def styling():
		style.set_theme(themeBox.get())
		themeBox.config(values=style.theme_names())
	def xOpen():
		global filepath
		style = ThemedStyle(mainwin)
		filepath = askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")])
		if not filepath: return
		mainText.delete("1.0", tk.END)
		xfile = open(filepath, "r")
		mainText.insert(tk.END, xfile.read())
		mainwin.title(f"{sffName} - {filepath}")
	def xSaveAs():
		global filepath
		style = ThemedStyle(mainwin)
		filepath = asksaveasfilename(
			defaultextension="txt", 
			filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"), ("Файлы Python", "*.py")]
		)
		if not filepath: return
		xfile = open(filepath, "w")
		xfile.write(mainText.get("1.0", tk.END))
		mainwin.title(f"{sffName} - {filepath}")
	def xSave():
		global filepath
		style = ThemedStyle(mainwin)
		if not filepath: return
		xfile = open(filepath, "w")
		xfile.write(mainText.get("1.0", tk.END))
		mainwin.title(f"{sffName} - {filepath}")
	def xNew():
		global filepath, xpadnew
		style = ThemedStyle(mainwin)
		xpadnew += 1
		filepath = f"text{xpadnew}.txt"
		xfile = open(filepath, "w")
		mainText.delete("1.0", tk.END)
		mainwin.title(f"{sffName} - {filepath}")
	def xClear(): mainText.delete("1.0", "end")
	# Окно
	mainwin = tk.Tk()
	mainwin.geometry("600x400")
	mainwin.title(sffName)
	style = ThemedStyle(mainwin)
	mainMenuframe = ttk.Frame(master=mainwin, borderwidth=2, relief="raised")
	if 1:
		def textOut(relist):
			reout = list(relist)
			for revar in reout:
				mainText.insert("end", str(revar)+"\n")
		fdFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def fdOut(): textOut(findDivisors(fdSpinbox.get()))
			fdButton = ttk.Button(master=fdFrame, text="fd", width=3, command=fdOut)
			fdButton.pack(side="left", fill="y")
			fdSpinbox = ttk.Spinbox(master=fdFrame, from_=-mathMax, to=mathMax, width=4)
			fdSpinbox.pack(side="right")
			fdSpinbox.set(0)
		fdFrame.pack(side="left", pady=1, padx=2)
		fmFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def fmOut(): textOut(findMultiplier(fmSpinbox.get()))
			fmButton = ttk.Button(master=fmFrame, text="fm", width=3, command=fmOut)
			fmButton.pack(side="left", fill="y")
			fmSpinbox = ttk.Spinbox(master=fmFrame, from_=-mathMax, to=mathMax, width=4)
			fmSpinbox.pack(side="right")
			fmSpinbox.set(0)
		fmFrame.pack(side="left", pady=1, padx=1)
		mtFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def mtOut(): textOut(mathTower(mtSpinboxX.get(), mtSpinboxA.get(), mtSpinboxB.get()))
			mtButton = ttk.Button(master=mtFrame, text="mt", width=3, command=mtOut)
			mtButton.pack(side="left", fill="y")
			mtSpinboxX = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxX.pack(side="left")
			mtSpinboxX.set(0)
			mtSpinboxA = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxA.pack(side="left")
			mtSpinboxA.set(0)
			mtSpinboxB = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxB.pack(side="left")
			mtSpinboxB.set(0)
		mtFrame.pack(side="left", pady=1, padx=1)
		calcFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def calcOut():
				relist, re_a = sffCalc(calcSpinboxA.get(), calcSpinboxB.get(), calcCombobox.get())
				textOut(relist)
				calcSpinboxA.set(re_a)
			calcButton = ttk.Button(master=calcFrame, text="calc", width=4, command=calcOut)
			calcButton.pack(side="left", fill="y")
			calcSpinboxA = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxA.pack(side="left")
			calcSpinboxA.set(0)
			calcCombobox = ttk.Combobox(master=calcFrame, values=("+", "-", "x", ":"), width=2)
			calcCombobox.pack(side="left", fill="y")
			calcCombobox.set("+")
			calcSpinboxB = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxB.pack(side="left")
			calcSpinboxB.set(0)
		calcFrame.pack(side="left", pady=1, padx=1)
	mainMenuframe.pack(side="top", fill="x")
	mainPadFrame = ttk.Frame(master=mainwin, borderwidth=2, relief="raised")
	if 1:
		textLabelBig = ttk.Label(master=mainPadFrame, text="[big]")
		textLabelBig.pack(side="left", fill="y", padx=2)
		textLabelSmall = ttk.Label(master=mainPadFrame, text="[small]")
		textLabelSmall.pack(side="left", fill="y", padx=2)
		themeFrame = ttk.Frame(master=mainPadFrame, borderwidth=1, relief="raised")
		if 1:
			themeButton = ttk.Button(master=themeFrame, text="Тема: ", width=5, command=styling)
			themeButton.pack(side="left", fill="y")
			themeBox = ttk.Combobox(master=themeFrame, text="default", width=10, values=style.theme_names(), height=6)
			themeBox.pack(side="right", fill="y")
		themeFrame.pack(side="right", fill="y", pady=1, padx=2)
		commandsFrame = ttk.Frame(master=mainPadFrame, borderwidth=1, relief="raised")
		if 1:
			saveasButton = ttk.Button(master=commandsFrame, text="💾 ...", width=0, command=xSaveAs)
			saveasButton.pack(side="right", fill="y")
			saveButton = ttk.Button(master=commandsFrame, text="💾", width=0, command=xSave)
			saveButton.pack(side="right", fill="y")
			openButton = ttk.Button(master=commandsFrame, text="🗂", width=0, command=xOpen)
			openButton.pack(side="right", fill="y")
			newButton = ttk.Button(master=commandsFrame, text="📦", width=0, command=xNew)
			#err# newButton.pack(side="right", fill="y")
			clearButton = ttk.Button(master=commandsFrame, text="🗑", width=0, command=xClear)
			clearButton.pack(side="right", fill="y")
		commandsFrame.pack(side="right", fill="y", pady=1, padx=1)
	mainPadFrame.pack(side="bottom", fill="x")
	mainRightFrame = ttk.Frame(master=mainwin)
	mainScroll = ttk.Scrollbar(master=mainRightFrame, orient="vertical")#, length=4)
	mainText = tk.Text(master=mainwin, yscrollcommand=mainScroll.set)
	mainScroll.config(command=mainText.yview)
	mainGrip = ttk.Sizegrip(mainRightFrame).pack(side="bottom")
	mainScroll.pack(expand=True, side="top", fill="y")
	mainRightFrame.pack(side="right", fill="y")
	mainText.pack(expand=True, side="bottom", fill="both")
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
	textLabelBig.after_idle(textLabelRefresh)
	mainwin.mainloop()

if __name__ == "__main__": main() # Конец файла
