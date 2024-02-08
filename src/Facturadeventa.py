def imprimir_factura(producto, cantidad, precio):
    subtotal = cantidad * precio
    descuento = subtotal * 0.25
    subtotal_con_descuento = subtotal - descuento
    iva = subtotal_con_descuento * 0.19

producto = input('Ingrese el nombre del producto: ')
cantidad = int(input('Ingrese la cantidad del producto: '))
precio = float(input('Ingrese el precio del producto: $'))