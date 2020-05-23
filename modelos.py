# Para definir nuestras entidades (modelos)

from decimal import Decimal


class Tienda:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"\nTienda : {self.nombre}\n"              


class Producto:

    def __init__(self,  nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def buscar_producto(nombre, productos):
        resultado = None
        for producto in productos:
            if producto.nombre == nombre:
                resultado = producto
                break
        return resultado

    def __str__(self):   
        return (
            "\n----- Producto -----\n"
            f"\n Nombre del producto : {self.nombre} \n"
            f"\n Precio del producto : {self.precio} \n"
            "\n---------------------\n"
        )


class Compra:

    def __init__(self, nombre_cliente, documento_cliente):
        self.nombre_cliente = nombre_cliente
        self.documento_cliente = documento_cliente
        self.productos_comprados = []

    def aniadir_producto(self, producto, cantidad):
        self.productos_comprados.append(
            (cantidad, producto, producto.precio * cantidad)
        )

    def generar_factura(self):
        return {
            'nombre': self.nombre_cliente,
            'documento': self.documento_cliente,
            'detalle': self.productos_comprados,
            'subtotal': self._obtener_subtotal(),
            'igv': self._obtener_igv(),
            'total': self._obtener_total(),
        }

    def _obtener_subtotal(self):
        subtotal = Decimal('0.00')
        for cantidad, producto, precio_total in self.productos_comprados:
            subtotal += precio_total
        return subtotal

    def _obtener_igv(self):
        subtotal = self._obtener_subtotal()
        igv = subtotal * Decimal('0.18')
        return igv

    def _obtener_total(self):
        return (
            self._obtener_igv() +
            self._obtener_subtotal()
        )

    def __str__(self):
        return (
            "\n ----------- Compra ---------\n"
            f"\n - Cliente : {self.nombre_cliente}\n"
            f"\n - Documento : {self.documento_cliente}\n"
            f"\n - Detalle de la compra : \n\n{self._detalle_str()}"
            f"\n - Subtotal : {self._obtener_subtotal()}\n"
            f"\n - IGV : {self._obtener_igv()}\n"
            f"\n - Total : {self._obtener_total()}\n"
            "\n ----------------------------\n"
        )

    def _detalle_str(self):
        detalle = " ---------------------------------------------- "
        detalle += "Cant.   Descripcion     Precio U.   Precio T."
        detalle = " ---------------------------------------------- "
        for cantidad, producto, precio_total in self.productos_comprados:
            detalle += "\n -------------------- \n"
            detalle += f"\n{cantidad}   {producto.nombre}   {producto.precio}   {precio_total}\n"
            detalle += "\n -------------------- \n"
        return detalle
