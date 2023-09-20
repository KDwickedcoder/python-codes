#str1 = "karan"
#split = list(str1)
#print(split)

inp_no = input("Enter the number:\n")

list1 = list(inp_no)



list2 = []

for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])

str1 = ""
str1 = str1.join(list2)

print("the reverse number is: ",str1)


