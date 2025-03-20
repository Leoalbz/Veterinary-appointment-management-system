import clientes as cl
import tkinter as tk
from tkinter import messagebox

pacientes = cl.Pacientes()

# Función para agregar un paciente a MySQL
def agregar_pacientes():
    nombre = nombre_entry.get()
    raza = raza_entry.get()
    edad = edad_entry.get()
    diagnostico = diagnostico_text.get("1.0", tk.END).strip()
    tratamiento = tratamiento_text.get("1.0", tk.END).strip()
    telefono = telefono_entry.get()
    email = email_entry.get()
    
    nuevo_paciente = {
        "nombre": nombre,
        "raza": raza,
        "edad": edad,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "telefono": telefono,
        "email": email
    }

    pacientes.agregar_paciente(paciente=nuevo_paciente)
    messagebox.showinfo("Información", "Paciente agregado exitosamente")

    # Limpiar los campos
    nombre_entry.delete(0, tk.END)
    raza_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    diagnostico_text.delete("1.0", tk.END)
    tratamiento_text.delete("1.0", tk.END)
    telefono_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def buscar_paciente():
    nombre = nombre_entry.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Ingrese el nombre del paciente a buscar.")
        return
    
    resultado = pacientes.mostrar_paciente(nombre)
    messagebox.showinfo("Resultado de búsqueda", resultado)

def actualizar_paciente():
    nombre = nombre_entry.get()
    raza = raza_entry.get()
    edad = edad_entry.get()
    diagnostico = diagnostico_text.get("1.0", tk.END).strip()
    tratamiento = tratamiento_text.get("1.0", tk.END).strip()
    telefono = telefono_entry.get("1.0", tk.END).strip()
    email = email_entry.get("1.0", tk.END).strip()
    
    pacientes.actualizar_paciente(nombre, raza, edad, diagnostico, tratamiento, telefono, email)
    messagebox.showinfo("Información", "Paciente actualizado correctamente")


# Función para mostrar pacientes desde MySQL
def mostrar_pacientes():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Lista de Pacientes")
    nueva_ventana.geometry("800x600")

    text_lista = tk.Text(nueva_ventana, wrap=tk.WORD, height=20, width=80)
    text_lista.pack(pady=10)

    pacientes_texto = pacientes.mostrar_pacientes()
    text_lista.insert(tk.END, pacientes_texto)

    label = tk.Label(nueva_ventana, text="Lista de Pacientes", font=("Arial",14))
    label.pack(pady=10)

    tk.Label(nueva_ventana, text="Eliminar Paciente").pack(pady=5)
    tk.Label(nueva_ventana, text="Coloque el nombre del paciente a eliminar").pack(pady=6)
    id_eliminar_entry = tk.Entry(nueva_ventana)
    id_eliminar_entry.pack(pady=5)

    def eliminar_paciente():
        nombre = nombre_entry.get()
        if nombre:
            pacientes.eliminar_paciente(nombre)
            messagebox.showinfo("Información", f"Paciente con nombre {nombre} eliminado")
            nombre_entry.delete(0, tk.END)
            text_lista.delete("1.0", tk.END)
            pacientes_texto = pacientes.mostrar_pacientes()
            text_lista.insert(tk.END, pacientes_texto)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre de paciente.")

    tk.Button(nueva_ventana, text="Eliminar Paciente", command=eliminar_paciente).pack(pady=10)

# Interfaz 
ventana = tk.Tk()
ventana.title('Sistema gestor de pacientes')
ventana.geometry('800x600')

icono = tk.PhotoImage(file="icono-vet.png")
ventana.iconphoto(False, icono)

ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)

titulo = tk.Label(ventana, text='Sistema gestor de pacientes', fg='red', font=('Arial', 12))
titulo.pack(pady=10)

img = tk.PhotoImage(file='background_img.png')
bg_imagen = tk.Label(ventana, image=img)
bg_imagen.place(x=200, y=-100, relwidth=1, relheight=1)

# Campos de entrada

tk.Label(ventana, text="Nombre:").place(x=50, y=80)
nombre_entry = tk.Entry(ventana)
nombre_entry.place(x=150, y=80, width=150)

tk.Label(ventana, text="Raza:").place(x=50, y=110)
raza_entry = tk.Entry(ventana)
raza_entry.place(x=150, y=110, width=150)

tk.Label(ventana, text="Años:").place(x=50, y=140)
edad_entry = tk.Entry(ventana)
edad_entry.place(x=150, y=140, width=150)

tk.Label(ventana, text="Diagnóstico:").place(x=50, y=170)
diagnostico_text = tk.Text(ventana, height=4, width=40)
diagnostico_text.place(x=150, y=170)

tk.Label(ventana, text="Tratamiento:").place(x=50, y=300)
tratamiento_text = tk.Text(ventana, height=4, width=40)
tratamiento_text.place(x=150, y=270)

tk.Label(ventana, text="Teléfono:").place(x=50, y=350)
telefono_entry = tk.Entry(ventana)
telefono_entry.place(x=150, y=350, width=150)

tk.Label(ventana, text="Email:").place(x=50, y=370)
email_entry = tk.Entry(ventana)
email_entry.place(x=150, y=370, width=150)

tk.Button(ventana, text="Añadir Paciente", command=agregar_pacientes).place(x=120, y=450)
tk.Button(ventana, text="Mostrar Lista", command=mostrar_pacientes).place(x=280, y=450)
tk.Button(ventana, text="Buscar Paciente", command=buscar_paciente).place(x=150, y=500)
tk.Button(ventana, text="Actualizar Paciente", command=actualizar_paciente).place(x=300, y=500)

ventana.mainloop()
