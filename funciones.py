def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")