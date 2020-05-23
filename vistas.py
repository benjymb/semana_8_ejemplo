from controladores import (
    ControladorTienda, ControladorProducto,
    ControladorCompra
)


class VistaTienda:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("Bienvenid@ a la seccion de la tienda! ")
            print("Elija 1 para registrar una nueva tienda")
            print("Elija 2 para listar la tienda")
            print("Elija 3 para volver al menu principal")
            opcion = input("Elija una opcion : ")
            if opcion == "1":
                VistaTienda.ingreso_datos()
            elif opcion == "2":
                VistaTienda.listar_tienda()
            else:
                continuar = False
 
    @staticmethod
    def ingreso_datos():
        if ControladorTienda.tienda is None:
            nombre = input("Ingrese el nombre de la tienda: ")
            ControladorTienda.registrar_tienda(
                {
                    'nombre': nombre
                }
            )
        else:
            print("Ya se registro una tienda!")
        print(ControladorTienda.tienda)

    @staticmethod
    def listar_tienda():
        print(ControladorTienda.tienda)


class VistaCompra:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("Bienvenid@ a la seccion de compras! ")
            print("Elija 1 para registrar una nueva compra")
            print("Elija 2 para listar las compras realizadas")
            print("Elija 3 para volver al menu principal")
            opcion = input("Elija una opcion : ")
            if opcion == "1":
                VistaCompra.ingreso_compra()
            elif opcion == "2":
                VistaCompra.listar_compras()
            else:
                continuar = False
 
    
    @staticmethod
    def ingreso_compra():
        VistaCompra._ingreso_cliente()
        VistaCompra._agregar_productos()

    @staticmethod
    def _ingreso_cliente():
        nombre = input("Ingrese el nombre del cliente: ")
        documento = input("Ingrese el documento del cliente: ")
        nueva_compra = ControladorCompra.registrar_compra(
            {
                'nombre': nombre,
                'documento': documento
            }
        )
        print(
            "Se va a registrar una compra para el cliente "
            f"{nueva_compra.nombre_cliente}"
        )

    @staticmethod
    def _agregar_productos():
        nombre_producto = input("Ingrese el nombre del producto a comprar : ")
        cantidad = int(input("Ingrese la cantidad de productos a comprar : "))
        respuesta = ControladorCompra.registrar_producto_de_compra(
            nombre_producto, cantidad
        )
        if respuesta:
            print("Se aniadio el producto a la compra.")
        else:
            print("No se pudo encontrar el producto.")

    @staticmethod
    def listar_compras():
        for compra in ControladorCompra.compras:
            print(compra)

class VistaProducto:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("Bienvenid@ a las seccion de productos! ")
            print("Elija 1 para registrar un producto")
            print("Elija 2 para listar los productos")
            print("Elija 3 para volver al menu principal")
            opcion = input("Elija una opcion : ")
            if opcion == "1":
                VistaProducto.ingresar_producto()
            elif opcion == "2":
                VistaProducto.listar_productos()
            else:
                continuar = False



    @staticmethod
    def ingresar_producto():
        nombre = input("Ingrese el nombre del producto : ")
        precio = input("Ingrese el precio del producto : ")
        nuevo_producto = ControladorProducto.registrar_producto(
            {
                'nombre': nombre, 'precio': precio
            }
        )
        print(nuevo_producto)

    @staticmethod
    def listar_productos():
        for producto in ControladorProducto.productos:
            print(producto)


class VistaAplicacion:

    @staticmethod
    def iniciar():
        VistaAplicacion.bienvenida()
        VistaAplicacion.menu()
    
    @staticmethod
    def bienvenida():
        print("Bienvenid@ a nuestro sistema de tiendas!")

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("Elija 1 para ir a la seccion de tienda")
            print("Elija 2 para ir a la seccion de productos")
            print("Elija 3 para ir a la seccion de compras")
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                VistaTienda.menu()
            elif opcion == "2":
                VistaProducto.menu()
            elif opcion == "3":
                VistaCompra.menu()
            else:
                continuar = False
