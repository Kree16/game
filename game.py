import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[rock,paper,scissor] 
choice=int(input("type 0 for rock type 1 for paper type 2 for scissor:"))
print(choice)
print(list[choice])

           
computer_choice=random.randint(0,2)
print(f"computer chose:{computer_choice}")
print(list[computer_choice])

if choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and choice==2:
    print("you lose")
elif choice==1 and computer_choice==0:
    print("you win")        
elif choice<computer_choice:
    print("you lose")    
elif choice==computer_choice:
    print("its a draw")  
else:
    print("you loser")      