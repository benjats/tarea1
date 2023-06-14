def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_numeros_primos_hasta_cero(numero):
    numeros_primos = []
    for i in range(numero, 0, -1):
        if es_primo(i):
            numeros_primos.append(i)
    print(numeros_primos)

numero = int(input("Ingrese un número: "))
imprimir_numeros_primos_hasta_cero(numero)

    