# Programa: Ingeniería Electrónica
# Código fuente: Autoría propia

print("----- Sistema de ventas Pizzería 2026 -----")

# R1 Almacenar precios y porciones en arreglos
precios = [10000, 15000, 20000, 25000, 35000]
porciones = [2, 4, 6, 8, 12]
nombres = ["Pequeña", "Mediana", "Larga", "Familiar", "Extra Familiar"]
vendidas = [0, 0, 0, 0, 0]

# R2 Solicitar el número de clientes
clientes = 0
while clientes <= 0:
    clientes = int(input("Ingrese el número de clientes a atender: "))

total_ventas = 0
total_porciones = 0

# R3 Atender a cada cliente
for c in range(clientes):
    print("===== Cliente", c + 1, "=====")
    total_cliente = 0
    porciones_cliente = 0
    continuar = "SI"

    while continuar == "SI":
        print("----- MENÚ DE PIZZAS -----")
        for i in range(len(precios)):
            print(i + 1, "-", nombres[i], "-", porciones[i], "porciones - $", precios[i])

        tipo = int(input("Seleccione el tipo de pizza (1 a 5): "))
        cantidad = int(input("¿Cuántas pizzas de este tipo desea?: "))

        if tipo < 1 or tipo > 5 or cantidad <= 0:
            print("Error: tipo o cantidad no válidos.")
        else:
            # R4 y R5 Calcular la compra y acumular
            costo = precios[tipo - 1] * cantidad
            # TODO 1: completa estas 4 líneas
            porc = porciones[tipo - 1] * cantidad    (porciones de esta compra)
            vendidas[tipo - 1] = vendidas[tipo - 1] + cantidad  (suma la cantidad al tipo vendido)
            total_cliente = total_cliente + costo       (suma el costo)
            porciones_cliente = porciones_cliente + porc   (suma las porciones)
            print("Agregado: $", costo, "-", porc, "porciones")

        continuar = input("¿Desea comprar otro tipo de pizza? (si/no): ").upper()

    print("Total a pagar del cliente", c + 1, ": $", total_cliente)
    print("Porciones del pedido:", porciones_cliente)
    total_ventas = total_ventas + total_cliente
    total_porciones = total_porciones + porciones_cliente

# R6 Mostrar resultados finales
print("===== RESUMEN DE VENTAS =====")
# TODO 2: con un for que recorra el arreglo vendidas,
#         imprime el nombre de cada tipo y cuántas se vendieron
print("Valor total de las ventas: $", total_ventas)
print("Total de porciones vendidas:", total_porciones)