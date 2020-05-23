# Enrutar nuestra aplicacion
from modelos import (
    Tienda, Producto, Compra
)


class ControladorTienda:

    tienda = None

    @classmethod
    def registrar_tienda(cls, datos_tienda):
        cls.tienda = Tienda(datos_tienda['nombre'])
        return cls.tienda


class ControladorProducto:

    productos = None

    @classmethod
    def registrar_producto(cls, datos_producto):
        if cls.productos is None:
            cls.productos = []
        nuevo_producto = Producto(
            datos_producto['nombre'],
            datos_producto['precio']
        )
        cls.productos.append(nuevo_producto)
        return nuevo_producto


class ControladorCompra:

    compras = None
    compra_actual = None

    @classmethod
    def registrar_compra(cls, datos_cliente):
        if cls.compras is None:
            cls.compras = []
        cls.compras.append(
            Compra(
                datos_cliente['nombre'],
                datos_cliente['documento']
            )
        )
        cls.compra_actual = cls.compras[-1]
        return cls.compra_actual

    @classmethod
    def registrar_producto_de_compra(
        cls, nombre_producto, cantidad
    ):
        respuesta = False
        producto_comprado = Producto.buscar_producto(
            nombre_producto, ControladorProducto.productos
        )
        if producto_comprado:
            cls.compra_actual.aniadir_producto(
                producto_comprado, cantidad
            )
            respuesta = True
        return respuesta

    @staticmethod
    def generar_factura(compra):
        return compra.generar_factura()
