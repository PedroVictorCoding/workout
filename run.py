'''

-Alert for workout (Every hour except sleep zone)
-Programmatic workout(x amount of pushups etc. a week)
-Save workout data into a file (json or sql or plain txt)
-Progress check (If underworked show difference and update to new rhythm)
-Graph visualizer


'''
import matplotlib
import os, sys
from playsound import playsound


from apscheduler.schedulers.blocking import BlockingScheduler

def init():
    print("Workout Sess")
    alarmSound()

scheduler = BlockingScheduler()
scheduler.add_job(init, 'interval', hours=1)
scheduler.start()

def alarmSound():
    playsound('doit.mp3')

def currentWorkout():
    '''
    16 times a day of 20 push-ups and 20 sit-ups
    '''
    

def getStats():
    pass

def updateStats():
    pass

def 