import conexion as cs 

class Pacientes:

    def agregar_paciente(self, paciente):
        conexion, cursor = cs.conectar()
        sql = "INSERT INTO pacientes (nombre, raza, edad, diagnostico, tratamiento, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (paciente["nombre"], paciente["raza"], paciente["edad"], paciente["diagnostico"], paciente["tratamiento"], paciente["telefono"], paciente["email"])
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()


    def mostrar_paciente(self, nombre):
     conexion, cursor = cs.conectar()
     sql = "SELECT nombre, raza, edad, diagnostico, tratamiento, telefono, email FROM pacientes WHERE nombre = %s"
     cursor.execute(sql, (nombre,))
     resultado = cursor.fetchone()
     conexion.close()
     if resultado:
                paciente = {
                "nombre": resultado[0],
                "raza": resultado[1],
                "edad": resultado[2],
                "diagnostico": resultado[3],
                "tratamiento": resultado[4],
                "telefono": resultado[5],
                "email": resultado[6]
        }
                return paciente
     else:
           return None

    
    def mostrar_todos_los_pacientes(self):
        conexion, cursor = cs.conectar()
        sql = "SELECT * FROM pacientes"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.close()
        
        pacientes_texto = ""
        for paciente in resultado:
            pacientes_texto += f"ID: {paciente[0]}, Nombre: {paciente[1]}, Raza: {paciente[2]}, Edad: {paciente[3]}, Teléfono: {paciente[4]}, Email: {paciente[5]}, Diagnóstico: {paciente[6]}, Tratamiento: {paciente[7]}\n"
        
        return pacientes_texto


    def actualizar_paciente(self, nombre, raza, edad, diagnostico, tratamiento, telefono, email):
        conexion, cursor = cs.conectar()
        sql = """UPDATE pacientes SET nombre = %s, raza = %s, edad = %s, 
                 diagnostico = %s, tratamiento = %s, telefono = %s, email = %s, WHERE nombre = %s"""
        valores = (nombre, raza, edad, diagnostico, tratamiento, telefono, email)
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()
    
    def actualizar_paciente(self, nombre, nuevos_datos):
        conexion, cursor = cs.conectar()
        sql = """UPDATE pacientes SET nombre = %s, raza = %s, edad = %s, diagnostico = %s, tratamiento = %s, telefono = %s, email = %s WHERE nombre = %s"""
        valores = (nuevos_datos["nombre"], nuevos_datos["raza"], nuevos_datos["edad"], nuevos_datos["diagnostico"], nuevos_datos["tratamiento"], nuevos_datos["telefono"], nuevos_datos["email"], nombre)
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()



    def eliminar_paciente(self, nombre):
     conexion, cursor = cs.conectar()
     sql = "DELETE FROM pacientes WHERE nombre = %s"
     valores = (nombre,)
     cursor.execute(sql, valores)
     conexion.commit()
     conexion.close()


pacientes = Pacientes()
