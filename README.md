# MRML compiler + IDE

##### This is a IDE for a reduced Assembly language.
---
### Commands

>**JMP** - jumps to a specific line
**TST** - tests if the var is 0 or not
if it is 0 the next line is skipped 
else the next line is executed 
**DEC** - decreases the var by one
**INC** - increases the var by one 
**HLT** - stops the program 
**VAR** - defines a integer variable 

### Structure

##### [line number] [command] [pointer of line or var]

Examples: *(in samples file)*
    `10 VAR 5`
    `1 TST 10`
    `2 JMP 4`
    `3 JMP 6`
    `4 DEC 10`
    `5 JMP 1`
    `6 HLT 0`


### Usage 
> To use the IDE you have two windows.
On the left the input window where you write your code.
On the right your output window or the console.
Your programs can be saved and loades with textfiles,
the button save and load are there for this purpose

---
**credits to Bastian Nicholas Lipka**