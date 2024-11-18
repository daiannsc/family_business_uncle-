# Funciones de la interfaz de consola

from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Gato, Perro
from clases.producto import Producto
from clases.venta import Venta


def registrar_mascota():
    tipo = input('Ingrese el tipo de mascota (Perro/Gato): ').strip().lower()
    nombre = input('Nombre de la mascota: ')
    edad = int(input('Edad del animal: '))
    salud = input('Estado de salud del animal: ')
    precio = float(input('Precio de la mascota: '))

    if tipo == 'perro':
        raza = input('Raza del perro: ')
        nivel_de_energia = input('Nivel de energía del perro: ')
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    elif tipo == 'gato':
        raza = input('Raza del gato: ')
        independencia = input('Nivel de independencia del gato: ')
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print('Tipo de mascota no reconocido.')
        return None
    return mascota


def registrar_cliente():
    nombre = input('Nombre del cliente: ')
    direccion = input('Dirección del cliente: ')
    telefono = input('Teléfono del cliente: ')
    cliente = Cliente(nombre, direccion, telefono)
    return cliente


def registrar_producto():
    nombre = input('Nombre del producto: ')
    categoria = input('Categoría del producto: ')
    precio = float(input('Precio del producto: '))  # Corregido, faltaba el precio
    cantidad = int(input('Cantidad de productos: '))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto


def registrar_venta(clientes, inventario):
    nombre_cliente = input('Nombre del cliente: ')
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print('Cliente no encontrado.')
        return
    
    productos = []

    while True:
        nombre_producto = input('Nombre del producto (deje vacío para finalizar): ')
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        
        if producto:
            productos.append(producto)
        else:
            print('Producto no encontrado.')

    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print('La venta ha sido registrada.')
    else:
        print('No se ha registrado la venta porque no se seleccionaron productos.')


def mostrar_menu():
    print('\n --- Menú de gestión de Patas Felices ---')
    print('1. Registrar mascota')
    print('2. Registrar cliente')
    print('3. Registrar producto')
    print('4. Registrar venta')
    print('5. Mostrar información acerca de mascotas')
    print('6. Mostrar información acerca de clientes')
    print('7. Mostrar información acerca de productos')
    print('8. Generar alerta de inventario')
    print('9. Salir')


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input('Seleccionar una opción: ')

        if opcion == '1':
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print('Mascota registrada con éxito.')

        elif opcion == '2':
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print('Cliente registrado con éxito.')

        elif opcion == '3':
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print('Producto registrado con éxito.')

        elif opcion == '4':
            registrar_venta(clientes, inventario)

        elif opcion == '5':
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())

        elif opcion == '6':
            for cliente in clientes:
                print(cliente.mostrar_informacion())

        elif opcion == '7':
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())

        elif opcion == '8':
            umbral_minimo = int(input('Ingrese el umbral mínimo del inventario: '))
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == '9':
            print('Saliendo del sistema, gracias por usar Patas Felices App.')
            break

        else:
            print('Opción no encontrada.')


if __name__ == "__main__":
    main()