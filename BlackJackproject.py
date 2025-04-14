#program to build a blackjack game
import random

print('Welcome to Black jack game')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards = []

computer_cards = []


for i in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
print(user_cards)
print(computer_cards[0])

Total_user = user_cards[0] + user_cards[1]

Total_computer = computer_cards[0] + computer_cards[1]

if Total_user == 21:

    if Total_computer == 21:
        print(computer_cards)
        print(Total_computer)
        print('Draw!')

    elif Total_computer < 21:
        print(computer_cards)
        print(Total_computer)
        print('You WON ')

while Total_user < 21:
    choice  = input("Enter you choice 'hit' or 'Reveal' : ")

    if choice.lower() == 'hit':
        user_cards.append(random.choice(cards))

        Total_user += user_cards[len(user_cards)+1]
        





