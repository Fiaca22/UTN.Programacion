pila = 0
notas = []
while True:
    nota = input("Introduce una nota (o 'fin' para terminar): ")
    if nota.lower() == 'fin':
        break
    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
            pila += 1
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número o 'fin'.")