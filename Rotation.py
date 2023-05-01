import time

EndTime = 0
rotationList = []
Run = True
isRotaiton = False
RotationPoint = 0

def NewItem():
    print("New Item Name...")
    rotationList.append(str(input()))

def deletItem(Index):
    print("Item gelöscht")
    del rotationList[Index]

def ShowList():
    print("Derzeitige Liste:" + str(rotationList))

def Help():
    print("<-----------------------  Command List  ----------------------->")
    print("/new     -> fügt ein neuen Punkt in der Rotation hinzu")
    print("/del     -> löscht einen Punkt in der Rotation nach dem Index")
    print("show     -> zeigt die derzeitige Rotation")
    print("/help    -> command Liste")
    print("/exit    -> beendet den Vorgang")
    print("/time    -> zeigt derzeitige Uhrzeit")

def RotationHelp():
    print("<-----------------------  Rotation  ----------------------->")
    print("/r          -> zeigt den derzeitigen Rotationspunkt ")
    print("/r start    -> startet und legt den Startpunkt der Rotation fest")
    print("/r next     -> springt zur nächsten Rotations Punkt")
    print("/r jump     -> springt zum ausgewählten Rotations Punkt")
    print("/r end      -> beendet die Rotation")

def AlarmHelp():
    print("<-----------------------  Alarm  ----------------------->")
    print("/a          -> zeigt den derzeitigen Alarm ")
    print("/a set      -> startet und legt den Startpunkt des Alarms fest")
    print("/a clear    -> löscht den Alarm")
    print("/a help     -> zeigt Alarm Command List")



def RotationStart(Point):
    global RotationPoint
    RotationPoint = Point

def ShowRotation():
    if RotationPoint <= len(rotationList) and isRotaiton == True:
        print("Rotationspunkt: " + str(rotationList[RotationPoint]))
    else:
        print("bitte füge zuerst einen Rotationspunkt hinzu oder achte darauf das der Rotationspunkt nicht größer als die Liste ist")

def AlarmStart(EndTimeUser):
    
    global StartTimeMinute
    StartTimeMinute = time.strftime("%M")
    
    global StartTimeHour
    StartTimeHour = time.strftime("%H") 

    global EndTime 
    EndTime = EndTimeUser
    global EndTimeStr 
    EndTimeStr = str(EndTime)




print(time.strftime("%H:%M:%S"))

#--------------------------------------Commands---------------------------------#
while Run:
    Command = input()

    if Command == "/new":
        NewItem()
    
    elif Command == "/del":
        ShowList()
        print("welcher Index soll gelöscht werden?")
        Item = int(input())
        if Item <= len(rotationList) - 1:
            deletItem(int(Item))
        else: 
            print("Item konnte nicht gelöscht werden")

    elif Command == "/show":
        ShowList()

    elif Command == "/help":
        Help()

    elif Command == "/exit":
        Run = False
        exit()
    
    elif Command == "/time":
        print(time.strftime("%H:%M:%S"))
    
    elif Command == "/r":
        ShowRotation()
    
    elif Command == "/r start":
        if isRotaiton == False:
            print("wo willst du mit der Rotation anfangen")
            RotationStart(int(input()))
            if RotationPoint >= len(rotationList):
                print("bitte füge zuerst die Anzahl an werte in die Liste hinzu")
            else:
                isRotaiton = True
        else:
            print("es läuft bereits eine Rotation")
    
    elif Command == "/r next":
        if RotationPoint + 1 == len(rotationList):
            RotationPoint = 0
            ShowRotation()
        else:
            RotationPoint += 1 
            ShowRotation()
    
    elif Command == "/r jump":
        if isRotaiton == True:
            print("wo willst du mit der Rotation hinspringen")
            RotationStart(int(input()))
        else:
            print("start erst eine Rotation.")
    
    elif Command == "/r end":
        print("Rotation abgebrochen")
        isRotaiton = False
        RotationPoint = 0
    
    elif Command == "/r help":
        RotationHelp()
    
    elif Command == "/a ":
        print("...")
    
    elif Command == "/a help":
        AlarmHelp()
    
    elif Command == "/a set":
        print("Schreibe HHMM")
        AlarmStart(int(input()))
        print("Alarm auf " + str(EndTimeStr[0:2]) + ":" + str(EndTimeStr[2:]))
    
    elif Command == "/a clear":
        print("...")
    else:
        print("command " + Command + " not found.")
        print("try /help for help")


    if time.strftime("%H%M") == str(EndTime):
       print("ALARM")
