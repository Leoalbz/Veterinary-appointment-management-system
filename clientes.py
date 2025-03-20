import conexion as cs  # Importamos el módulo de conexión a MySQL

class Pacientes:
    # Agregar paciente
    def agregar_paciente(self, paciente):
        conexion, cursor = cs.conectar()
        sql = "INSERT INTO pacientes (nombre, raza, edad, diagnostico, tratamiento, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (paciente["nombre"], paciente["raza"], paciente["edad"], paciente["diagnostico"], paciente["tratamiento"], paciente["telefono"], paciente["email"])
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()

    # Mostrar todos los pacientes
    def mostrar_pacientes(self):
        conexion, cursor = cs.conectar()
        sql = "SELECT * FROM pacientes"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.close()
        
        pacientes_texto = ""
        for paciente in resultado:
            pacientes_texto += f"ID: {paciente[0]}, Nombre: {paciente[1]}, Raza: {paciente[2]}, Edad: {paciente[3]}, Diagnóstico: {paciente[4]}, Tratamiento: {paciente[5]}, Telefono: {paciente[5]}, Email:{paciente[6]}\n"
        
        return pacientes_texto

    # 🔹 Mostrar un solo paciente por nombre
    def mostrar_paciente(self, nombre):
        conexion, cursor = cs.conectar()
        sql = "SELECT * FROM pacientes WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        resultado = cursor.fetchall()
        conexion.close()

        if resultado:
            paciente = resultado[0]
            return f"ID: {paciente[0]}, Nombre: {paciente[1]}, Raza: {paciente[2]}, Edad: {paciente[3]}, Diagnóstico: {paciente[4]}, Tratamiento: {paciente[5]},Telefono: {paciente[5]}, Email:{paciente[6]}"
        else:
            return "Paciente no encontrado."

    # 🔹 Actualizar los datos de un paciente por ID
    def actualizar_paciente(self, nombre, raza, edad, diagnostico, tratamiento, telefono, email):
        conexion, cursor = cs.conectar()
        sql = """UPDATE pacientes SET nombre = %s, raza = %s, edad = %s, 
                 diagnostico = %s, tratamiento = %s, telefono = %s, email = %s, WHERE nombre = %s"""
        valores = (nombre, raza, edad, diagnostico, tratamiento, telefono, email)
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()

    # Eliminar paciente
    def eliminar_paciente(self, nombre):
        conexion, cursor = cs.conectar()
        sql = "DELETE FROM pacientes WHERE nombre = %s"
        cursor.execute(sql, (nombre))
        conexion.commit()
        conexion.close()

pacientes = Pacientes()
