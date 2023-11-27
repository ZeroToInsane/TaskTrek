# Project TaskTrek
# Main File
import tkinter as tk

def main():
	# Event to add a task
	def buttonAdd_click():
		task = inputbox.get()
		print(task)

	# Main Window
	window = tk.Tk()
	window.title("TaskTrek")
	
	# Input & Button element for a new task
	inputbox = tk.Entry(window)	
	inputbox.pack()

	buttonAdd = tk.Button(window, text="Add", command=buttonAdd_click)
	buttonAdd.pack()

	window.mainloop()

if __name__ == "__main__":
	main()

