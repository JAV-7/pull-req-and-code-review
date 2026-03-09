import random

def check_equality(user_guess: int, secret_number: int) -> int:
    if user_guess == secret_number:
        return 0
    elif user_guess > secret_number:
        return 1
    return -1

def loop_until_correct(secret_number: int):
    comparison_result = None
    attempts = 0
    while True:
        user_guess = int(input("Ingresa tu intento: "))
        attempts += 1
        comparison_result = check_equality(user_guess, secret_number)
        if comparison_result == 0:
            print("¡Felicidades! Has adivinado el número.")
            break
        elif comparison_result == 1:
            print("Intenta con un número más bajo.")
        else:
            print("Intenta con un número más alto.")
    return attempts

def start_game():
    secret_number = random.randint(1, 20)
    print("Adivina el número entre 1 y 20")
    attempts = loop_until_correct(secret_number)
    print("Número de intentos:", attempts)

if __name__ == "__main__":
    start_game()