import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(frame, text=char, font=("Arial", 14),
                            command=calculate)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 14),
                            command=lambda c=char: press(c))
        btn.pack(side="left", expand=True, fill="both")

clear_btn = tk.Button(root, text="Clear", font=("Arial", 14), command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
