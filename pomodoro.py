import time
import os

def timeconvert (time):
    return time*60

def countdown(timegiven, label):
    #60
    while timegiven:
        #time // 60
        #time % 60
        minute, second = divmod(timegiven, 60)
        print(f"{label}: {minute:02d}:{second:02d}", end="\r")
        time.sleep(1)
        timegiven -= 1

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
pomodoro(work, rest)