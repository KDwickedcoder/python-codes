def prime_checker(number):
    is_prime = True
    for i in range (2, number-1):
        #if (number%number==0) and (number%1==0):
         # if (number == 2)or(number == 3)or(number == 5):
             # is_prime = False
          if (number%i == 0):
              is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
