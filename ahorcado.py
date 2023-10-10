import random

def jugar_ahorcado():
    palabra_secreta = ['ahorcado','follada','vanessa','estanco','portatil','superior','follame','pedorro'
        ,'imbecil','analisis']

    VIDAS = 8

    letras_adivinadas = []
    letras_incorrectas = []

    def elegir_palabra_secreta(lista_de_palabras):
        return random.choice(lista_de_palabras)

    def solicitar_letra():
        while True:
            letra = input('Dime una letra: ').lower()
            if letra.isalpha() and len(letra) == 1:
                return letra
            print('Entrada no válida. Ingresa solo una letra.')

    def mostrar_estado_palabra(palabra, letras_adivinadas):
        palabra_a_mostrar = ''
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_a_mostrar += letra + ' '
            else:
                palabra_a_mostrar += '_ '
        print(palabra_a_mostrar)

    def mostrar_vidas(vidas):
        print(f'Te quedan {vidas} vidas.')

    def mostrar_lista_incorrectas(letras):
        print('Letras incorrectas: ' + ''.join(letras))

    def mostrar_ahorcado(vidas):
        ahorcado = [
            '''
                -------
                |     |
                      |
                      |
                      |
                      |
            ''',
            '''
                -------
                |     |
                O     |
                      |
                      |
                      |
            ''',
            '''
                -------
                |     |
                O     |
                |     |
                      |
                      |
            ''',
            '''
                -------
                |     |
                O     |
               /|     |
                      |
                      |
            ''',
            '''
                -------
                |     |
                O     |
               /|     |
                |     |
                      |
            ''',
            '''
                -------
                |     |
                O     |
               /|\\    |
                |     |
                      |
            ''',
            '''
                -------
                |     |
                O     |
               /|\\    |
               / \\    |
                      |
            ''',
            '''
            MUERTO
            '''
        ]
        print(ahorcado[8 - vidas])

    palabra_elegida = elegir_palabra_secreta(palabra_secreta)
    print("\n¡Bienvenido al Juego del Ahorcado!\n")
    mostrar_estado_palabra(palabra_elegida, letras_adivinadas)

    while VIDAS > 0:
        letra_usuario = solicitar_letra()
        acierto = comprobar_letra(letra_usuario, palabra_elegida, letras_adivinadas, VIDAS)

        if acierto:
            mostrar_estado_palabra(palabra_elegida, letras_adivinadas)
            if len(set(palabra_elegida)) == len(letras_adivinadas):
                print('\n¡Felicidades! ¡Has ganado el juego!')
                return

        else:
            VIDAS -= 1
            letras_incorrectas.append(letra_usuario)
            mostrar_lista_incorrectas(letras_incorrectas)
            mostrar_vidas(VIDAS)
            if VIDAS > 0:
                mostrar_ahorcado(VIDAS)

    print('\n¡Has perdido! ¡Más suerte la próxima vez!')
    return

def comprobar_letra(letra, palabra, letras_adivinadas, VIDAS):
    if letra in palabra and letra not in letras_adivinadas:
        letras_adivinadas.append(letra)
        return True
    else:
        print('Letra no válida.')
        return False

jugar_ahorcado()