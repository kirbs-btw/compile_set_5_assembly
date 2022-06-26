import tkinter as tk
import compiler as c


def compile(code):
    ram.clear()
    print(list(code))
    line = ""
    for i in code:
        if i == '\n':
            ram.addLine(line)
            print(line)
            line = ""
        else:
            line += str(i)

    ram.addLine(line)
    ram.print()


def main():
    root = tk.Tk()
    root.title("MRML - compiler")

    canvas = tk.Canvas(height=900, width=900)
    canvas.pack()

    inputField = tk.Text(canvas)
    inputField.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.8)

    compileButton = tk.Button(canvas, text="Run", command=lambda :compile(inputField.get("1.0", "end-1c")))
    compileButton.place(relx=0.6, rely=0.85, relwidth=0.3, relheight=0.05)

    output = tk.Canvas(canvas, bg="Black")
    output.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.75)

    root.mainloop()








if __name__ == '__main__':
    ram = c.ram()
    main()