import time
import os
from readchar import readkey, readchar, key

def timeconvert (time):
    return time*60

#This technically behaves as I wanted it to but it needs CTRL+C/Z to quit which isn't user friendly. 
def countdown(timegiven, label):
    try:
        print("Press CTRL+C or CTRL+Z to Exit")
        while timegiven:
            #time // 60
            #time % 60
            minute, second = divmod(timegiven, 60)
            print(f"{label}: {minute:02d}:{second:02d}", end="\r")
            time.sleep(1)
            timegiven -= 1
    except KeyboardInterrupt:
        pass

    #60
#    while True:
#        print("Press Any Key to Exit")
#        while timegiven:
            #time // 60
            #time % 60
#            minute, second = divmod(timegiven, 60)
#            print(f"{label}: {minute:02d}:{second:02d}", end="\r")
#            time.sleep(1)
#            timegiven -= 1
#        exitKey = readchar()
#        if exitKey == key.ENTER:
#            break

def pomodoro(work, rest):
    #convert min to sec
    worksec = timeconvert(work)
    restsec = timeconvert(rest)
    countdown(worksec, "Work")
    os.system("clear||cls")
    countdown(restsec, "Rest")
    os.system("clear||cls")

work = int(input("Enter work time (min): "))
rest = int(input("Enter rest time (min): "))
os.system("clear||cls")
pomodoro(work, rest)
