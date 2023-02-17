import time

"""
compiles a easy form of assembly
INC
DEC
TST
JMP
HLT
VAR
"""


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

    def comp(self):
        self.sort()

        count = 0
        skipNxt = False
        while count < len(self.lines):

            if skipNxt:
                count += 1
                skipNxt = False

            line = self.lines[count]
            time.sleep(0.1)

            print(line)

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

            elif line[1] == "INC":
                index = self.search(line[2], 0)

                self.lines[index][2] += 1

            elif line[1] == "HLT":
                break
            count += 1

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

    def insertLines(self):
        pass



def inputLoop():
    run = True
    while run:
        i = input(":")
        if i.lower() == "print":
            ram.print()
            pass
        elif i.lower() == "comp":
            ram.comp()
        elif i.lower() == "sort":
            ram.sort()
            ram.print()
        elif i.lower() == "stop":
            run = False
        else:
            ram.addLine(i)

def load_program():

    f = open("main.txt")

    lines = f.readlines()

    for line in lines:
        # print(line)
        ram.addLine(line)

    inputLoop()

def main():
    inputLoop()

if __name__ == '__main__':
    ram = ram()
    # main()
    load_program()