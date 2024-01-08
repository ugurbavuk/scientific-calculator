import tkinter as tk
from math import sqrt, sin, cos, tan, radians, log, factorial, pi

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Bilimsel Hesap Makinası")

        self.entry = tk.Entry(master, width=30, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3),
            ('log', 6, 0), ('exp', 6, 1), ('(', 6, 2), (')', 6, 3),
            ('π', 7, 0), ('!', 7, 1), ('C', 7, 2), ('AC', 7, 3)
        ]

        for (text, row, col) in buttons:
            if text.isdigit():
                button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.press(t), bg='lightblue')
            else:
                button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.press(t))

            button.grid(row=row, column=col)

    def press(self, key):
        current = self.entry.get()

        if key == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Hata")
        elif key == 'C':
            self.entry.delete(0, tk.END)
        elif key == 'AC':
            self.entry.delete(0, tk.END)
        elif key == '√':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(sqrt(float(current))))
        elif key == 'sin':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(sin(radians(float(current)))))
        elif key == 'cos':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(cos(radians(float(current)))))
        elif key == 'tan':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(tan(radians(float(current)))))
        elif key == 'log':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(log(float(current))))
        elif key == 'exp':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(2.718281828459045 ** float(current)))
        elif key == '!':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(factorial(int(current))))
        elif key == 'π':
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(pi))
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(current) + str(key))

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
