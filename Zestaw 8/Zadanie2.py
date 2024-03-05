import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog

okno = tk.Tk()
okno.title("PDF Reader")
okno.geometry("400x400")
okno.resizable(False, False)

# dodać tytuł, rozmiar

# dodać widget Text i umieściś z jakimś marginesem
text = tk.Text(okno, width=300, height=300)
text.pack()




def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
    okno.quit()
    okno.destroy()


menu_bar = tk.Menu(okno)
okno.config(menu=menu_bar)

menu_options = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_options)

menu_options.add_command(label="Open", command=open_pdf)
menu_options.add_command(label="Clear", command=clear_text)
menu_options.add_command(label="Quit", command=quit_app)



# utworzyć widget Menu i jego strukturę jak na rysunku


# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app

okno.mainloop()