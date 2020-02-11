#efim Teleaga
#Check if number is prime
#The primes are 2,3,5,7,11...

p = 10
m = 2
isprime=True

while m < p:   #could be replaced by : for m in range (2,p-1):
    if p % m == 0:
        print (m , "divides",p, "and therefore",p, "is not prime")
        isprime=False
        break
    m = m +1
if isprime:
        print (p,"is a prime number") 
else:
     print (p,"is not prime number")     
        
print ("Thank you for running my program")        