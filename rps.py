import random
user_points=(0)
bot_points=(0)
options=["quit","rock","paper","scissors"]
while user_points<=10 or bot_points<10:
    user_number=input("please pick 1 for rock/2 for paper/3 for scissors or 0 to quit ")
    user_number=int(user_number)
    random_number = random.randint(1,3)#picks bots option
    bot_pick=options[random_number]
    user_pick=options[user_number]
    if user_pick == options[0]:
        quit()
    print ("bot picked",bot_pick)
    if user_pick == ("rock") and bot_pick == ("scissors"):
        print("You Win")
        user_points +=1
        print("you have",user_points," points")
        print("bot has",bot_points," points")
    elif user_pick == ("scissors") and bot_pick == ("paper"):
        print("You Win")
        user_points +=1
        print("you have",user_points," points")
        print("bot has",bot_points," points")
    elif user_pick == ("paper") and bot_pick == ("rock"):
        print("You Win")
        user_points +=1
        print("you have",user_points," points")
        print("bot has",bot_points," points")
    elif user_pick == bot_pick:
        print("draw")
    else:
        print("You Lose")
        bot_points +=1
        print("you have",user_points," points")
        print("bot has",bot_points," points")
else:
    if user_points>bot_points:
        print("WELL DONE YOU WIN")
    elif user_points<bot_points:
        print("UNLUCKY YOU LOSE")
    else:
        print("DRAW")    
