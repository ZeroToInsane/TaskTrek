# Project: TaskTrek
# Author: Mario Spörl
# File: Main File for the Project

import tkinter as tk
import json

# Main Function
def main():
    def buttonAdd_click():
        task = inputBox.get()
        if task: 
            checkedStatus = tk.BooleanVar()
            checkbox = tk.Checkbutton(frame, text=task, variable=checkedStatus)
            checkbox.pack(anchor='w')
            inputBox.delete(0, tk.END)

    def buttonSaveJson_click():
        taskList = [listBox.get(i) for i in range(listBox.size())]
        with open('aufgaben.json', 'w') as file:
            json.dump(taskList, file)
        print("Liste gespeichert!")

    def buttonLoadJson_click():
        try:
            with open('aufgaben.json', 'r') as file:
                taskList = json.load(file)
                listBox.delete(0, tk.END)
                for item in taskList:
                    listBox.insert(tk.END, item)
                print("Datei erfolgreich geladen!")
        except FileNotFoundError:
            print("Datei nicht gefunden!")

    # Main window
    window = tk.Tk()
    window.title("TaskTrek")

    # Button & Inputbox for adding new tasks 
    inputBox = tk.Entry(window)
    inputBox.pack()

    buttonAdd = tk.Button(window, text="Add", command=buttonAdd_click)
    buttonAdd.pack()

    # Frame for the tasks
    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    # To-Do-Elemente
    todos = [
        "Einkaufen gehen",
        "Hausaufgaben machen",
        "Spazieren gehen",
        "Python lernen"
    ]

    # Erstellen der Checkbuttons für jedes To-Do
    for todo in todos:
        var = tk.BooleanVar()
        check = tk.Checkbutton(frame, text=todo, variable=var)
        check.pack(anchor='w')

    buttonSaveJson = tk.Button(window, text="Save to Json", command=buttonSaveJson_click)
    buttonSaveJson.pack()

    buttonLoadJson = tk.Button(window, text="Load to Json", command=buttonLoadJson_click)
    buttonLoadJson.pack()

    window.mainloop()

# Execute the main() function
if __name__ == "__main__":
    main()

