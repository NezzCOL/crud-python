import pyodbc

DB = 'sena'
SERVER = 'DESKTOP-NEJ0TUM\SQLEXPRESS'

try:
    conn = pyodbc.connect (
        'DRIVER={SQL Server};'
        f'SERVER={SERVER};'
        f'DATABASE={DB};'
        'Trusted_Connection=yes;'
    )
    print('Conexión exitosa', conn)
except Exception as err:
    print(f'Error de conexión {err}')

def Consulta():
    cur = conn.cursor()
    cur.execute('SELECT * FROM tps')
    row = cur.fetchall()

    while row:
        print (
            '---- CONSULTA DE DATOS ----\n'
              f'{row}\n'
        )
        break

def Eliminar():
    id = int(input('Ingrese el número del id que desea eliminar: '))

    res = conn.cursor()
    sql = ('DELETE FROM tps WHERE id={}').format(id)
    res.execute(sql)

    conn.commit()
    row = res.rowcount

    print(f'Registro del id {row} eliminado')

def Insertar():
    id = int(input('Ingrese un id válido: '))
    nombre = str(input('Ingrese un nombre: '))
    apellido = str(input('Ingrese un apellido: '))
    telefono = int(input('Ingrese un número de telefono: '))

    res = conn.cursor()
    res.execute(f"INSERT INTO tps(id, nombre, apellido, telefono) VALUES({id},'{nombre}', '{apellido}', {telefono})")
    conn.commit()

    row = res.rowcount
    print(f'{row} registro insertado')

def Editar():
    id = int(input('Seleccione el id del dato que quiere actualizar: '))
    nombre = str(input('Ingrese el nuevo nombre: '))
    apellido = str(input('Ingrese el nuevo apellido: '))
    telefono = int(input('Ingrese el nuevo número de teléfono: '))

    cur = conn.cursor()
    sql = 'UPDATE tps SET nombre=?, apellido=?, telefono=? WHERE id=?'

    cur.execute(sql, (nombre, apellido, telefono, id))
    conn.commit()

    row = cur.rowcount
    print(row)

while True:
    print('\nQue desea realizar \n')

    print('1. Consultar datos de la tabla')
    print('2. Editar datos de la tabla')
    print('3. Insertar datos en la tabla')
    print('4. Eliminar datos de la tabla')
    print('0. Finalizar programa')

    opcion = int(input('\nEscoja una opción: '))

    if opcion == 1:
        Consulta()
    if opcion == 2:
        Editar()
    if opcion == 3:
        Insertar()
    if opcion == 4:
        Eliminar()
    elif opcion == 0:
        print('Adios')
        break
    else:
        print('☝️')