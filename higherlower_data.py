
"""class CricketPlayer:
        def __init__(self, name, age, highest_run):
            self.name = name
            self.age = age
            self.highest_run = highest_run

    # Create some player objects
player1 = CricketPlayer(name="Virat Kohli", age=33, highest_run=12000)
player2 = CricketPlayer(name="Rohit Sharma", age=34, highest_run=14000)
player3 = CricketPlayer(name="Kane Williamson", age=31, highest_run=10000)

    # Store the player objects in a list
players_list = [player1.__dict__, player2.__dict__, player3.__dict__]

    # Print the list of players
for player in players_list:
    print(f"Name: {player['name']}, Age: {player['age']}, Highest Run: {player['highest_run']}")
print(players_list) """
 

class Players:
    def __init__(self,name,age,run):
        self.name = name 
        self.age = age 
        self.run = run 
p1 = Players("Virat Kohli",35,137.04)
p2 = Players("Rohit Sharma",37,140.89)
p3 = Players("Hardik Pandya",30,140.88)
p4 = Players("Ravindra Jadeja",35,127.16)
p5 = Players("Shivam Dube",31,133.66)
p6 = Players("Axar Patel",30,19.1)
p7 = Players("Rishav Pant",26,126.55)
p8 = Players("Kuldeep Yadav",29,12.4)
p9 = Players("Jasprit Bumrah",30,16.9)
p10 = Players("SuryaKumar Yadav",33,167.74)
p11= Players("Arshdeep Singh",25,13.6)

playerlist = [p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__, p5.__dict__, p6.__dict__,p7.__dict__,p8.__dict__,p9.__dict__,p10.__dict__,p11.__dict__]

