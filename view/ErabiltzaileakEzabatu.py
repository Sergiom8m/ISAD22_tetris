import tkinter as tk
from tkinter import *
from tkinter import ttk

# https://www.youtube.com/watch?v=0WafQCaok6g ESTA ES LA QUE ESTA PUESTA, PERO NO FUNCIONA... CREO Q ES POR LAMBDA
# https://www.youtube.com/watch?v=VmlgrrXAqb4 ESTE ES PARECIDO PERO EL LAMBDA CAMBIA....PERO TAMPOCO VA
# https://www.tutorialspoint.com/python/tk_scrollbar.htm ESTE VA PERO ES MUY SIMPLE Y NO SE SI NOS SIRVE PARA LO QUE QUEREMOS
# https://www.aprendeaprogramar.com/mod/forum/discuss.php?d=2839 ESTE CREO QUE MEZCLA LAS PRIMERAS CON LA TERCERA PERO NO LO ENTIENDO BIEN
class ErabiltzaileakEzabatu(object):

    def __init__(self):
        super(ErabiltzaileakEzabatu, self).__init__()
        window = tk.Tk()
        window.title("PASAHITZA BERRESKURATU")
        window.geometry('400x400')
        window.resizable(False, False)

        # 1 create a main frame
        nagusia = Frame(window)
        nagusia.pack(fill=BOTH, expand=1)

        # 2 create a canvas
        nire_canvas = Canvas(nagusia)
        nire_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # 3 add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(nagusia, orient=VERTICAL, command=nire_canvas.yview())
        scrollbar.pack(side=RIGHT, fill=Y)

        # 4 configure the canvas
        nire_canvas.configure(yscrollcommand=scrollbar.set)
        nire_canvas.bind('<Configure>', lambda e: nire_canvas.configure(scrollregion=nire_canvas.bbox("all")))

        # 5 create another frame inside canvas
        marko = Frame(nire_canvas)

        # 6 add that new frame to a window in the canvas
        nire_canvas.create_window((0, 0), window=marko, anchor="nw")

        for i in range(100):
            Button(marko, text=f'Erabiltzaile: {i} ').grid(row=i, column=0, pady=10, padx=10)

        window.mainloop()