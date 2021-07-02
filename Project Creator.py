import os
import sys

#Application intro
print("Hello and Welcome to the Project Builder!!!")
print("-------------------------------------------")
print("How may I be of assistance?")
print("To view project types type "?"")

type = input("Enter the project type:")

if type == "?"
    print("Types include Python and Web")
    type = input("Enter the project type:")
else
    name = input("What is the file name?: ")

    if type == "Python"
        save_path = "C:\Users\cpbai\PlayGrounds\Python"
        extension = ".py"
        elif type == "Web"
            save_path = "C:\Users\cpbai\PlayGrounds\Web"
            extension = ".html"

file = name + extension
completed_name = os.path.join(save_path, file)

f = open(completed_name, "x")
f.write("Created the file in " + completed_name)

input("Press ENTER to Close!!!")
