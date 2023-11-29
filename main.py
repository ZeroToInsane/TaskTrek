# Project TaskTrek
# Main File
import tkinter as tk
import json

def main():
	# Event to add a task
	def buttonAdd_click():
		task = inputBox.get()
		if task: #Check if the inputBox field is empty
			listBox.insert(tk.END, task)
			inputBox.delete(0, tk.END) #Remove the content from input field
	
	# Event to save to a Json file
	def buttonSaveJson_click():
		taskList = [listBox.get(i) for i in range(listBox.size())]
		with open('aufgaben.json', 'w') as file:
			json.dump(taskList, file)
		print("Liste gespeichert!")

	# Main Window
	window = tk.Tk()
	window.title("TaskTrek")
	
	# Input & Button element for a new task
	inputBox = tk.Entry(window)	
	inputBox.pack()

	buttonAdd = tk.Button(window, text="Add", command=buttonAdd_click)
	buttonAdd.pack()

	# List for the tasks
	listBox = tk.Listbox(window)
	listBox.pack()

	# Button to save a Json file
	buttonSaveJson = tk.Button(window, text="Save to Json", command=buttonSaveJson_click)
	buttonSaveJson.pack()

	window.mainloop()

if __name__ == "__main__":
	main()

