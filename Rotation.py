import time


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

def RotationStart(Point):
    global RotationPoint
    RotationPoint = Point

def ShowRotation():
    if RotationPoint <= len(rotationList) and isRotaiton == True:
        print("Rotationspunkt: " + str(rotationList[RotationPoint]))
    else:
        print("bitte füge zuerst einen Rotationspunkt hinzu oder achte darauf das der Rotationspunkt nicht größer als die Liste ist")

print(time.strftime("%H:%M:%S"))


while Run:
    Command = input()

    if Command == "/new":
        NewItem()
    elif Command == "/del":
        ShowList()
        print("welcher Index soll gelöscht werden?")
        deletItem(int(input()))
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
    else:
        print("command " + Command + " not found.")
        print("try /help for help")

