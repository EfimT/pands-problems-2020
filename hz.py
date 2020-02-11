#Efim Teleaga
#weekly task 4
#Write a program that asks the user to input any positive integer
#  and outputs the successive values of the following calculation.
#  At each step calculate the next value by taking the current value and,
#  if it is even, divide it by two, but if it is odd, multiply it by three 
# and add one. Have the program end if the current value is one.


a = int(input("Enter any positive integer number: "))


while a != 1:

    if int(a) % 2 == 0:
      a = int(a)/2
    else:
      a = int(a)*3+1
    print (a)

print ("end")    
