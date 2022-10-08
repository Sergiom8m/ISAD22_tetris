import tkinter as tk
from tkinter import ttk
class Ezarpenak():

    ezarpenak = tk.Tk()
    ezarpenak.geometry('400x400')
    ezarpenak.title("Tetris jokoa")
    window.resizable(False, False)
    #ezarpenak.iconbitmap('/home/aingeru/PycharmProjects/ISAD22_tetris/Irudiak')
    espacio = ttk.Label(ezarpenak, text="")
    titulo = tk.Label(ezarpenak, text="Partidaren ezarpenak", font=("Times New Roman",25))
    titulo.pack()
    espacio.pack()

    mensaje = tk.Label(ezarpenak, text="Partidaren ezaugarriak aukera itzazu", font=("Calibri"))
    mensaje.pack()

    espacio.pack()

    titulo_abiadura = tk.Label(ezarpenak, text="Abiadura:", font=("Calibri", 14))
    titulo_abiadura.place(x=60, y= 100)

    opcion = tk.IntVar()

    #Meter Frame: TODO

    tk.Radiobutton(ezarpenak, text="Erraza", variable=opcion,value=1).place(x=50, y=140)
    tk.Radiobutton(ezarpenak, text="Ertaina", variable=opcion,value=2).place(x=130, y=140)
    tk.Radiobutton(ezarpenak, text="Zaila", variable=opcion,value=3).place(x=210, y=140)
    tk.Radiobutton(ezarpenak, text="Oso zaila", variable=opcion,value=4).place(x=280, y=140)



    titulo_tamaina = tk.Label(ezarpenak, text="Tamaina:", font=("Calibri", 14))
    titulo_tamaina.place(x=60, y=180)

    opcion2 = tk.IntVar()


    tk.Radiobutton(ezarpenak, text="Erraza", variable=opcion2, value=1).place(x=50, y=220)
    tk.Radiobutton(ezarpenak, text="Ertaina", variable=opcion2, value=2).place(x=130, y=220)
    tk.Radiobutton(ezarpenak, text="Zaila", variable=opcion2, value=3).place(x=210, y=220)
    tk.Radiobutton(ezarpenak, text="Oso zaila", variable=opcion2, value=4).place(x=280, y=220)

    buttonirten = tk.Button(ezarpenak, text="Irten", width=8, font=("Calibri"))
    buttonirten.place(x=60, y=300)
    buttonj = tk.Button(ezarpenak, text="Erregistratu", width=8, font=("Calibri"))
    buttonj.place(x=220, y=300)


    ezarpenak.mainloop()




