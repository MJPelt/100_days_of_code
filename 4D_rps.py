import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("Lets play Rock, Paper, Scissors!\n\n")

user_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors. \n"))
computer_choice = random.randint(0, 2)
print(options[user_choice])
print(f"computer chose: \n {options[computer_choice]}")
if user_choice == computer_choice:
    print("Tie. No winner")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice ==1:
    print("You win")
else:
    print("You lose")



