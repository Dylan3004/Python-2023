import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry = Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

# przykładowy pierwszy Button
btn_1 = Button(okno, text="1", padx=20, pady=10)
btn_1['font'] = myFont
btn_1.grid(row=1, column=0)

btn_2 = Button(okno, text="2", padx=20, pady=10)
btn_2['font'] = myFont
btn_2.grid(row=1, column=1)

btn_3 = Button(okno, text="3", padx=20, pady=10)
btn_3['font'] = myFont
btn_3.grid(row=1, column=2)

btn_4 = Button(okno, text="4", padx=20, pady=10)
btn_4['font'] = myFont
btn_4.grid(row=2, column=0)

btn_5 = Button(okno, text="5", padx=20, pady=10)
btn_5['font'] = myFont
btn_5.grid(row=2, column=1)

btn_6 = Button(okno, text="6", padx=20, pady=10)
btn_6['font'] = myFont
btn_6.grid(row=2, column=2)

btn_7 = Button(okno, text="7", padx=20, pady=10)
btn_7['font'] = myFont
btn_7.grid(row=3, column=0)

btn_8 = Button(okno, text="8", padx=20, pady=10)
btn_8['font'] = myFont
btn_8.grid(row=3, column=1)

btn_9 = Button(okno, text="9", padx=20, pady=10)
btn_9['font'] = myFont
btn_9.grid(row=3, column=2)

btn_0 = Button(okno, text="0", padx=20, pady=10)
btn_0['font'] = myFont
btn_0.grid(row=4, column=0)

btn_plus = Button(okno, text="+", padx=20, pady=10)
btn_plus['font'] = myFont
btn_plus.grid(row=1, column=3)

btn_minus = Button(okno, text="-", padx=20, pady=10)
btn_minus['font'] = myFont
btn_minus.grid(row=2, column=3)

btn_multiply = Button(okno, text="*", padx=20, pady=10)
btn_multiply['font'] = myFont
btn_multiply.grid(row=3, column=3)

btn_divide = Button(okno, text="/", padx=20, pady=10)
btn_divide['font'] = myFont
btn_divide.grid(row=4, column=3)

btn_clear = Button(okno, text="C", padx=20, pady=10)
btn_clear['font'] = myFont
btn_clear.grid(row=4, column=1)

btn_equal = Button(okno, text="=", padx=20, pady=10)
btn_equal['font'] = myFont
btn_equal.grid(row=4, column=2)

# proponuje dopisywac do slownika trzy elementy:
# num_1, num_2, oper wraz z wartościami
equation = {
    "num_1": "",
    "num_2": "",
    "oper": ""
}


def mouse_button_release(event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789" and equation["oper"] == "":
        ans_entry.insert(len(ans_entry.get()), text)
        equation["num_1"] += text
        print("Pierwsza liczba", text)

    if text in "+-*/" and equation["num_1"] != "":
        equation["oper"] = text

    if text == "C":
        equation["num_1"] = ""
        equation["num_2"] = ""
        equation["oper"] = ""
        ans_entry.delete(0, len(ans_entry.get()))

    if text in "0123456789" and equation["oper"] != "":
        ans_entry.delete(0, len(ans_entry.get()))
        ans_entry.insert(len(ans_entry.get()), text)
        equation["num_2"] += text
        print("Druga liczba", text)

    if text == "=":
        if equation["oper"] == "+":
            ans_entry.delete(0, len(ans_entry.get()))
            ans_entry.insert(len(ans_entry.get()), str(float(equation["num_1"]) + float(equation["num_2"])))
            equation["num_1"] = str(float(equation["num_1"]) + float(equation["num_2"]))
            equation["num_2"] = ""
            equation["oper"] = ""

        if equation["oper"] == "-":
            ans_entry.delete(0, len(ans_entry.get()))
            ans_entry.insert(len(ans_entry.get()), str(float(equation["num_1"]) - float(equation["num_2"])))
            equation["num_1"] = str(float(equation["num_1"]) - float(equation["num_2"]))
            equation["num_2"] = ""
            equation["oper"] = ""
        if equation["oper"] == "*":
            ans_entry.delete(0, len(ans_entry.get()))
            ans_entry.insert(len(ans_entry.get()), str(float(equation["num_1"]) * float(equation["num_2"])))
            equation["num_1"] = str(float(equation["num_1"]) * float(equation["num_2"]))
            equation["num_2"] = ""
            equation["oper"] = ""
        if equation["oper"] == "/":
            if equation["num_2"] == "0":
                ans_entry.delete(0, len(ans_entry.get()))
                ans_entry.insert(len(ans_entry.get()), "Nie dziel przez 0")
                equation["num_1"] = ""
                equation["num_2"] = ""
                equation["oper"] = ""
            else:
                ans_entry.delete(0, len(ans_entry.get()))
                ans_entry.insert(len(ans_entry.get()), str(float(equation["num_1"]) / float(equation["num_2"])))
                equation["num_1"] = str(float(equation["num_1"]) / float(equation["num_2"]))
                equation["num_2"] = ""
                equation["oper"] = ""
        print("Wynik", equation["num_1"])


# sposób na reakcję
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()