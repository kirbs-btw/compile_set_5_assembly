import tkinter as tk
import time


"""
designing the output mechanism for the console 
"""

class main:
    def __init__(self):
        self.root = tk.Tk()

        self.canvas = tk.Canvas(self.root, height=900, width=900)
        self.canvas.pack()

        self.textField = tk.Text(self.canvas)
        self.textField.pack()

        self.createData()

        self.root.mainloop()



    def createData(self):
        for i in range(10):
            time.sleep(0.5)
            self.textField.insert("1.0", "TEXT\n")
            self.textField.update()



if __name__ == '__main__':
    main = main()