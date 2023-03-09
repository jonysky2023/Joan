import sqlite3
from tkinter import ttk, StringVar
import tkinter as tk

windows = tk.Tk()
windows.title("Fichero clientes")
windows.columnconfigure(1, weight=1)
windows.rowconfigure(4, weight=1)

conector = sqlite3.connect('Alumnos.db')

query = "SELECT nombre, apellido FROM Alumnos WHERE nombre = ? OR apellido = ?"
agrega_nom = "INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)"
cursor = conector.cursor()

añade = StringVar()
añadenombre = ttk.Entry(windows, width=25, state="normal", textvariable=añade)
añadenombre.grid(row=1, column=0)

añadeape = StringVar()
agregaape = ttk.Entry(windows, width=25, state="normal", textvariable=añadeape)
agregaape.grid(row=2, column=0)

busqueda = StringVar()
entradanombre = ttk.Entry(windows, width=25, state="normal", textvariable=busqueda)
entradanombre.grid(row=3, column=0)

resultado = StringVar()
salida = ttk.Entry(windows, width=25, state="readonly", textvariable=resultado)
salida.grid(row=4, column=0)


def añadir():
    cursor.execute(agrega_nom, (añade.get(), añadeape.get()))
    conector.commit()
    añade.set("")
    añadeape.set("")


def buscar():
    cursor.execute(query, (busqueda.get(), busqueda.get()))
    result = cursor.fetchone()
    if result:
        resultado.set(f"{result[0]} {result[1]}")
    else:
        resultado.set("No encontrado")

añade_button = ttk.Button(windows, text="añadir cliente", command=añadir)
añade_button.grid(row=1, column=1)

buscar_button = ttk.Button(windows, text="Buscar", command=buscar)
buscar_button.grid(row=3, column=1)



windows.mainloop()
conector.close()
cursor.close()






