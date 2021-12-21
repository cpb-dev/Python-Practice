import tkinter as tk
from tkinter import filedialog, Text
import os

if os.path.isfile("save.txt"): #Checking to see if an exe file already exists for program
    with open("save.txt", "r") as f:
        tempapps = f.read()
        tempapps = tempapps.split(",")
        apps = [x for x in tempapps if x.strip()] #Making sure correct apps are shown

root = tk.Tk()
apps = [] #Array to carry all apps

def addApps(): #Function to add apps to a list
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), 
                                        ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runapp(): #Run all apps in the list
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=800, width=800, bg="#457b9d") #Create canvas
canvas.pack()

frame = tk.Frame(root, bg="#a8dadc") #Create outer frame
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

#Create buttons
openFile = tk.Button(root, text="Choose App", padx=10, pady=5, fg="White", bg="#457b9d", command=addApps)
openFile.pack()

runFile = tk.Button(root, text="Open App", padx=10, pady=5, fg="White", bg="#457b9d", command=runapp)
runFile.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")