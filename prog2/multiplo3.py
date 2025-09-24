# generar una lista con los elementos pares multiplos de 3, menores a un numero ingresado por el usuario, dividir el problema en subproblemas

def pedir_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def es_par_y_multiplo_de_tres(num):
    return num % 2 == 0 and num % 3 == 0

def generar_lista(limite):
    lista = []
    for i in range(limite):
        if es_par_y_multiplo_de_tres(i):
            lista.append(i)
    return lista

def main():
    limite = pedir_numero()
    lista_resultante = generar_lista(limite)
    print("Lista de números pares múltiplos de 3 menores a", limite, ":")
    print(lista_resultante)

main()