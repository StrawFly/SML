from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Text, Scrollbar
from tkinter.font import Font

# Lista para almacenar todos los registros
datos_guardados = []

def mostrar_resultado(nombre, apellido, fecha, profesion):
    ventana = Toplevel()
    ventana.title("Datos Recolectados")
    ventana.geometry("500x400")
    ventana.configure(bg="light blue")
    
    fuente_cursiva = Font(family="Comic Sans MS", size=12, slant="italic")
    
    mensaje = f"Un saludo {nombre} {apellido},\n\nAsí que naciste el {fecha}\ny es increíble que estés en {profesion}."
    
    Label(ventana, 
          text=mensaje, 
          bg="light blue", 
          fg="black", 
          font=fuente_cursiva).pack(pady=20)
    
    Button(ventana, 
           text="Cerrar", 
           command=ventana.destroy, 
           bg="light blue", 
           fg="black",
           font=fuente_cursiva).pack()

def mostrar_historial():
    historial = Toplevel()
    historial.title("Historial Completo")
    historial.geometry("600x400")
    
    scrollbar = Scrollbar(historial)
    scrollbar.pack(side="right", fill="y")
    
    texto_historial = Text(historial, 
                          yscrollcommand=scrollbar.set,
                          bg="light blue",
                          font=Font(family="Comic Sans MS", size=10))
    texto_historial.pack(fill="both", expand=True)
    
    scrollbar.config(command=texto_historial.yview)
    
    for registro in datos_guardados:
        texto_historial.insert("end", 
                             f"Nombre: {registro['nombre']}\n"
                             f"Apellido: {registro['apellido']}\n"
                             f"Fecha: {registro['fecha']}\n"
                             f"Profesión: {registro['profesion']}\n"
                             "--------------------------\n")

def guardar():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    fecha = entrada_fecha.get()
    profesion = entrada_profesion.get()
    
    if not all([nombre, apellido, fecha, profesion]):
        messagebox.showerror("Error", "Completa todos los campos")
        return
    
    # Guardar en la lista como diccionario
    datos_guardados.append({
        "nombre": nombre,
        "apellido": apellido,
        "fecha": fecha,
        "profesion": profesion
    })
    
    mostrar_resultado(nombre, apellido, fecha, profesion)
    
    # Limpiar campos
    entrada_nombre.delete(0, 'end')
    entrada_apellido.delete(0, 'end')
    entrada_fecha.delete(0, 'end')
    entrada_profesion.delete(0, 'end')

# Configuración principal
root = Tk()
root.title("Datos Personales")
root.geometry("400x450")  # Aumenté el tamaño para el botón adicional
root.configure(bg="light blue")

fuente = Font(family="Comic Sans MS", size=10)
fuente_titulo = Font(family="Comic Sans MS", size=12, weight="bold")

# Texto de advertencia grande
Label(root, 
      text="TE INFORMAMOS \n Que estos datos serán guardados y protegidos\ncon el debido proceso.", 
      bg="light blue", 
      fg="black",
      font=fuente_titulo).pack(pady=10)

# Campos de entrada
Label(root, text="Nombre:", bg="light blue", font=fuente).pack(pady=5)
entrada_nombre = Entry(root, font=fuente, fg="black")
entrada_nombre.pack()

Label(root, text="Apellido:", bg="light blue", font=fuente).pack(pady=5)
entrada_apellido = Entry(root, font=fuente, fg="black")
entrada_apellido.pack()

Label(root, text="Fecha (dd/mm/aaaa):", bg="light blue", font=fuente).pack(pady=5)
entrada_fecha = Entry(root, font=fuente, fg="black")
entrada_fecha.pack()

Label(root, text="Profesión/Carrera:", bg="light blue", font=fuente).pack(pady=5)
entrada_profesion = Entry(root, font=fuente, fg="black")
entrada_profesion.pack()

# Botones
Button(root, 
       text="Guardar", 
       command=guardar, 
       bg="light sky blue", 
       fg="black",
       font=fuente).pack(pady=10)

Button(root, 
       text="Ver Historial", 
       command=mostrar_historial, 
       bg="light coral", 
       fg="black",
       font=fuente).pack(pady=10)

root.mainloop()