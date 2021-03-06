from tkinter import *
import tkinter.font as font


# This function is used by the showOC Button Widget
# Pre-condition: All cells must be filled with correct Value Types
# Post-condition: When clicked on for an odd number of times, it will display the Opportunity Costs
# Post-condition: When clicked on for an even number of times, it will display the user's original Numerical Inputs
def change():
    if check and calc_press:
        global count
        count = count + 1
        # This if-statement occurs when you click on the showOC button for an odd number of times
        if count % 2 == 1:
            showOC.config(text="Back")
            a.delete(0, "end")
            b.delete(0, "end")
            c.delete(0, "end")
            d.delete(0, "end")
            a.insert(0, "OC: " + str(round(ocA, 3)))
            b.insert(0, "OC: " + str(round(ocB, 3)))
            c.insert(0, "OC: " + str(round(ocC, 3)))
            d.insert(0, "OC: " + str(round(ocD, 3)))
            a.config(fg='white', state='readonly', readonlybackground='grey')
            b.config(fg='white', state='readonly', readonlybackground='grey')
            c.config(fg='white', state='readonly', readonlybackground='grey')
            d.config(fg='white', state='readonly', readonlybackground='grey')
        # This if-statement occurs when you click on the showOC button for an even number of times
        if count % 2 == 0:
            showOC.config(text="Show O.C.")
            a.config(bg='#ededed', fg='black', state='normal')
            b.config(bg='#ededed', fg='black', state='normal')
            c.config(bg='#ededed', fg='black', state='normal')
            d.config(bg='#ededed', fg='black', state='normal')
            a.delete(0, "end")
            b.delete(0, "end")
            c.delete(0, "end")
            d.delete(0, "end")
            a.insert(0, aList[-1])
            b.insert(0, bList[-1])
            c.insert(0, cList[-1])
            d.insert(0, dList[-1])


#  Function that occurs when you Focus In on Person A
def personA_click(event):
    if personA.get() == 'Enter Name':
        personA.delete(0, "end")  # delete all the text in the entry
        personA.insert(0, '')  # Insert blank for user input
        personA.config(fg='black')


#  Function that occurs when you Focus Out on Person A
def personA_focus_out(event):
    if personA.get() == '':
        personA.insert(0, 'Enter Name')
        personA.config(fg='grey')


#  Function that occurs when you Focus In on Person B
def personB_click(event):
    if personB.get() == 'Enter Name':
        personB.delete(0, "end")  # delete all the text in the entry
        personB.insert(0, '')  # Insert blank for user input
        personB.config(fg='black')


#  Function that occurs when you Focus Out on Person B
def personB_focus_out(event):
    if personB.get() == '':
        personB.insert(0, 'Enter Name')
        personB.config(fg='grey')


#  Function that occurs when you Focus In on Item A
def itemA_click(event):
    if itemA.get() == ' Enter Item':
        itemA.delete(0, "end")  # delete all the text in the entry
        itemA.insert(0, '')  # Insert blank for user input
        itemA.config(fg='black')


#  Function that occurs when you Focus Out on Item A
def itemA_focus_out(event):
    if itemA.get() == '':
        itemA.insert(0, ' Enter Item')
        itemA.config(fg='grey')


#  Function that occurs when you Focus In on Item B
def itemB_click(event):
    if itemB.get() == ' Enter Item':
        itemB.delete(0, "end")  # delete all the text in the entry
        itemB.insert(0, '')  # Insert blank for user input
        itemB.config(fg='black')


#  Function that occurs when you Focus Out on Item B
def itemB_focus_out(event):
    if itemB.get() == '':
        itemB.insert(0, ' Enter Item')
        itemB.config(fg='grey')


#  Pre-Condition: User must've inputted all required information
#  Post-Condition: Calculates Opportunity Costs
#  Post-Condition: The GUI will notify the user if the Numerical inputs contain Non-Numerical Characters
def calculate():
    global check  # This variable stores a boolean that checks if the user inputs the correct Value Types
    global ocA  # Opportunity cost of Cell A
    global ocB  # Opportunity cost of Cell B
    global ocC  # Opportunity cost of Cell C
    global ocD  # Opportunity cost of Cell D

    global calc_press
    calc_press = True

    if personA.get() != '' and personB.get() != '' and itemA.get() != '' and itemB.get() != '':
        if a.get().isnumeric() and b.get().isnumeric() and c.get().isnumeric() and d.get().isnumeric():
            # Calculates the Opportunity Costs for Each person with respect to the item
            ocA = int(b.get()) / int(a.get())
            ocB = int(a.get()) / int(b.get())
            ocC = int(d.get()) / int(c.get())
            ocD = int(c.get()) / int(d.get())
            check = True
            if check and a.get() != 0 and b.get() != 0 and c.get() != 0 and d.get():
                check = True
            else:
                check = False
        else:
            check = False

    # Pre-Condition: All inputs are valid in terms of their Value Types
    # Post-Condition: The GUI will notify the user which Subject has the comparative advantage over each item
    if check:
        aList.append(aS.get())
        bList.append(bS.get())
        cList.append(cS.get())
        dList.append(dS.get())

        # Simplify User Inputs to Minuscule Nomenclatures
        pA = personA.get()
        pB = personB.get()
        iA = itemA.get()
        iB = itemB.get()

        # This statement determines which Subject has a comparative advantage over Item A
        if ocA < ocC:
            # print(pA + " has a comparative advantage in creating " + iA + ".")
            answer1 = pA + " has a comparative advantage in creating " + iA + "."
        elif ocA > ocC:
            # print(pB + " has a comparative advantage in creating " + iA + ".")
            answer1 = pB + " has a comparative advantage in creating " + iA + "."
        else:
            # print("Neither " + pA + " nor " + pB + " has a comparative advantage in the production of " + iA + ".")
            answer1 = "Neither " + pA + " nor " + pB + " has a comparative advantage in the production of " + iA + "."

        # This statement determines which Subject has a comparative advantage over Item B
        if ocB < ocD:
            # print(pA + " has a comparative advantage in creating " + iB + ".")
            answer2 = pA + " has a comparative advantage in creating " + iB + "."
        elif ocB > ocD:
            # print(pB + " has a comparative advantage in creating " + iB + ".")
            answer2 = pB + " has a comparative advantage in creating " + iB + "."
        else:
            # print("Neither " + pA + " nor " + pB + " has a comparative advantage in the production of " + iB + ".")
            answer2 = "Neither " + pA + " nor " + pB + " has a comparative advantage in the production of " + iB + "."

        answerMessage1.config(text=answer1)
        answerMessage2.config(text=answer2)
        errorMessage.config(text="")
    else:
        errorMessage.config(text="Please Input Numbers Only", fg="red")
        answerMessage1.config(text="")
        answerMessage2.config(text="")


root = Tk()  # Creates the Window named root
root.title("Comparative Advantage Calculator")  # Names the window
root.geometry("496x400")  # Sets the size of the window
root.resizable(height=False, width=False)  # Prevents the window from changing size

canvas = Canvas(root, bg="white", width=496, height=400).pack()  # Creates a white background behind the widgets

# Fonts
tFont = font.Font(family="Helvetica Now", size=15, weight="bold")  # Font for the Titles
bFont = font.Font(family="Helvetica Now", weight="bold")  # Font for the Buttons
aFont = font.Font(family="Helvetica Now", size=13, weight="bold")  # Font for the Answers
eFont = font.Font(family="Helvetica Now", size=15, weight="bold")  # Font for the Entries
iFont = font.Font(family="Helvetica Now", size=11, weight="bold", slant='italic')  # Font for the Instructions

# Frames
tFrame = Frame(root, bg="white", width=480, height=200)
tFrame.place(x=250, y=110, anchor=CENTER)

calc_press = False  # Stores a boolean that determines if the Calculate Button Widget had been pressed
check = False  # Stores a boolean that determines if the User Inputs are Valid in terms of Value Types
count = 0  # Counts how many times the OC Button was clicked on

instructions = "***Click on the Show O.C. Button for Opportunity Costs***"
Label(root, bg='white', fg='#5f6061', text=instructions, font=iFont).place(x=250, y=385, anchor=CENTER)
errorMessage = Message(root, font=aFont, bg="white", text="", width=400)
errorMessage.place(x=250, y=307, anchor=CENTER)
answerMessage1 = Message(root, font=aFont, bg="white", text="", width=440)
answerMessage1.place(x=250, y=275, anchor=CENTER)
answerMessage2 = Message(root, font=aFont, bg="white", text="", width=440)
answerMessage2.place(x=250, y=330, anchor=CENTER)

# Creates a Button Widget
# When this button is pressed, it will call on the change() function
showOC = Button(tFrame, font=bFont, width=10, bg='grey', fg='white', command=change)
showOC.config(text="Show O.C.")
showOC.grid(row=0, column=0)

# Person A Entry Section
personA = Entry(tFrame, font=eFont, bg="white", bd=0, width=10)
personA.insert(0, "Enter Name")
personA.bind('<FocusIn>', personA_click)
personA.bind('<FocusOut>', personA_focus_out)
personA.config(fg="grey")
personA.grid(row=1, column=0, padx=13, pady=15)

# Person B Entry Section
personB = Entry(tFrame, font=tFont, bg="white", bd=0, width=10)
personB.insert(0, "Enter Name")
personB.bind('<FocusIn>', personB_click)
personB.bind('<FocusOut>', personB_focus_out)
personB.config(fg="grey")
personB.grid(row=2, column=0)

# Item A Entry Section
itemA = Entry(tFrame, font=tFont, bg="white", bd=0, width=10)
itemA.insert(0, " Enter Item")
itemA.bind('<FocusIn>', itemA_click)
itemA.bind('<FocusOut>', itemA_focus_out)
itemA.config(fg="grey")
itemA.grid(row=0, column=1, padx=15)

# Item B Entry Section
itemB = Entry(tFrame, font=tFont, bg="white", bd=0, width=10)
itemB.insert(0, " Enter Item")
itemB.bind('<FocusIn>', itemB_click)
itemB.bind('<FocusOut>', itemB_focus_out)
itemB.config(fg="grey")
itemB.grid(row=0, column=2)

aList = []  # List to hold the values from user Numerical Inputs of Cell A
bList = []  # List to hold the values from user Numerical Inputs of Cell B
cList = []  # List to hold the values from user Numerical Inputs of Cell C
dList = []  # List to hold the values from user Numerical Inputs of Cell D

# Numerical Entry of Cell A in the form of a String
aS = StringVar()
a = Entry(tFrame, textvariable=aS, font=tFont, bg="#ededed", bd=0, width=10)  # Entry for personA in respect to itemA
a.grid(row=1, column=1, padx=13, pady=25)

# Numerical Entry of Cell B in the form of a String
bS = StringVar()
b = Entry(tFrame, textvariable=bS, font=tFont, bg="#ededed", bd=0, width=10)  # Entry for personA in respect to itemB
b.grid(row=1, column=2, padx=13, pady=15)

# Numerical Entry of Cell C in the form of a String
cS = StringVar()
c = Entry(tFrame, textvariable=cS, font=tFont, bg="#ededed", bd=0, width=10)  # Entry for personB in respect to itemA
c.grid(row=2, column=1)

# Numerical Entry of Cell D in the form of a String
dS = StringVar()
d = Entry(tFrame, textvariable=dS, font=tFont, bg="#ededed", bd=0, width=10)  # Entry for personB in respect to itemB
d.grid(row=2, column=2)

# Button that runs the calculate() function
enter = Button(root, bg='black', activebackground='black', activeforeground='white', fg='white', text="Calculate",
               font=bFont, bd=2, width=40, command=calculate).place(x=250, y=215, anchor=CENTER)

root.mainloop()  # Runs the root
