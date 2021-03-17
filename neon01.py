import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.filedialog import askopenfilename, asksaveasfilename
# Сокращенние relist (returnList) - выводимый функцией список

# IO функции
congCommonValues = ("", " ", "  ", "   ", "    ", "     ")
def cong(list1, list2 = congCommonValues):
	# Сравнение списков на одинаковые элементы
	var0 = 0
	list1 = (list1, "=====")
	for var1 in list1:
		for var2 in list2:
			if var2 == var1:
				var0 = 1
				return 1
	if var0 == 0: return 0
def congtest():
	print("cong mind how yes%a + not%a" %(cong("a", "a"), cong("a", "b")))
	print("cong  0    in 1, 2, 3 as "+str(cong("0", ("1", "2", "3"))))
	print("cong  1    in 1, 2, 3 as "+str(cong("1", ("1", "2", "3"))))
	print("cong  2    in 1, 2, 3 as "+str(cong("2", ("1", "2", "3"))))
	print("cong  3    in 1, 2, 3 as "+str(cong("3", ("1", "2", "3"))))
	print("cong [x]   in comlist as "+str(cong("")))
	print("cong yes   in comlist as "+str(cong("yes")))
	print("cong eof   in comlist as "+str(cong("eof")))
	print("cong ex    in comlist as "+str(cong("ex")))
	print("cong exit  in comlist as "+str(cong("exit")))
	print("cong q     in comlist as "+str(cong("q")))
	print("cong quit  in comlist as "+str(cong("quit")))
	print("cong qq    in comlist as "+str(cong("qq")))
	print("comlist="+str(klist))
# Мат. функции
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
		elif x == a*x + b: relist.append("Ошибка mt_abx ~ [Защита от цикличного умножения] |a| = |b| + 1")
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
			relist = ['findDivisors: D0 = бесконечность']
		elif invar == 1:
			relist = ["findDivisors: D1 = [1]"]
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
		if invarMirrow == 0: relist = [f"findMultiplier: {str(invarMirrow)} => [0]"]
		elif invarMirrow == 1: relist = [f"findMultiplier: {str(invarMirrow)} => [1]"]
		else: relist = [f"findMultiplier: {str(invarMirrow)} => {str(inlist)}"]
		
	except ValueError:
		relist = ["Ошибка fmInt  ~ [Q] Данные - не числа"]
	return relist
# Сама по себе программа
filepath = "text.txt"
xpadnew = 0
def main():
	sffVer = "neon" # Версия sff
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
		fdFrame.pack(side="left", pady=1, padx=2)
		fmFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def fmOut(): textOut(findMultiplier(fmSpinbox.get()))
			fmButton = ttk.Button(master=fmFrame, text="fm", width=3, command=fmOut)
			fmButton.pack(side="left", fill="y")
			fmSpinbox = ttk.Spinbox(master=fmFrame, from_=-mathMax, to=mathMax, width=4)
			fmSpinbox.pack(side="right")
		fmFrame.pack(side="left", pady=1, padx=1)
		mtFrame = ttk.Frame(master=mainMenuframe, borderwidth=1, relief="raised")
		if 1:
			def mtOut(): textOut(mathTower(mtSpinboxX.get(), mtSpinboxA.get(), mtSpinboxB.get()))
			mtButton = ttk.Button(master=mtFrame, text="mt", width=3, command=mtOut)
			mtButton.pack(side="left", fill="y")
			mtSpinboxX = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxX.pack(side="left")
			mtSpinboxA = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxA.pack(side="left")
			mtSpinboxB = ttk.Spinbox(master=mtFrame, from_=-mathMax, to=mathMax, width=4)
			mtSpinboxB.pack(side="left")
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
			calcCombobox = ttk.Combobox(master=calcFrame, values=("+", "-", "x", ":"), width=2)
			calcCombobox.pack(side="left", fill="y")
			calcSpinboxB = ttk.Spinbox(master=calcFrame, from_=-mathMax, to=mathMax, width=4)
			calcSpinboxB.pack(side="left")
		calcFrame.pack(side="left", pady=1, padx=1)
	mainMenuframe.pack(side="top", fill="x")
	mainBottomFrame = ttk.Frame(master=mainwin, borderwidth=2, relief="raised")
	if 1:
		#textLabel = ttk.Label(master=mainBottomFrame, text="x.x")
		#textLabel.pack(side="left", padx=2)
		themeFrame = ttk.Frame(master=mainBottomFrame, borderwidth=1, relief="raised")
		if 1:
			themeButton = ttk.Button(master=themeFrame, text="Тема: ", width=5, command=styling)
			themeButton.pack(side="left", fill="y")
			themeBox = ttk.Combobox(master=themeFrame, text="default", width=10, values=style.theme_names())
			themeBox.pack(side="right", fill="y")
		themeFrame.pack(side="right", fill="y", pady=1, padx=2)
		commandsFrame = ttk.Frame(master=mainBottomFrame, borderwidth=1, relief="raised")
		if 1:
			saveasButton = ttk.Button(master=commandsFrame, text="💾 ...", width=4, command=xSaveAs)
			saveasButton.pack(side="right", fill="y")
			saveButton = ttk.Button(master=commandsFrame, text="💾", width=2, command=xSave)
			saveButton.pack(side="right", fill="y")
			openButton = ttk.Button(master=commandsFrame, text="🗂", width=2, command=xOpen)
			openButton.pack(side="right", fill="y")
			newButton = ttk.Button(master=commandsFrame, text="📦", width=2, command=xNew)
			newButton.pack(side="right", fill="y")
			clearButton = ttk.Button(master=commandsFrame, text="🗑", width=2, command=xClear)
			clearButton.pack(side="right", fill="y")
		commandsFrame.pack(side="right", fill="y", pady=1, padx=1)
	mainBottomFrame.pack(side="bottom", fill="x")
	mainScroll = ttk.Scrollbar(master=mainwin, orient="vertical")
	mainText = tk.Text(master=mainwin, yscrollcommand=mainScroll.set)
	mainScroll.config(command=mainText.yview)
	mainScroll.pack(side="right", fill="y")
	mainText.pack(expand=True, fill="both")
	#def textLabelRefresh(): textLabel.config(text="Строка: " + str(mainText.index("insert")))
	#textLabelRefresh()
	mainwin.mainloop()

if __name__ == "__main__": main() # Конец файла
