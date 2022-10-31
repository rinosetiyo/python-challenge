import random
card_list = [2,3,4,5,6,7,8,9,10,11]

first_card = random.choice(card_list)
second_card = random.choice(card_list)
com_card = random.choice(card_list)
com_cards = random.choice(card_list)
my_total = first_card + second_card
computer_card = com_card + com_cards
print(f"Your first card {first_card} and your second card {second_card} and total {my_total}" )

print(f"Computer card is {computer_card}")

while my_total <= 16:
  print("You have to add more card !")
  more_card = input("Click 'Y' to add more card : ").lower()
  if more_card == "y":
    add_card = random.choice(card_list)
    my_total += add_card
    print(f"Your more card {add_card} and total {my_total} ")
  
if my_total > computer_card:
  print("You win")
elif my_total < computer_card:
  print("You lose")
elif my_total == computer_card:
  print("Draw !")
