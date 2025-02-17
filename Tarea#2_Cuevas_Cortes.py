#Nombre: Viridiana Cuevas Cortes Grupo: 951
#Fecha de realización:14/02/2025
#Descripción del problema:1. Sistema de Reserva, utilizando sets
#habitaciones disponibles y reservadas

print("---EJERCICIO#1---")
habit_disp={101,102,103,201,202,203,301,302,303}
habit_reser=set()

def reservar_habit(no_habit):
    print("\n--Reserva de habitación--")
    if no_habit in habit_disp:
        habit_disp.remove(no_habit)
        habit_reser.add(no_habit)
        print(f"Habitacion:",no_habit, "reservada con exito")
    else:
        print(f"Habitación:",no_habit,"no reservada, revise los datos")

def liberar_habit(no_habit):
    print("\n--Liberar habitación--")
    if no_habit in habit_reser:
        habit_reser.remove(no_habit)
        habit_disp.add(no_habit)
        print(f"Habitación:",no_habit,"liberada con exito")
    else:
        print(f"Habitación:",no_habit,"no liberada con exito, revise los datos")

def mostar_disp():
    print("\n--Mostrar disponibilidad--")
    print(f"Habitaciones disponibles:",habit_disp)
    print(f"Habitaciones reservadas:", habit_reser)

#Pruebas
reservar_habit(101)
reservar_habit(202)
reservar_habit(303)
liberar_habit(303)
mostar_disp()

#Nombre: Viridiana Cuevas Cortes Grupo: 951
#Fecha de realización:14/02/2025
#Descripción del problema:2. Encriptación y Desencriptación de Mensajes Secretos
# utilizar un método de encriptación y desencriptación basado en listas o diccionarios

print("\n---EJERCICIO#2---")
diccionario_encrip = {
    'a': '@1#', 'b': '%2^', 'c': '&3/', 'd': '+4=', 'e': 'q5e',
    'f': 'r6y', 'g': 'u7*', 'h': 'p8!', 'i': 'd9g', 'j': 'h0-',
    'k': '1lx', 'l': '2vb', 'm': '3mq', 'n': '4er', 'o': '5yu',
    'p': '6op', 'q': '7sd', 'r': '8gh', 's': '9kl', 't': '0xc',
    'u': 'vb1', 'v': 'mn2', 'w': 'qa3', 'x': 'ws4', 'y': 'ed5',
    'z': 'rf6'
}

diccionario_desencrip = {v: k for k, v in diccionario_encrip.items()}

def encriptar_mensaje(mensaje):
    mensaje_encriptado = []
    for letra in mensaje.lower():
        if letra in diccionario_encrip:
            mensaje_encriptado.append(diccionario_encrip[letra])
        else:
            mensaje_encriptado.append(letra)
    return ''.join(mensaje_encriptado)

def desencriptar_mensaje(mensaje_encriptado):
    mensaje_desencriptado = []
    i = 0
    while i < len(mensaje_encriptado):
        codigo = mensaje_encriptado[i:i+3]
        if codigo in diccionario_desencrip:
            mensaje_desencriptado.append(diccionario_desencrip[codigo])
            i += 3
        else:
            mensaje_desencriptado.append(mensaje_encriptado[i])
            i += 1
    return ''.join(mensaje_desencriptado)

# Pruebas
mensaje_original = "quiero un cien en esta tarea"
mensaje_encriptado = encriptar_mensaje(mensaje_original)
print(f"Mensaje original: {mensaje_original}")
print(f"Mensaje encriptado: {mensaje_encriptado}")

mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado)
print(f"Mensaje desencriptado: {mensaje_desencriptado}")

#Nombre: Viridiana Cuevas Cortes Grupo: 951
#Fecha de realización:14/02/2025
#Descripción del problema:3.Crear un Inventario de Productos,Las claves: códigos de producto
# y los valores: nombre, precio y cantidad en stock.Debe tener funciones:
# agregar, editar,eliminar producto, realizar venta e imprimir inventario

print("\n---EJERCICIO#3---")

inventario = {}

def agregar_producto(codigo, nombre, precio, cantidad):
    if codigo not in inventario:
        inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"Producto {nombre} agregado con éxito al inventario.")
    else:
        print(f"El producto con código {codigo} ya existe en el inventario.")

def editar_producto(codigo, nombre=None, precio=None, cantidad=None):
    if codigo in inventario:
        if nombre:
            inventario[codigo]["nombre"] = nombre
        if precio:
            inventario[codigo]["precio"] = precio
        if cantidad:
            inventario[codigo]["cantidad"] = cantidad
        print(f"El producto con código {codigo} fue editado con éxito.")
    else:
        print(f"El producto con código {codigo} no existe.")

def eliminar_producto(codigo):
    if codigo in inventario:
        eliminado = inventario.pop(codigo)
        print(f"Producto {eliminado['nombre']} eliminado con éxito.")
    else:
        print(f"El producto con código {codigo} no existe.")

def realizar_venta(codigo, cantidad_vendida):
    if codigo in inventario:
        if inventario[codigo]["cantidad"] >= cantidad_vendida:
            inventario[codigo]["cantidad"] -= cantidad_vendida
            print(f"Venta realizada: {cantidad_vendida} unidades de {inventario[codigo]['nombre']}.")
        else:
            print(f"No hay suficiente stock de {inventario[codigo]['nombre']}.")
    else:
        print(f"El producto con código {codigo} no existe.")

def imprimir_inventario():
    print("\n=======INVENTARIO ACTUAL======\n")
    for codigo, detalles in inventario.items():
        print(f"Código: {codigo}, Nombre: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

# Pruebas
agregar_producto(1, "Galletas", 200, 10)
agregar_producto(2, "Sabritas", 20, 60)
editar_producto(1, nombre="Cajas de Galletas", precio=350)
realizar_venta(2, 5)
imprimir_inventario()