import tkinter as tk
import time
from tkinter import filedialog

class ram:
    def __init__(self):
        """
        the idea is to save the line in an array
        every line has 3 parts
        31 TST 4
        [
        [31, "TST", 4]
        ]
        part one: line number
        part two: the command
        part three: the line to jump or the data pointer
        """

        self.lines = []

    def addLine(self, n):
        num, command, pointer = self.splitLine(n)
        self.lines.append([int(num), command.upper(), int(pointer)])

    def splitLine(self, line):
        lineNum = ""
        command = ""
        pointer = ""

        counter = 0
        for i in line:
            if i == " ":
                counter += 1
            elif counter == 0:
                lineNum += str(i)
            elif counter == 1:
                command += str(i)
            elif counter == 2:
                pointer += str(i)

        return lineNum, command, pointer

    def print(self):
        for item in self.lines:
            print(item)

    def clear(self):
        self.lines = []

    def show(self, main):

        for i in main.ram.lines:
            line = f"{i[0]} {i[1]} {i[2]}"

            main.output.insert(tk.END, f"{line}\n")

        main.output.update()

    def comp(self, main):
        self.sort()

        main.output.insert(tk.END, "CODE: \n")
        self.show(main)

        main.output.insert(tk.END, "\nRUN: \n")
        main.output.update()

        count = 0
        skipNxt = False

        main.runtime = True

        while count < len(self.lines) and main.runtime:

            if skipNxt:
                count += 1
                skipNxt = False

            line = self.lines[count]
            time.sleep(0.1)

            output_line = f"{line[0]} {line[1]} {line[2]}"
            main.output.insert(tk.END, f"{output_line}\n")
            main.output.update()

            if line[1] == "TST":
                index = self.search(line[2], 0)

                if self.lines[index][2] == 0:
                    skipNxt = True

            elif line[1] == "JMP":
                index = self.search(line[2], 0)
                count = index - 1

            elif line[1] == "DEC":
                index = self.search(line[2], 0)
                self.lines[index][2] -= 1

                check = f"{self.lines[index][0]} {self.lines[index][1]} {self.lines[index][2] + 1} -> {self.lines[index][0]} {self.lines[index][1]} {self.lines[index][2]}"
                main.output.insert(tk.END, f"{check}\n\n")
                main.output.update()

            elif line[1] == "INC":
                index = self.search(line[2], 0)
                self.lines[index][2] += 1

                check = f"{self.lines[index][0]} {self.lines[index][1]} {self.lines[index][2] - 1} -> {self.lines[index][0]} {self.lines[index][1]} {self.lines[index][2]}"
                main.output.insert(tk.END, f"{check}\n\n")
                main.output.update()

            elif line[1] == "HLT":
                break
            count += 1

        main.output.insert(tk.END, "\nEXECUTED CODE: \n")
        self.show(main)

        main.output.insert(tk.END, "\nProcess finished with exit code 0 - MURM \n")
        main.output.update()

        print("Process finished with exit code 0 - MURM")

    def sort(self):
        n = len(self.lines)
        swapped = False

        for i in range(n - 1):

            for j in range(0, n - i - 1):
                if self.lines[j][0] > self.lines[j + 1][0]:
                    swapped = True
                    self.lines[j], self.lines[j + 1] = self.lines[j + 1], self.lines[j]

            if not swapped:
                return

    def search(self, value, index):
        obj_index = 0
        found = False
        for line in self.lines:
            if line[index] == value:
                found = True
                break

            obj_index += 1

        if not found:
            return None

        return obj_index


class ide:
    def __init__(self):
        self.runtime = False
        self.ram = ram()
        self.console_output = ""

        self.root = tk.Tk()
        self.root.title("MRML - compiler")

        self.canvas = tk.Canvas(height=900, width=900, bg="#202020")
        self.canvas.pack()

        # <tool bar>

        self.toolbar = tk.Canvas(self.canvas, bg="Red")
        self.toolbar.place(relx=0, rely=0, relwidth=1, relheight=0.05)

        self.saveButton = tk.Button(self.toolbar, bg="Blue", command=lambda : self.saveProgram())
        self.saveButton.place(relx=0, rely=0, relwidth=0.05, relheight=1)

        self.loadButton = tk.Button(self.toolbar, bg="Green", command=lambda : self.loadProgram())
        self.loadButton.place(relx=0.05, rely=0, relwidth=0.05, relheight=1)

        # </toolbar end>

        self.inputField = tk.Text(self.canvas, bg="#0f0f0f", bd=1, fg="#ffffff", insertbackground='white')
        self.inputField.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.8)

        self.compileButton = tk.Button(self.canvas, text="execute", font=(15), command=lambda: self.compile(), bg="#599fd7", fg="#ffffff")
        self.compileButton.place(relx=0.6, rely=0.85, relwidth=0.15, relheight=0.05)

        self.stopButton = tk.Button(self.canvas, text="stop", font=(15), command=lambda : self.stop(), bg="#599fd7", fg="#ffffff")
        self.stopButton.place(relx=0.75, rely=0.85, relwidth=0.15, relheight=0.05)

        self.output = tk.Text(self.canvas, bg="#0f0f0f", bd=1, fg="#ffffff", insertbackground='white')
        self.output.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.75)

        self.root.mainloop()

    def loadProgram(self):
        filePath = filedialog.askopenfilename()
        file = open(filePath)
        openFile = file.readlines()

        for line in openFile:
            self.inputField.insert(tk.END, line)

        self.inputField.update()

    def saveProgram(self):
        filePath = filedialog.askopenfilename()
        file = open(filePath, "w+")
        file.write(self.inputField.get("1.0", "end-1c"))
        file.close()

    def stop(self):
        self.runtime = False

    def clean(self):
        """
        cuts of \n of the front and the end
        """

        code = list(self.inputField.get("1.0", "end-1c"))

        for i in range(2):
            cut = 0
            switch = False
            for i, c in enumerate(code):
                if switch:
                    break
                if c != '\n':
                    cut = i
                    switch = True

            code = code[cut::]
            code = code[::-1]

        return code

    def compile(self):
        self.output.delete('1.0', tk.END)

        self.ram.clear()
        line = ""

        code = self.clean()

        for i in code:
            if i == '\n':
                self.ram.addLine(line)
                line = ""

            else:
                line += str(i)


        self.ram.addLine(line)
        self.ram.print()
        self.ram.comp(self)


if __name__ == '__main__':
    main = ide()
