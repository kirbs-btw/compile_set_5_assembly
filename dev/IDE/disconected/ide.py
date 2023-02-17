import tkinter as tk
import compiler as c


class main:
    def __init__(self):
        self.console_output = ""

        self.root = tk.Tk()
        self.root.title("MRML - compiler")

        self.canvas = tk.Canvas(height=900, width=900)
        self.canvas.pack()

        self.inputField = tk.Text(self.canvas)
        self.inputField.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.8)

        self.compileButton = tk.Button(self.canvas, text="Run", command=lambda: main.compile(self))
        self.compileButton.place(relx=0.6, rely=0.85, relwidth=0.3, relheight=0.05)

        self.output = tk.Text(self.canvas)
        self.output.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.75)

        self.root.mainloop()

    def compile(self):
        ram.clear()
        line = ""

        for i in self.inputField.get("1.0", "end-1c"):
            if i == '\n':
                ram.addLine(line)
                print(line)
                line = ""
            else:
                line += str(i)

        ram.addLine(line)
        ram.print()
        ram.comp()



if __name__ == '__main__':
    ram = c.ram()
    main = main()