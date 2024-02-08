def imprimir_factura(producto, cantidad, precio):
    subtotal = cantidad * precio
    descuento = subtotal * 0.25
    subtotal_con_descuento = subtotal - descuento
    iva = subtotal_con_descuento * 0.19
    total_a_pagar = subtotal_con_descuento + iva
    
    print('\n ****** FACTURA DE VENTA  ********')
    print('------------------------------------------------------------')
    print("Producto: ", producto)
    print("Cantidad: ", cantidad)
    print("Precio unitario: ", precio)
    print("Subtotal: ", subtotal)
    print("Descuento 25%: ", descuento)
    print("Subtotal con descuento: ", subtotal_con_descuento)
    print("Iva 19%: ", iva)
    print("Total a pagar: ", total_a_pagar)

producto = input('Ingrese el nombre del producto: ')
cantidad = int(input('Ingrese la cantidad del producto: '))
precio = float(input('Ingrese el precio del producto: $'))

imprimir_factura(producto, cantidad, precio)