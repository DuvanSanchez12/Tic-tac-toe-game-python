from random import *

# Función para guardar una partida
def guardar_partida(posiciones, ganador,empezo):
    with open("aprendizaje.txt", "a") as archivo:
        archivo.write(f"{posiciones},'{ganador}','{empezo}'\n")

# Función para cargar partidas previas
def cargar_partidas(dificultad):
    try:
        archivo = open(f"{dificultad}.txt", "r")
        partidas = archivo.readlines()
        archivo.close()
        return [eval(partida.strip()) for partida in partidas]
    except FileNotFoundError:
        crear= open(f"{dificultad}.txt", "w")
        crear.close()
        return []

# Función para que la IA aprenda de las partidas anteriores
def movimiento_ia(posiciones, empezo,dificultades):
    partidas_previas = cargar_partidas(dificultades)
    contador_posiciones = [0] * 9
    for partida, ganador, empezar in partidas_previas:
        if empezar==empezo and (ganador == 'ia' or ganador == 'jugador'):
            i = 0
            while i < 9:
                # Verificamos si la posición está vacía o si coincide con la partida
                if posiciones[i] != ' ' and posiciones[i] != partida[i]:
                    break  # Si no coincide, salimos del bucle
                i += 1  # Incrementamos el índice
            if i == 9:  # Si hemos recorrido todas las posiciones sin encontrar discrepancias
                for j in range(9):
                    if partida[j] == 'O' or partida[j] == 'X':
                        contador_posiciones[j] += 1

    print("\n"
          "                !Pocision similar ganadora¡")
    punteo = []
    for posicion in range(9):  # Recorrer las posiciones del 0 al 8
        count = contador_posiciones[posicion]
        if count > 0 and posicion_libre(posiciones, posicion):  # Solo mostrar posiciones que han sido jugadas y están desocupadas
            punteo.append((posicion + 1, count))  # Guardar el número de posición (1-9) y el conteo

    # Ordenar el punteo de mayor a menor basado en el número de veces jugadas
    punteo.sort(key=lambda x: -x[1])  # Ordenar por el número de veces que se ha jugado, de mayor a menor

    # Elegir la mejor posición disponible según el punteo
    for posicion, veces in punteo:
        print(f"                    Posición {posicion}: {veces} veces")
        if posicion_libre(posiciones, posicion - 1):  # Verificar si la posición está libre
            return posicion - 1  # Retornar el índice de la posición elegida

    # Si no hay posiciones basadas en el punteo, elegir una posición aleatoria
    while True:
        n = randint(0, 8)
        if posicion_libre(posiciones, n):
            return n

def inicio_principal():
    r=str(input('\n'
                '                     TRES EN RAYA\n'
                '\n'
                '                          X/O    \n'
                '\n'
                '         Tenga en cuenta que con X empieza usted: ').upper())
    while r!= 'O' and r!= 'X':
        r=input('                Diga una opcion correcta--> ').upper()
    if r=='O':
        ia='X'
        persona='O'
    else:
        ia='O'
        persona='X'
    return ia, persona

def mostrar_juego(posiciones):
    print(f'\n'
          '                       TRES EN RAYA         \n'
          '\n'
          '\n               1        |2        |3        '
          f'\n                   {posiciones[0]}    |    {posiciones[1]}    |    {posiciones[2]}         '
          '\n                        |         |         '
          '\n               ---------+---------+---------'
          '\n               4        |5        |6        '
          f'\n                   {posiciones[3]}    |    {posiciones[4]}    |    {posiciones[5]}         '
          '\n                        |         |         '
          '\n               ---------+---------+---------'
          '\n               7        |8        |9        '
          f'\n                   {posiciones[6]}    |    {posiciones[7]}    |    {posiciones[8]}         '
          '\n                        |         |         '
          '\n')

def otra_partida():
    r=input('                       ¿Otra partida?          \n'
            '\n'
            '                            si/no\n'
            '\n'
            '                          ---> ')
    while r!= 'si' and r!='no':
        r=input('                      Diga bien --->')
    return r == 'si'


def verificar_ganador(posiciones,jugador):
    if posiciones[0] == posiciones[1] == posiciones[2] == jugador or\
       posiciones[3] == posiciones[4] == posiciones[5] == jugador or\
       posiciones[6] == posiciones[7] == posiciones[8] == jugador or\
       posiciones[0] == posiciones[3] == posiciones[6] == jugador or\
       posiciones[1] == posiciones[4] == posiciones[7] == jugador or\
       posiciones[2] == posiciones[5] == posiciones[8] == jugador or\
       posiciones[0] == posiciones[4] == posiciones[8] == jugador or\
       posiciones[2] == posiciones[4] == posiciones[6] == jugador:
        return True
    else:
        return False

def tablero_lleno(posiciones):
    for i in posiciones:
        if i == ' ':
            return False
    return True

def posicion_libre(posiciones,posicion):
    return posiciones[posicion]== ' '

def posicion_jugar(posiciones):
    lugares=['1','2','3','4','5','6','7','8','9']
    posicion=input('                        Te toca(1-9)\n'
                   '                           --->')
    while posicion not in lugares:
        posicion=input('                      Diga bien --->')
    posicion=int(posicion)-1
    if posicion_libre(posiciones, posicion):
        return posicion
    else:
        print('\n'
              '                     ¡Casilla ocupada!\n')
        return posicion_jugar(posiciones)
    
jugar= True
while jugar:
    posiciones=[' ']*9
    ia,jugador=inicio_principal()
    d=input("\n"
          "                ¿Qué dificultad desea jugar?\n"
          "\n"
          "                      1: Fácil\n"
         "\n"
          "                      2: Normal\n"
          "\n"
          "                      3: Difícil\n"
          "\n"
          "                      4: Imposible\n"
          "\n"
          "                      5: Aprendizaje\n"
          "\n"
          "              Diga una opción correcta --> ")
        
    while d not in ['1', '2', '3', '4','5']:
        d = input('              Diga una opción correcta --> ')
        
    if d == '1':
        dificultad= 'facil'
    elif d == '2':
        dificultad= 'normal'
    elif d == '3':
        dificultad= 'dificil'
    elif d == '4':
        dificultad= 'imposible'
    elif d=='5':
        dificultad='aprendizaje'
    mostrar_juego(posiciones)

    if jugador=='O':
        turno= 'ia'
    else:
        turno= 'jugador'
    partida = True
    while partida:
        if tablero_lleno(posiciones):
            print('                        Empate\n')
            guardar_partida(posiciones, 'empate',ia)
            partida=False
        elif turno == 'jugador':
            posicion=posicion_jugar(posiciones)
            posiciones[posicion] = jugador
            turno = 'ia'
            if verificar_ganador(posiciones, jugador):
                print('\n'
                      '                        ¡Has Ganado!\n')
                guardar_partida(posiciones,'jugador', jugador)
                partida=False
        elif turno == 'ia':
            posicion = movimiento_ia(posiciones, ia,dificultad)
            posiciones[posicion] = ia
            turno = 'jugador'
            mostrar_juego(posiciones)
            if verificar_ganador(posiciones, ia):
                print('\n'
                      '                       ¡Has Perdido!\n')
                guardar_partida(posiciones,'ia',ia)
                partida = False
    jugar=otra_partida()