NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES): 
    print(NAMES[i], AGES[i])
    i += 1 # goes through list by 1 each time till it reaches the end 

for name in NAMES:
    print(name) #Prints name in list 

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}") #zip function puts two lists together 

for name in reversed(NAMES):
    print(name) #Reverses loop

for i in range(5):
    print(i)

# enumerate
for i, name in enumerate(NAMES): # numbers list when enumerate function is used 
    print (f"{i} {name}")