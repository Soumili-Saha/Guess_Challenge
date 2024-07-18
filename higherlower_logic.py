import random
import higherlower_logo
import higherlower_data 
score = 0
print(higherlower_logo.logo)
store = True
while store != False:
    player1 = random.choice(higherlower_data.playerlist)
    player2 = random.choice(higherlower_data.playerlist)
    while player2 == player1 :
        player2 = random.choice(higherlower_data.playerlist)
    print("choose who have highest strike rate !!")
    print(f"player 1 : {player1["name"]}")
    print(higherlower_logo.OR)
    print(f"player 2 : {player2["name"]}")
    choose = int(input("enter 1 or 2 :"))
    def result():
        if player1["run"] > player2["run"]:
            if choose == 1:
                print("correct")
                return True
            else :
                print("wrong")
                return False
        else :
            if choose == 1:
                print("wrong")
                return False
            else :
                print("correct")
                return True

    store = result()
    if store == True:
        score += 1
    print("your final score is : ",score)






