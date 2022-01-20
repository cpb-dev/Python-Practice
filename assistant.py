import pyttsx3

engine = pyttsx3.init() #Setting the object "Engine"

def start(): #User choice for program
    mode = input("\nChoose from: \n 1 to continue to speech \n 2 to access settings \n 3 to Exit \n")
    if(mode == "1"):
        talk()
    elif(mode == "2"):
        settings()
    elif(mode == "3"):
        exit()
    else:
        print("\n Please retry! \n")
        start()
    
def settings():
    #Voice Setting
    voices = engine.getProperty('voices') 
    voice = input("What voice do you want?: ")
    if(voice == "f"):
        engine.setProperty('voice', voices[1].id)
    elif(voice == "m"):
        engine.setProperty('voice', voices[0].id)
    #Volume Control
    volume =engine.getProperty('volume') 
    vol = int(input("What volume would you like to adjust to? (between 0-100): "))
    if(vol > 1):
        vol = vol / 100
    engine.setProperty('volume', vol)
    #Speech Rate
    rate = engine.getProperty('rate') 
    speed = int(input("Choose a speed number (150 is standard): "))
    engine.setProperty('rate', speed)

    start()

def talk():
    speech = input("\nWhat do you want the system to say?: ")
    #Actual Speaking
    engine.say(speech)
    engine.runAndWait()
    engine.stop()

    start()

start() #Starting the program

