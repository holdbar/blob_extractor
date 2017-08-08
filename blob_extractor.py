# -*- coding: utf-8 -*-

import tkinter as tk


class Toolbar(tk.Frame): ...
class Output(tk.Frame): ...


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		# TODO: Implement GUI here

        self.toolbar = Toolbar(self, ...)
        self.output = Outpoot(self, ...)



        self.toolbar.pack(side="top", fill="x")
        self.output.pack(side="left", fill="y")



def main():
	root = tk.Tk()
	# set name of window
	root.title("Blob Extractor")
	# set min size of window
	root.minsize(500,500)
	# turn of resize of window
	root.resizable(width=False, height=False)

	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
		
if __name__ == "__main__":
	main()
	
