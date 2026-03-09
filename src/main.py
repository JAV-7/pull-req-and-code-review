import random

def check_equality(user_guess: int, secret_number: int) -> int:
    """
    This function compares the user's guess with the secret number and returns:

    Parameters:
    -----------
    user_guess: int
        The number guessed by the user.
    secret_number: int
        The secret number that the user is trying to guess.

    Returns:
    -----------
    int
        0 if the user's guess is correct.
        1 if the user's guess is greater than the secret number.
        -1 if the user's guess is less than the secret number.
    """

    if user_guess == secret_number:
        return 0
    elif user_guess > secret_number:
        return 1
    return -1

def loop_until_correct(secret_number: int) -> list:
    """
    This function continuously prompts the user to guess the secret number
    until they guess it correctly. 
    It keeps track of the total number of attempts and the number of correct
    attempts.
    
    Parameter:
    -----------
    secret_number: int
        The secret number that the user is trying to guess.

    Returns:
    -----------
    list
        A list containing the total number of attempts and the number of
        correct attempts.
    """

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
    """
    This function prompts the user to input the lower and upper bounds for the range
    of numbers to be used in the game. It ensures that the user inputs valid integers
    and returns the bounds as a list.

    Parameters:
    -----------
    None

    Returns:
    -----------
    list
        A list containing the lower and upper bounds for the range of numbers.
    """

    while True:
        try:
            bounds = [0,0]
            bounds[0] = int(input("Ingresa el límite inferior del rango: "))
            bounds[1] = int(input("Ingresa el límite superior del rango: "))
            return bounds
        except ValueError:
            print("Por favor, ingrese un número válido.")

def start_game() -> None:
    """
    This function initializes the game by welcoming the user, setting
    the range for the secret number, generating a random secret number
    within that range, and then calling the function to start the guessing
    loop.

    Parameters:
    -----------
    None

    Returns:
    -----------
    None
    """

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
    """
    This function displays the main menu and handles the user's choice.

    Parameters:
    -----------
    None

    Returns:
    -----------
    None
    """

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