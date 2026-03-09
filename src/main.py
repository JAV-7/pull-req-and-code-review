import random

def check_equality(user_guess: int, secret_number: int) -> int:
    if user_guess == secret_number:
        return 0
    elif user_guess > secret_number:
        return 1
    return -1

def loop_until_correct(secret_number: int) -> list:
    comparison_result = None
    attempts = [0,0]
    while True:
        try:
            user_guess = int(input("Ingresa tu intento: "))
            attempts[0] += 1
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        attempts[1] += 1
        comparison_result = check_equality(user_guess, secret_number)
        if comparison_result == 0:
            print("¡Felicidades! Has adivinado el número.")
            break
        elif comparison_result == 1:
            print("Intenta con un número más bajo.")
        else:
            print("Intenta con un número más alto.")
    return attempts

def set_range() -> list:
    while True:
        try:
            bounds = [0,0]
            bounds[0] = int(input("Ingresa el límite inferior del rango: "))
            bounds[1] = int(input("Ingresa el límite superior del rango: "))
            return bounds
        except ValueError:
            print("Por favor, ingrese un número válido.")

def start_game() -> None:
    print("¡Bienvenido al juego de adivinar el número!")
    print("Primero, vamos a establecer un rango de números para el juego...")
    lower_bound, upper_bound = set_range()
    secret_number = random.randint(lower_bound, upper_bound)
    print(f"¿Puedes adivinar el número secreto entre {lower_bound} y {upper_bound}?")
    attempts = loop_until_correct(secret_number)
    print("Número de intentos realizados:", attempts[0])
    print("Número de intentos acertados:", attempts[1])
    print("Gracias por jugar. ¡Hasta la próxima!")

def menu() -> None:
    while True:
        print("Menú:")
        print("1. Jugar")
        print("2. Salir")
        choice = input("Selecciona una opción (1 o 2): ").strip()
        if choice == "1":
            start_game()
        elif choice == "2":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()