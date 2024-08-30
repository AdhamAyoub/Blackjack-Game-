import random
from art import logo
from replit import clear

def card_deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_on = True

    for _ in range(2):
        user_cards.append(card_deck())
        computer_cards.append(card_deck())

    while game_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        else:
            user_turn = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_turn == 'y':
                user_cards.append(card_deck())
            else:
                game_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_deck())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()  
    play_game()
