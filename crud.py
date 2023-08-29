import pyodbc

DB = 'sena'
SERVER = 'DESKTOP-RGO03S4\MSSQLSERVER3'

try:
    conex = pyodbc.connect ('DRIVER={SQL Server};'f'SERVER={SERVER};'f'DATABASE={DB};''Trusted_Connection=yes;')
    print('Conexión exitosa', conex)
except Exception:
    print(f'Error de conexión {Exception}')

def Consulta():
    res=conex.cursor()
    res.execute("select * from tps35")
    datos=res.fetchall()
    #res.close()
    #conex.close()
    for i in datos:
        print(i)

def Insertar():
    id=int(input('Ingrese un id valido: '))
    nombre=str(input('Ingrese un nombre: '))
    apellido=str(input('Ingrese un apellido: '))
    telefono=int(input('Ingresse un número de telefono: '))

    res=conex.cursor()
    res.execute(f"INSERT INTO tps35(id, nombre, apellido, telefono) VALUES({id},'{nombre}', '{apellido}', {telefono})")
    conex.commit()
    fila=res.rowcount
    print(fila,"Registro insertado")

def Eliminar():
    id=int(input('Ingrese el id que desea eliminar: '))
    res=conex.cursor()
    sql=("delete from tps35 where id={}").format(id)
    res.execute(sql)
    conex.commit()
    fila=res.rowcount
    print("Usuario borrado",fila)

def Actualizar():
    id=int(input('Seleccione el id a actualizar: '))
    nombre=str(input('Ingrese un nuevo nombre: '))
    apellido=str(input('Ingrese un nuevo apellido: '))
    telefono=int(input('Ingrese un nuevo numero de telefono: '))
    res=conex.cursor()
    sql=(f"UPDATE tps35 SET nombre='{nombre}', apellido='{apellido}', telefono={telefono} WHERE id={id}")
    res.execute(sql)
    conex.commit()
    fila=res.rowcount
    print("Datos actualizados",fila)

while True:
    print('\nQue desea realizar \n')
    print('1. Consultar datos de la tabla')
    print('2. Editar datos de la tabla')
    print('3. Insertar datos en la tabla')
    print('4. Eliminar datos de la tabla')
    print('0. Finalizar programa')

    opcion = int(input('\nElija una opción: '))

    if opcion == 1:
        Consulta()
    if opcion == 2:
        Actualizar()
    if opcion == 3:
        Insertar()
    if opcion == 4:
        Eliminar()
    elif opcion == 0:
        print('\nAdios\n')
        break
    else:
        print('\nHola de nuevo\n')
