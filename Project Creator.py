import os
import sys
import subprocess

#Application intro
print("Hello and Welcome to the Project Builder!!!")
print("-------------------------------------------")
print("How may I be of assistance?")
print("To view project types type (?) ")

type = input("Enter the project type: ")

#Gathering inputs to create appropriate files
if type == "?":
    print("Choose between Python or HTML")
    type = input("Enter the project type: ")

#Seperate statement to the previous to allow the new type to be collected
if type == "Python":
    name = input("Enter the files desired name: ")
    extension = ".py"
    proj = name + extension
    f = open(proj, "x")
    app = 'C:\\Users\\cpbai\\AppData\\Local\\atom\\atom.exe' #Location of IDE
    subprocess.call([app, proj])
    exit()
#The if statement for html projects
elif type == "HTML" or type == "html":
    name = input("Enter the files desired name: ")
    extension = ".html"
    location = "C:\\Users\\cpbai\\PlayGrounds\\Web\\" + name
    os.mkdir(location)
    proj = location + "\\index" + extension
    f = open(proj, "x")
    app = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
    subprocess.call([app, proj])
    exit()
else:
    print("Please restart the program and type a valid input")

input("Press ENTER to Close!!!")
