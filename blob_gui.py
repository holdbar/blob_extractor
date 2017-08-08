# -*- coding: utf-8 -*-

from tkinter import *





with open("blob_extractor.conf", "r") as config_file:
    configs = config_file.readlines()

    for line in configs:
        config = line.rstrip("\n")
        if "server" in line:
            server = config[config.index("=") + 1:]
        if "user" in line:
            user = config[config.index("=") + 1:]
        if "password" in line:
            password = config[config.index("=") + 1:]
        if "connection_string" in line:
            connection_string = config[config.index("=") + 1:]
        if "base_list" in line:
            base_list = config[config.index("=") + 1:].split(",")
        if "table_list" in line:
            table_list = config[config.index("=") + 1:].split(",")
        if "blob_field_list" in line:
            blob_field_list = config[config.index("=") + 1:].split(",")
        if "filter_field_list" in line:
            filter_field_list = config[config.index("=") + 1:].split(",")
# connection_string = connection_string % (server, database, user, password)



def inserter(value):
    """Inserts specified value into next widget."""
    
    output.delete("", "end")
    output.insert("", value)


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
base_var = StringVar()
base = OptionMenu(frame, base_var, *base_list)
base.grid(row=1, column=1, padx=(10, 0))
# text label
base_label = Label(frame, text="Choose db").grid(row=1, column=2)

# table field (table)
table_var = StringVar()
table = OptionMenu(frame, table_var, *table_list)
table.grid(row=1, column=3)
# text label
table_label = Label(frame, text="Choose table").grid(row=1, column=4)

# unique filter field (unique_filter)
unique_filter_var = StringVar()
unique_filter = OptionMenu(frame, unique_filter_var, *filter_field_list)
unique_filter.grid(row=1, column=5)
# text label
unique_filter_label = Label(frame, text="Choose filter field").grid(row=1, column=6)

# blob field (blob)
blob_var = StringVar()
blob = OptionMenu(frame, blob_var, *blob_field_list)
blob.grid(row=1, column=7)
# text label
blob = Label(frame, text="Choose field to extract from").grid(row=1, column=8)

# filename field (name)
name = Entry(frame, width=15)
name.grid(row=2, column=1, padx=(10, 0))
# text label
name_label = Label(frame, text="Enter filename(with extension)").grid(row=2, column=2) 





# extract button
but = Button(frame, text="Extract", command=handler).grid(row=1, column=9, padx=(10, 0))

# result space
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=3, columnspan=8)





# run main window
root.mainloop()
