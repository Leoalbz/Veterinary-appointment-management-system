import clientes as cl
import tkinter as tk
from tkinter import messagebox

pacientes = cl.Pacientes()


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


    nombre_entry.delete(0, tk.END)
    raza_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    diagnostico_text.delete("1.0", tk.END)
    tratamiento_text.delete("1.0", tk.END)
    telefono_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def buscar_paciente():

    ventana_busqueda = tk.Toplevel(ventana)
    ventana_busqueda.title("Buscar Paciente")
    ventana_busqueda.geometry("400x300")

    tk.Label(ventana_busqueda, text="Ingrese el nombre del paciente:").pack(pady=10)
    nombre_buscar_entry = tk.Entry(ventana_busqueda)
    nombre_buscar_entry.pack(pady=5)
    text_resultado = tk.Text(ventana_busqueda, wrap=tk.WORD, height=10, width=50)
    text_resultado.pack(pady=10)

    def realizar_busqueda():
        nombre = nombre_buscar_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Ingrese un nombre válido.")
            return
        
        resultado = pacientes.mostrar_paciente(nombre)

        if resultado:
            text_resultado.delete("1.0", tk.END) 
            text_resultado.insert(tk.END, resultado)
        else:
            messagebox.showinfo("Resultado", "No se encontró ningún paciente con ese nombre.")


    tk.Button(ventana_busqueda, text="Buscar", command=realizar_busqueda).pack(pady=10)



def editar_paciente():
    ventana_editar = tk.Toplevel(ventana)
    ventana_editar.title("Editar Paciente")
    ventana_editar.geometry("400x400")

    tk.Label(ventana_editar, text="Ingrese el nombre del paciente:").pack(pady=5)
    nombre_buscar_entry = tk.Entry(ventana_editar)
    nombre_buscar_entry.pack(pady=5)

    def cargar_datos():
        nombre = nombre_buscar_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Ingrese un nombre válido.")
            return

        datos_paciente = pacientes.mostrar_paciente(nombre)
        if datos_paciente is None:
            messagebox.showerror("Error", "Paciente no encontrado.")
            return

        ventana_actualizar = tk.Toplevel(ventana_editar)
        ventana_actualizar.title("Actualizar Paciente")
        ventana_actualizar.geometry("400x500")

        global nombre_entry, raza_entry, edad_entry, diagnostico_text, tratamiento_text, telefono_entry, email_entry

        tk.Label(ventana_actualizar, text="Nombre:").pack(pady=2)
        nombre_entry = tk.Entry(ventana_actualizar)
        nombre_entry.insert(0, datos_paciente["nombre"])
        nombre_entry.pack(pady=2)

        tk.Label(ventana_actualizar, text="Raza:").pack(pady=2)
        raza_entry = tk.Entry(ventana_actualizar)
        raza_entry.insert(0, datos_paciente["raza"])
        raza_entry.pack(pady=2)

        tk.Label(ventana_actualizar, text="Edad:").pack(pady=2)
        edad_entry = tk.Entry(ventana_actualizar)
        edad_entry.insert(0, datos_paciente["edad"])
        edad_entry.pack(pady=2)

        tk.Label(ventana_actualizar, text="Diagnóstico:").pack(pady=2)
        diagnostico_text = tk.Text(ventana_actualizar, height=3, width=30)
        diagnostico_text.insert(tk.END, datos_paciente["diagnostico"])
        diagnostico_text.pack(pady=2)

        tk.Label(ventana_actualizar, text="Tratamiento:").pack(pady=2)
        tratamiento_text = tk.Text(ventana_actualizar, height=3, width=30)
        tratamiento_text.insert(tk.END, datos_paciente["tratamiento"])
        tratamiento_text.pack(pady=2)

        tk.Label(ventana_actualizar, text="Teléfono:").pack(pady=2)
        telefono_entry = tk.Entry(ventana_actualizar)
        telefono_entry.insert(0, datos_paciente["telefono"])
        telefono_entry.pack(pady=2)

        tk.Label(ventana_actualizar, text="Email:").pack(pady=2)
        email_entry = tk.Entry(ventana_actualizar)
        email_entry.insert(0, datos_paciente["email"])
        email_entry.pack(pady=2)

        def actualizar_paciente():
            nuevo_paciente = {
                "nombre": nombre_entry.get(),
                "raza": raza_entry.get(),
                "edad": edad_entry.get(),
                "diagnostico": diagnostico_text.get("1.0", tk.END).strip(),
                "tratamiento": tratamiento_text.get("1.0", tk.END).strip(),
                "telefono": telefono_entry.get(),
                "email": email_entry.get(),
            }
            
            pacientes.actualizar_paciente(nombre, nuevo_paciente)
            messagebox.showinfo("Información", "Paciente actualizado correctamente.")
            ventana_actualizar.destroy()

        tk.Button(ventana_actualizar, text="Guardar Cambios", command=actualizar_paciente).pack(pady=10)

    tk.Button(ventana_editar, text="Buscar", command=cargar_datos).pack(pady=10)


def mostrar_pacientes():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Lista de Pacientes")
    nueva_ventana.geometry("800x600")

    text_lista = tk.Text(nueva_ventana, wrap=tk.WORD, height=20, width=80)
    text_lista.pack(pady=10)

    pacientes_texto = pacientes.mostrar_todos_los_pacientes()
    text_lista.insert(tk.END, pacientes_texto)

    label = tk.Label(nueva_ventana, text="Lista de Pacientes", font=("Arial", 14))
    label.pack(pady=10)

    tk.Label(nueva_ventana, text="Eliminar Paciente").pack(pady=5)
    tk.Label(nueva_ventana, text="Coloque el nombre del paciente a eliminar").pack(pady=6)
    
    nombre_entry = tk.Entry(nueva_ventana)
    nombre_entry.pack(pady=5)

    def eliminar_paciente():
        nombre = nombre_entry.get().strip()  
        if nombre:
            confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Seguro que quieres eliminar al paciente '{nombre}'?")
            if confirmacion:
                pacientes.eliminar_paciente(nombre) 
                messagebox.showinfo("Información", f"Paciente '{nombre}' eliminado con éxito")
                

                nombre_entry.delete(0, tk.END)
                text_lista.delete("1.0", tk.END)
                pacientes_texto = pacientes.mostrar_pacientes()
                text_lista.insert(tk.END, pacientes_texto)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre del paciente.")

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
tk.Button(ventana, text="Editar Paciente", command=editar_paciente).place(x=450, y=500)


ventana.mainloop()
