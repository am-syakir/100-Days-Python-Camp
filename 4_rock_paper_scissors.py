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

#Write your code below this line 👇

user = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for scissors.\n"))

if user > 2:
    print("Invalid input. Please restart.")
else:
    print("\nUser:")
    
    images = [rock, paper, scissors]
    print(images[user])
      
    
    import random
    
    print("\nComputer:")
    
    comp = random.randint(0, 2)
    print(images[comp])
    
    if user == comp:
        print("Draw!")
    elif user == 0 and comp == 2:
        print("You Won!")
    elif user == 2 and comp == 0:
        print("You Lost!")        
    elif user < comp:
        print("You Lost!")
    elif user > comp:
        print("You Won!")