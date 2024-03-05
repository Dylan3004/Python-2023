import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar



def update_date_time():

	current_time = datetime.now()
	date_time_str.set(current_time.strftime("%A %d/%m/%Y %H:%M:%S"))
	# update co sekundę
	okno.after(1000, update_date_time)



okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości
okno.title("Kalendarz")
okno.geometry("600x400")
okno.resizable(False, False)

# utwórz StringVar()
date_time_str = tk.StringVar()


# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania
date_time_Label = Label(
		okno,
		textvariable=date_time_str,
		font=("Arial", 20),
		bg="gray",
		fg="white",
	)
date_time_Label.pack(anchor="center")

current_time = datetime.now()
# przyda się do kalendarza
# day = odczytaj przez .strftime('%d')
# month =
# year =

cal = Calendar(
	okno,
	selectmode="day",
	year=current_time.year,
	month=current_time.month,
	day=current_time.day,
)
# wstaw przez .pack poniżej zegara
cal.pack(anchor="s", pady=20)

update_date_time()

okno.mainloop()