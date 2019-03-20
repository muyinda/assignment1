# 

#number3 finding  the factorial of a given number
num = int(input("enter a number of your choice: "))
fac = 1
for b in range (1, num + 1):
    fac = fac*b
print("factorial of " ,num, " is ", fac)    


# number 2 it required reversing the provided string
str = "The name is sharon" [::-1]
print(str)      

# number5 retruning an array

school=[

    ["john", "sarah", "jog"],
    ["Enoc", " martha", "cris"],
    [0,1,2,3,4,5,6],
    [6,9,0,4,2]
]
print(school)

students= [
    {"sharon":"stuborn", "mary": "cool"},
    {"martha": "unbearable", "shidah":"quite"}
]  
print(students)
print("sharon")

# number 4 returning the length of the longest word
word = "provided"
print(len(word))

# number1 
# from Celcius to fahrenheit
cel = input("enter temperature in celsius: ")
fahrenheit = (celsius*9/5) +32
print("temperature in fahrenheit =", fahrenheit)












