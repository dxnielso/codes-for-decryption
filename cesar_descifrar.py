import sys

letras = "abcdefghijklmnopqrstuvwxyz"


def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for letra in texto:
        if letra in letras:
            indice_original = letras.index(letra)
            nuevo_indice = (indice_original - desplazamiento) % len(letras)
            texto_cifrado += letras[nuevo_indice]
        else:
            texto_cifrado += (
                letra  # Mantiene los caracteres que no son letras sin cambios
            )
    return texto_cifrado


# Obtiene los argumentos de la línea de comandos
argumentos = sys.argv

if len(argumentos) > 1:
    palabras = argumentos[1:]

    # Recorre diferentes desplazamientos
    for j in range(1, 51):
        cadena = ""
        # Prueba cada palabra con el desplazamiento actual
        for palabra in palabras:
            nueva_palabra = cifrar_cesar(palabra, j)
            cadena += nueva_palabra + " "
        print(f"CADENA RESULTANTE CON SALTOS DE {j}: {cadena.strip()}")

else:
    print("No se proporcionó ningún parámetro.")
