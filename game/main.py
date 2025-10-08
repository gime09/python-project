import random
import os
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input(Fore.CYAN + 'piedra, papel o tijera -> ').lower()

    if user_option == 'salir':
        return 'salir', 'salir'

    if user_option not in options:
        print(Fore.RED + '⚠️  Esa opción no es válida')
        return None, None

    computer_option = random.choice(options)
    print('')
    print(Fore.MAGENTA + f'Oponente => {computer_option}')
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print(Fore.YELLOW + '🤝 ¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print(Fore.GREEN + '🪨 Piedra gana a tijera → USUARIO ¡GANA!')
            user_wins += 1
        else:
            print(Fore.RED + '📄 Papel gana a piedra → OPONENTE ¡GANA!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print(Fore.GREEN + '📄 Papel gana a piedra → USUARIO ¡GANA!')
            user_wins += 1
        else:
            print(Fore.RED + '✂️ Tijera gana a papel → OPONENTE ¡GANA!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print(Fore.GREEN + '✂️ Tijera gana a papel → USUARIO ¡GANA!')
            user_wins += 1
        else:
            print(Fore.RED + '🪨 Piedra gana a tijera → OPONENTE ¡GANA!')
            computer_wins += 1

    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        # Limpia la pantalla entre rondas
        os.system('clear' if os.name == 'posix' else 'cls')

        print(Fore.CYAN + Style.BRIGHT + '****************')
        print(Fore.CYAN + Style.BRIGHT + f'ROUND {rounds}')
        print(Fore.CYAN + Style.BRIGHT + '****************')
        print(Fore.WHITE + f'Oponente: {computer_wins} - Usuario: {user_wins}')
        print(Fore.YELLOW + "📝 Escribí 'salir' para terminar el juego.\n")

        user_option, computer_option = choose_options()
        if user_option is None:
            input(Fore.WHITE + "\nPresioná ENTER para continuar...")
            continue

        if user_option == 'salir':
            print(Fore.CYAN + '\n👋 Gracias por jugar. ¡Hasta la próxima!')
            break

        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins
        )

        rounds += 1

        if computer_wins == 2:
            print(Fore.RED + '\n======================')
            print(Fore.RED + '🏆 EL CAMPEÓN ES EL OPONENTE')
            print(Fore.RED + '======================\n')
            break

        if user_wins == 2:
            print(Fore.GREEN + '\n======================')
            print(Fore.GREEN + '🏆 EL CAMPEÓN ES EL USUARIO')
            print(Fore.GREEN + '======================\n')
            break

        input(Fore.WHITE + "\nPresioná ENTER para continuar a la siguiente ronda...")


run_game()

