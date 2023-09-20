fruits = ['apple', 'peach', 'pear']

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")





    # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
 student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
total_students = 0
for height in student_heights:
    total_height += height
    total_students += 1

average = round(total_height/total_students)
print(average)


#**********************************************************************************************************************************************************

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()      # second method
for n in range(0, len(student_heights)):
 student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
total_students = 0
for height in range (0,len(student_heights)):
    total_height += student_heights[height]
    total_students += 1

average = round(total_height/total_students)
print(average)


#***********************************************************************************************************************************************************


for number in range(1,101):                      # small loops
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:                        # first
        print("Buzz")
    else:
        print(number)




total = 0
for number in range(0,101,2):                  #second
    total+=number
print(total)