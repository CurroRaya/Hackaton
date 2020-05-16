edad = input("introduce tu edad: ")
edad = int(edad)

if edad < 4:
    print("El precio de la entrada es 0.")
elif edad >= 4 and edad <= 18:
    print("El precio de la entrada es 5€.")
else:
    print("El precio de la entrada es 10€.")