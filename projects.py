import os, subprocess, webbrowser, random, re

def on_open():
    subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

def open_project(folder, file_name):

    if re.search('.py|.ipynb', file_name):
        app = "C:\\Users\\cpbai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"


def create_new(file_type, proj_type, proj_name):

    if proj_type == "Personal": parent_dir = "C:\\Users\\cpbai\\OneDrive\\Documents\\Personal Projects\\"
    elif proj_type == "Play Grounds": parent_dir = "C:\\Users\\cpbai\\PlayGrounds\\"

    #Adding file extensions
    if file_type == "Python": 
        f_e = "\\" + proj_name + ".py"
        app = "C:\\Users\\cpbai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    elif file_type == "Note Book": 
        f_e = "\\" + proj_name + ".ipynb"
        app = "C:\\Users\\cpbai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    elif file_type == "Website":
        f_e = "\\index.html"
        app = "C:\\Users\\cpbai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

    path = os.path.join(parent_dir, proj_name)
    os.mkdir(path)
    file_path = os.path.join(path, f_e)
    open(file_path, "x")
    subprocess.call([app, file_path])


    
    
