import random
print("Welcome to Toss section!")
choice = input("What is your choice?? Heads or Tails\n")

HorT = random.randint(0,1)

if HorT == 0:
    print(f"You have chosen {choice} but it was Heads!")
else:
    print(f"You have chosen {choice} but it was Tail!")