#All inputs converted to inputs first
time = int(input("How long did the project take? (give a percentage higher is better): "))
read = int(input("How readable is the code? (give a percentage higher is better): "))
speed = int(input("How fast is the code executed? (give a percentage higher is better): "))

count = time + read + speed #Overall sum
score = count / 300 * 100 #Finding percentage

print("You got: " +  str(score)) #Output

input("Press ENTER to close!!!") #Needed so program doesn't close after execution
