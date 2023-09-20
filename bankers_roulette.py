# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #--------------> this could also be written as names_string.split()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



random_chose = random.choice(names)               # this is the first code to print the random choice
 
print(random_chose+" is going to buy the meal today!")

print("\n")

#********************************************************************************************************************************************************************* 
length = len(names)   

random_chose1 = random.randint(0,length-1)        # this is the second code to print the random choice

chose = names[random_chose1]

print(chose +" is going to buy the meal today!")