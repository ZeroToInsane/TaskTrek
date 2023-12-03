import tkinter as tk
import json

def main():
    def buttonAdd_click():
        task = inputBox.get()
        if task: 
            listBox.insert(tk.END, task)
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

    window = tk.Tk()
    window.title("TaskTrek")

    inputBox = tk.Entry(window)
    inputBox.pack()

    buttonAdd = tk.Button(window, text="Add", command=buttonAdd_click)
    buttonAdd.pack()

    listBox = tk.Listbox(window)
    listBox.pack()

    buttonSaveJson = tk.Button(window, text="Save to Json", command=buttonSaveJson_click)
    buttonSaveJson.pack()

    buttonLoadJson = tk.Button(window, text="Load to Json", command=buttonLoadJson_click)
    buttonLoadJson.pack()

    window.mainloop()

if __name__ == "__main__":
    main()

