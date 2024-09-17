import random

def play_game(win_count, loss_count, tie_count):
    choice_list = ["Rock", "Paper", "Scissors"]

    my_choice = input("Choose your option: Rock, Paper, Scissors (or type 'exit' to quit) ").capitalize()
    if my_choice.lower() == 'exit':
        return False, win_count, loss_count, tie_count

    if my_choice not in choice_list:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        return True, win_count, loss_count, tie_count

    computer_choice = random.choice(choice_list)

    if my_choice == computer_choice:
        print(f"Match tie :: Both Choose {my_choice}")
        tie_count += 1

    elif my_choice == "Rock":
        if computer_choice == "Paper":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. Computer [wins]")
            loss_count += 1
        elif computer_choice == "Scissors":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. You [win]")
            win_count += 1

    elif my_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. You [win]")
            win_count += 1
        elif computer_choice == "Scissors":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. Computer [wins]")
            loss_count += 1

    elif my_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. Computer [wins]")
            loss_count += 1
        elif computer_choice == "Paper":
            print(f"You choose: {my_choice}. Computer choose: {computer_choice}. You [win]")
            win_count += 1

    return True, win_count, loss_count, tie_count

def main():
    print("Welcome to Rock, Paper, Scissors!")
    win_count = 0
    loss_count = 0
    tie_count = 0

    while True:
        continue_game, win_count, loss_count, tie_count = play_game(win_count, loss_count, tie_count)
        if not continue_game:
            break

    print(f"Thanks for playing!")
    print(f"Total Wins: {win_count}")
    print(f"Total Losses: {loss_count}")
    print(f"Total Ties: {tie_count}")

if __name__ == "__main__":
    main()
