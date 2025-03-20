import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()



# Configuración de conexión a MySQL
def conectar():
    conexion = mysql.connector.connect(
        host= os.getenv("DB_HOST"),       
        user=os.getenv("DB_USER"),          
        password=os.getenv("DB_PASSWORD"),    
        database=os.getenv("DATABASE")  
    )
    cursor = conexion.cursor()
    return conexion, cursor



def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS pacientes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            raza VARCHAR(50) NOT NULL,
            edad INT(10),
            diagnostico VARCHAR(50),
            tratamiento VARCHAR(50),
            telefono VARCHAR(14) NOT NULL,
            email VARCHAR(50) NOT NULL
        )
    """
    cursor.execute(sql)
    print("Tabla creada o ya existente")
    conexion.close()

if __name__ == '__main__':
    crearTabla()
    print('Ejecutando script principal')
