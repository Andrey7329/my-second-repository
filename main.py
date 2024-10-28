import random

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "ничья"
    elif (player == 'камень' and computer == 'ножницы') or \
         (player == 'ножницы' and computer == 'бумага') or \
         (player == 'бумага' and computer == 'камень'):
        return "игрок"
    else:
        return "компьютер"

def play_game():
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        try:
            player_choice = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
            if player_choice not in ['камень', 'ножницы', 'бумага']:
                raise ValueError("Некорректный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")

            computer_choice = get_computer_choice()
            print(f"Компьютер выбрал: {computer_choice}")

            winner = determine_winner(player_choice, computer_choice)

            if winner == "игрок":
                player_score += 1
                print("Вы выиграли этот раунд!")
            elif winner == "компьютер":
                computer_score += 1
                print("Компьютер выиграл этот раунд!")
            else:
                print("Это ничья!")

            print(f"Счет: Игрок {player_score} - Компьютер {computer_score}\n")

        except ValueError as e:
            print(e)  # вывод сообщения об ошибке

    if player_score == 3:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("Компьютер выиграл игру. Попробуйте снова!")

# Запуск игры
play_game()