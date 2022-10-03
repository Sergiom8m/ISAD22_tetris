import tkinter as tk

class Ezarpenak():

    ezarpenak = tk.Tk()
    ezarpenak.geometry('780x780')
    ezarpenak.title("Tetris jokoa")
    #ezarpenak.iconbitmap('/home/aingeru/PycharmProjects/ISAD22_tetris/Irudiak')

    titulo = tk.Label(ezarpenak, text="Partidaren ezarpenak", font=("Calibri",40))
    titulo.pack()

    mensaje = tk.Label(ezarpenak, text="Mesedez, partidaren ezaugarriak aukeratu")
    mensaje.pack()

    titulo_abiadura = tk.Label(ezarpenak, text="Abiadura")
    titulo_abiadura.pack()

    opcion = tk.IntVar()

    #Meter Frame: TODO

    tk.Radiobutton(ezarpenak, text="Erraza", variable=opcion,value=1).pack(side = tk.LEFT)
    tk.Radiobutton(ezarpenak, text="Ertaina", variable=opcion,value=2).pack(side = tk.LEFT)
    tk.Radiobutton(ezarpenak, text="Zaila", variable=opcion,value=3).pack(side = tk.LEFT)
    tk.Radiobutton(ezarpenak, text="Oso zaila", variable=opcion,value=4).pack(side = tk.LEFT)

    ezarpenak.mainloop()




