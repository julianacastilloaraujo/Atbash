def cifrar_atbash(texto):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.lower()
            codigo_letra = ord(letra)
            letra_cifrada = chr(219 - codigo_letra)  # Invertir el valor ASCII de la letra
            if mayuscula:
                letra_cifrada = letra_cifrada.upper()
            resultado += letra_cifrada
        else:
            resultado += letra  # Mantener caracteres no alfabéticos sin cambios
    return resultado

# Ejemplo de uso
texto_original = "Vamonos a la guerra"
texto_cifrado = cifrar_atbash(texto_original)
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
