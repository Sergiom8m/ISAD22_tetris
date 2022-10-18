import tkinter as tk
from tkinter import *
from tkinter import ttk

# https://www.youtube.com/watch?v=0WafQCaok6g ESTA ES LA QUE ESTA PUESTA, PERO NO FUNCIONA... CREO Q ES POR LAMBDA
# https://www.youtube.com/watch?v=VmlgrrXAqb4 ESTE ES PARECIDO PERO EL LAMBDA CAMBIA....PERO TAMPOCO VA
# https://www.tutorialspoint.com/python/tk_scrollbar.htm ESTE VA PERO ES MUY SIMPLE Y NO SE SI NOS SIRVE PARA LO QUE QUEREMOS
# https://www.aprendeaprogramar.com/mod/forum/discuss.php?d=2839 ESTE CREO QUE MEZCLA LAS PRIMERAS CON LA TERCERA PERO NO LO ENTIENDO BIEN

# https://www.youtube.com/watch?v=hL2tMm1FNkE el que esta ahora
class ErabiltzaileakEzabatu(object):

    def __init__(self):
        super(ErabiltzaileakEzabatu, self).__init__()
        self.window = tk.Tk()
        self.window.title("Erabiltzaileak ezabatu")
        self.window.geometry('400x400')
        self.window.resizable(False, False)

        #Crear el scroll y el texto
        self.scroll = tk.Scrollbar(self.window)
        self.texto= tk.Text(self.window, height=10, width=50)

        #Colocar el scroll y el texto
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.texto.pack(side=tk.LEFT, fill=tk.Y)

        #Configurar el widget
        #indicamos que modificara a texto en su scroll Y invocando el metodo yview
        #yview, xview
        self.scroll.config(command=self.texto.yview)

        #Asociar con el scroll para poder colocarlo en la posicion invocando metodo set
        self.texto.config(yscrollcommand=self.scroll.set)

        mensaje="USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS " \
                "USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS "


        #insertar mensaje al final

        self.texto.insert(tk.END, mensaje)

        self.window.mainloop()
