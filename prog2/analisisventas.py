totalventas = 0
ventaMasAlta = None
totalRecaudado = 0.0
ultimaventa = 1
while ultimaventa >0:
    ultimaventa = float(input("Ingrese el monto de la última venta (negativo o 0 para terminar): "))

    if ultimaventa > 0:
        totalventas += 1
        totalRecaudado += ultimaventa

        if ventaMasAlta is None or ultimaventa > ventaMasAlta:
            ventaMasAlta = ultimaventa

if totalventas == 0:
    print("No se registraron ventas.")
else:
    promedioVentas = totalRecaudado / totalventas
    print(f"El número de ventas es: {totalventas}")
    print(f"La venta más alta es: {ventaMasAlta}")
    print(f"El promedio de ventas es: {promedioVentas}")
    print(f"El total recaudado es: {totalRecaudado}")
