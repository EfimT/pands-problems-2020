#this program calculate Body Mass index

weight = float(input("enter body weight in kg:"))
height = float(input ("enter body height in cm:"))

#cm transform in m 100cm=1m
heightm = height/100
BMI=weight/(heightm*heightm) 

print ("your BMI is",BMI)