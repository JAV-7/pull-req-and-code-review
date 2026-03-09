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

def start_game() -> None:
    secret_number = random.randint(1, 20)
    print("¡Bienvenido al juego de adivinar el número!")
    print("¿Puedes adivinar el número secreto entre 1 y 20?")
    attempts = loop_until_correct(secret_number)
    print("Número de intentos realizados:", attempts[0])
    print("Número de intentos acertados:", attempts[1])
    print("Gracias por jugar. ¡Hasta la próxima!")
    
if __name__ == "__main__":
    start_game()