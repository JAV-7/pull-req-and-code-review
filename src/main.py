import random

def start_game():
    secret_number = random.randint(1, 20)
    user_guess = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    while user_guess != secret_number:
        user_guess = int(input("Ingresa tu intento: "))
        attempts += 1
        if user_guess < secret_number:
            print("Muy bajo")
        elif user_guess > secret_number:
            print("Muy alto")
        elif user_guess == secret_number:
            print("¡Correcto!")
        else:
            print("Error")
    print("Número de intentos:", attempts)
start_game()