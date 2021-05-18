from tkinter import *
from tkinter import messagebox, Label
import tkinter as tk
# Programs knows where to get or receive information from

window = Tk()
window.title('BMI calculator')  # name of my window
window.geometry("600x600")  # size of the window
window["bg"] = "pink"

title = Label(window, text='Ideal Body Mass Index Calculator')  # name
title.place(x=200, y=150)  # where it is position(center)

# Rel is more flexibility to more my labels and entries around
frame = Frame(window, width=500, height=300, borderwidth=2)
frame.place(relx=0.10, rely=0.3)
frame["bg"] = "teal"

# Label and Entries. Entries are the bars you type in. labels are the names of the entry bars.
weight = Label(frame, text="Weight:")
weight.place(relx=0.0, rely=0.1)

weight_entry = Entry(frame)
weight_entry.place(relx=0.1, rely=0.1)

height = Label(frame, text="Height:")
height.place(relx=0.5, rely=0.1)

height_entry = Entry(frame)
height_entry.place(relx=0.6, rely=0.1)

gender = Label(frame, text="Gender:")
gender.place(relx=0.0, rely=0.4)

age = Label(frame, text="Age:")
age.place(relx=0.5, rely=0.4)

age_entry = Entry(frame, state="readonly")
age_entry.place(relx=0.6, rely=0.4)

bmi = Label(window, text="BMI:")
bmi.place(relx=0.3, rely=0.6)

bmi_field = Entry(window, state='readonly')
bmi_field.place(relx=0.4, rely=0.6)


# Functions for gender bar, clear button, calculate and exit button. You need to define a function before you do your
# buttons.

def activate(value):
    variable.set(value)
    if value != "Select":
        age_entry.config(state="normal")
    else:
        age_entry.config(state="readonly")


def calculate_bmi():
    try:
        int(weight_entry.get())
        int(height_entry.get())
        int(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * int(weight_entry.get())) / ((int(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            result_bmi = int(weight_entry.get()) / ((int(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * int(weight_entry.get())) / ((int(height_entry.get()) / 100) ** 2)) + (
                    0.03 * int(age_entry.get())) + 11
            result = round(result, 1)
            result_bmi = int(weight_entry.get()) / ((int(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
    except ValueError:
        messagebox.showerror(title=None, message="No gender was given or invalid entry")


def clear():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])


# Gender bar and clear, calculate and exit buttons. Buttons need to be placed under the function.

options = ["Select", "Male", "Female"]
variable = StringVar(frame)
variable.set(options[0])
gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.1, rely=0.4)

delete = Button(window, text="Clear", command=clear)
delete.place(relx=0.1, rely=0.7)

calculate = Button(window, text="Calculate your Ideal Body Mass Index", command=calculate_bmi)
calculate.place(relx=0.3, rely=0.7)

Quit = Button(window, text="Exit", command=exit)
Quit.place(relx=0.8, rely=0.7)

# Very important because without a mainloop(), the window will keep running and no results will be displayed
window.mainloop()
