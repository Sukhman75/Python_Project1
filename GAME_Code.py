from random import randint as ri
print("Lets Play Stone-Paper-Scissors....")
print("***")
print("***")
print("***")
print("***")
print("***")
Player= input("Hey 'Player' I am Mr. Computer!! \n ...Make your Move...")

rand_num = ri(0,2)

if rand_num==0:
	computer = "Stone"
elif rand_num==1:
	computer= "Paper"
else:
    computer = "Scissors"

print(f"Mr. Computer plays {computer}")  

if computer == Player:
     print("Its a tie.... PLAY AGAIN.")

elif Player == "Stone":
	if computer == "Paper":
	 print("Mr. Computer wins!!!")
	else:
	 print("You won!!!") 
elif Player == "Scissors":
	if computer == "Stone":
	 print("Mr. Computer wins!!!")
	else: 
	 print("You won!!!")

elif Player == "Paper":
     if Computer == "Scissors":
      print("Mr. Computer wins!!!")	
     else:
      print("You won!!!")    

else: 
	print("Invalid Entry..!! Put some thing from... Stone-Paper-Scissors ")

