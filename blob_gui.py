# -*- coding: utf-8 -*-

from tkinter import *

def solver(a,b,c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)        
    else:
        text = "The discriminant is: %s \n This equation has no solutions" % D 
    return text


def inserter(value):
	"""Inserts specified value into next widget."""
	
	output.delete("0.0", "end")
	output.insert("0.0", value)


def handler():
	"""Get the content of entries and passes result to the output area."""

	try:
		# make sure that we enterd correct values
		base_val = str(base.get())
		table_val = str(table.get())
		unique_filter_val = str(unique_filter.get())
		inserter(solver(a_val, b_val, c_val))
	except ValueError:
		inserter("Make sure you entered 3 numbers")


def clear(event):
	"""CLears entry form."""

	caller = event.widget
	caller.delete("0", "end")




# parent element
root = Tk()
# set name of window
root.title("Blob Extractor")
# set min size of window
root.minsize(500,500)
# turn of resize of window
root.resizable(width=False, height=False)

# create workspace
frame = Frame(root)
frame.grid()

# database field (base)
base = Entry(frame, width=3)
base.bind("<FocusIn>", clear)
base.grid(row=1, column=1, padx=(10, 0))
# text label
base_label = Label(frame, text="Choose db").grid(row=1, column=2)

# table field (table)
table = Entry(frame, width=3)
table.bind("<FocusIn>", clear)
table.grid(row=1, column=3)
# text label
table_label = Label(frame, text="Choose table").grid(row=1, column=4)

# unique filter field (unique_filter)
unique_filter = Entry(frame, width=3)
unique_filter.bind("<FocusIn>", clear)
unique_filter.grid(row=1, column=5)
# text label
unique_filter_label = Label(frame, text="Choose filter field").grid(row=1, column=6)

# blob field (blob)
blob = Entry(frame, width=3)
blob.bind("<FocusIn>", clear)
blob.grid(row=1, column=7)
# text label
blob = Label(frame, text="Choose field to extract from").grid(row=1, column=8)

# filename field (name)
name = Entry(frame, width=3)
name.bind("<FocusIn>", clear)
name.grid(row=2, column=1, padx=(10, 0))
# text label
name_label = Label(frame, text="Choose filename").grid(row=2, column=2) 

# extension field (extension)
extension = Entry(frame, width=3)
extension.bind("<FocusIn>", clear)
extension.grid(row=2, column=3)
# text label
extension_label = Label(frame, text="Choose file extension").grid(row=2, column=4)




# extract button
but = Button(frame, text="Extract", command=handler).grid(row=1, column=9, padx=(10, 0))

# result space
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=3, columnspan=8)

# run main window
root.mainloop()
