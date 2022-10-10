import tkinter as tk
from tkinter import ttk

class Ezarpenak():

    def __init__(self):
        super(Ezarpenak, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title("Tetris jokoa")
        self.window.resizable(False, False)

        espacio = ttk.Label(self.window, text="")
        titulo = tk.Label(self.window, text="Partidaren ezarpenak", font=("Times New Roman",25))
        titulo.pack()
        espacio.pack()

        mensaje = tk.Label(self.window, text="Partidaren ezaugarriak aukera itzazu", font=("Calibri"))
        mensaje.pack()

        espacio.pack()

        titulo_abiadura = tk.Label(self.window, text="Abiadura:", font=("Calibri", 14))
        titulo_abiadura.place(x=60, y= 100)

        opcion = tk.IntVar()



        tk.Radiobutton(self.window, text="Erraza", variable=opcion,value=1).place(x=50, y=140)
        tk.Radiobutton(self.window, text="Ertaina", variable=opcion,value=2).place(x=130, y=140)
        tk.Radiobutton(self.window, text="Zaila", variable=opcion,value=3).place(x=210, y=140)
        tk.Radiobutton(self.window, text="Oso zaila", variable=opcion,value=4).place(x=280, y=140)



        titulo_tamaina = tk.Label(self.window, text="Tamaina:", font=("Calibri", 14))
        titulo_tamaina.place(x=60, y=180)

        opcion2 = tk.IntVar()


        tk.Radiobutton(self.window, text="Erraza", variable=opcion2, value=1).place(x=50, y=220)
        tk.Radiobutton(self.window, text="Ertaina", variable=opcion2, value=2).place(x=130, y=220)
        tk.Radiobutton(self.window, text="Zaila", variable=opcion2, value=3).place(x=210, y=220)
        tk.Radiobutton(self.window, text="Oso zaila", variable=opcion2, value=4).place(x=280, y=220)

        buttonirten = tk.Button(self.window, text="Irten", width=8, font=("Calibri"))
        buttonirten.place(x=60, y=300)
        buttonj = tk.Button(self.window, text="Erregistratu", width=8, font=("Calibri"))
        buttonj.place(x=220, y=300)


        self.window.mainloop()




