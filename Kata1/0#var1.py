"""
Primer ejercicio en python.
"""

precio = 3.49
descuento = 0.4
precio_con_descuento = precio * descuento

numero_de_barras = input("Introduce el numero de barras vendidas: ")
numero_de_barras = int(numero_de_barras)

print("Precio habitual " + str(precio))
print("Descuento " + str(precio_con_descuento))
print("Coste final: " + str(numero_de_barras * precio_con_descuento))
