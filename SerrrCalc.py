from tkinter import *
from tkinter import messagebox
import math

app = Tk()
app.title("SerrrCalc")
app.minsize(width="240", height="350")

app["bg"] = "grey"

FONT = ("Segoe UI", 15)

def addDigit(digit):
	calc["state"] = NORMAL

	value = calc.get()

	if value[0] == "0":
		value = value[1:]

	calc.delete(0, END)

	if digit == "π":
		calc.insert(0, str(value) + str(math.pi))
	else:
		calc.insert(0, str(value) + str(digit))

	calc["state"] = DISABLED

def addOperation(operation):
	calc["state"] = NORMAL

	value = calc.get()

	if operation == "÷":
		operation = "/"

	if operation == "×":
		operation = "*"

	calc.delete(0, END)
	calc.insert(0, value + operation)

	calc["state"] = DISABLED

def calculate():
	calc["state"] = NORMAL

	value = calc.get()

	if value[-1] in "//*-+":
		calc.delete(0, END)
		calc.insert(0, "Error")
	else:
		calc.delete(0, END)
		try:	
			calc.insert(0, float(eval(value)))
		except NameError:
			messagebox.showerror("Error", "Incorrect symbols")
			calc.insert(0, "0")
		except SyntaxError:
			messagebox.showerror("Error", "You made a syntax error")
			calc.insert(0, "0")
		except ZeroDivisionError:
			messagebox.showerror("Error", "Can't divide by zero")
			calc.insert(0, "0")

	calc["state"] = DISABLED

def clear():
	calc["state"] = NORMAL

	calc.delete(0, END)
	calc.insert(0, "0")

	calc["state"] = DISABLED

def createDigitButton(digitSymbol):
	global FONT

	return Button(app, text=digitSymbol, bd=1, font=FONT, bg="white", fg="black", activebackground="black", activeforeground="white", command=lambda:addDigit(digitSymbol))

def createOperationButton(operationSymbol):
	global FONT

	return Button(app, text=operationSymbol, bd=1, font=FONT, bg="lime", fg="black", activebackground="green", activeforeground="white", command=lambda:addOperation(operationSymbol))

def createCalculateButton(calcSymbol):
	global FONT

	return Button(app, text=calcSymbol, bd=1, font=FONT, bg="blue", fg="white", activebackground="purple", activeforeground="white", command=calculate)

def createClearButton(clearSymbol):
	global FONT

	return Button(app, text=clearSymbol, bd=1, font=FONT, bg="red", fg="black", activebackground="purple", activeforeground="white", command=lambda:clear())

def keyPressed(event):
	if event.char.isdigit():
		addDigit(event.char)
	elif event.char in "/*-+Pp":
		if event.char == "/":
			addOperation("÷")
		elif event.char == "*":
			addOperation("×")
		elif event.char.lower() == "p":
			addDigit("π")
		else:
			addOperation(event.char)
	elif event.char == "\r":
		calculate()
	elif event.char.lower() == "c" or event.char.lower() == "с":
		clear()
	elif event.char == "." or event.char == ",":
		addDigit(".")
	else:
		pass

calc = Entry(app, justify=RIGHT, font=FONT, width=15)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5, pady=2.5)

calc["state"] = DISABLED

createDigitButton(7).grid(row=1, column=0, stick="wens", padx=2.5, pady=2.5)
createDigitButton(8).grid(row=1, column=1, stick="wens", padx=2.5, pady=2.5)
createDigitButton(9).grid(row=1, column=2, stick="wens", padx=2.5, pady=2.5)
createDigitButton(4).grid(row=2, column=0, stick="wens", padx=2.5, pady=2.5)
createDigitButton(5).grid(row=2, column=1, stick="wens", padx=2.5, pady=2.5)
createDigitButton(6).grid(row=2, column=2, stick="wens", padx=2.5, pady=2.5)
createDigitButton(1).grid(row=3, column=0, stick="wens", padx=2.5, pady=2.5)
createDigitButton(2).grid(row=3, column=1, stick="wens", padx=2.5, pady=2.5)
createDigitButton(3).grid(row=3, column=2, stick="wens", padx=2.5, pady=2.5)
createDigitButton(0).grid(row=4, column=1, stick="wens", padx=2.5, pady=2.5)
createDigitButton(".").grid(row=4, column=0, stick="wens", padx=2.5, pady=2.5)

createOperationButton("÷").grid(row=1, column=3, stick="wens", padx=2.5, pady=2.5)
createOperationButton("×").grid(row=2, column=3, stick="wens", padx=2.5, pady=2.5)
createOperationButton("-").grid(row=3, column=3, stick="wens", padx=2.5, pady=2.5)
createOperationButton("+").grid(row=4, column=3, stick="wens", padx=2.5, pady=2.5)

createCalculateButton("=").grid(row=4, column=2, stick="wens", padx=2.5, pady=2.5)

createClearButton("C").grid(row=5, column=0, stick="wens", padx=2.5, pady=2.5)

createDigitButton("π").grid(row=5, column=1, stick="wens", padx=2.5, pady=2.5)

app.grid_columnconfigure(0, minsize=60)
app.grid_columnconfigure(1, minsize=60)
app.grid_columnconfigure(2, minsize=60)
app.grid_columnconfigure(3, minsize=60)

app.grid_rowconfigure(1, minsize=60)
app.grid_rowconfigure(2, minsize=60)
app.grid_rowconfigure(3, minsize=60)
app.grid_rowconfigure(4, minsize=60)
app.grid_rowconfigure(5, minsize=60)

app.bind("<Key>", keyPressed)

app.mainloop()