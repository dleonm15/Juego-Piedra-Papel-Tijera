print("\nBienvenido al juego de \"Piedra, papel y tijeras\", deberán jugar hasta tener a un ganador" )

# Input de nombres
nombre1 = input("\n¿Cómo se llama el jugador 1?: ")
nombre2 = input("\n¿Cómo se llama el jugador 2?: ")

# Nombres con mayúscula inicial
nombrej1 = nombre1.title()
nombrej2 = nombre2.title()

Empate = True

# Input elección
while Empate:
    jugador1 = input("\n" + nombrej1 + ", ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
    jugador2 = input("\n" + nombrej2 + ", ¿Qué eliges? ¿Piedra, papel o tijeras?: ")

# Control sensitive case elección
    minusculasjugador1 = jugador1.lower()
    minusculasjugador2 = jugador2.lower()

# Condiciones de victoria
    condicion1 = minusculasjugador1 == "piedra" and minusculasjugador2 == "tijeras"
    condicion2 = minusculasjugador1 == "papel" and minusculasjugador2 == "piedra"
    condicion3 = minusculasjugador1 == "tijeras" and minusculasjugador2 == "papel"

    if minusculasjugador1 == minusculasjugador2:
        Empate = True
        print ("\n¡Ha sido un empate! Deben jugar nuevamente")
    elif condicion1 or condicion2 or condicion3:
        print ("\nHa ganado " + nombrej1)
        Empate = False
    else:
        print ("\nHa ganado " + nombrej2)
        Empate = False