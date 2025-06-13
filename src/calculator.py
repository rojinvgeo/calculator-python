from tkinter import Tk, Button, Entry, StringVar

class CalculatorApp:
    

    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.configure(bg="#6E9FA0")

        self.result_var = StringVar()

        self.entry = Entry(master, textvariable=self.result_var, width=16, font=('Arial', 24), bd=5, insertwidth=4, bg="powder blue", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [


        'C', '7', '8', '9',
        '4', '5', '6', '/',
        '1', '2', '3',('*'),
        '0', '=', '-', '+',
        
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, column):
        if value == 'C':
            bg_color = 'red'
            fg_color = 'white'
        elif value in ['+', '-', '*', '/', '=']:
            bg_color = "#1d2d44"  # Blue for symbols
            fg_color = 'white'
        elif value.isdigit():
            bg_color = "#00b4d8"  # Green for numbers
            fg_color = 'white'
        else:
            bg_color = 'light gray'
            fg_color = 'black'
        button = Button(
            self.master,
            text=value,
            padx=20,
            pady=20,
            font=('Arial', 18),
            bg=bg_color,
            fg=fg_color,
            command=lambda: self.on_button_click(value)
        )
        button.grid(row=row, column=column)

    

    
    def on_button_click(self, value):
        if value == 'C':
            self.result_var.set("")
        elif value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

if __name__ == "__main__":
    root = Tk()
    
    calculator = CalculatorApp(root)
    root.mainloop()