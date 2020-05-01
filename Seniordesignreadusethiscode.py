
import time
import numpy as np
from dual_mc33926_rpi import motors, MAX_SPEED

x = 0.1
motors.enable()
motors.setSpeeds(0, 0)


#=========define functions for driving robot==================#
def right(x):
    endtime = time.time() + x
    while time.time() < endtime:
        motors.motor1.setSpeed(440)
        motors.motor2.setSpeed(420)
        time.sleep(0.25)

def left(x):
    endtime = time.time() + x
    while time.time() < endtime:
        motors.motor1.setSpeed(-440)
        motors.motor2.setSpeed(-420)
        time.sleep(0.25)

def forwards(x):
    endtime = time.time() + x
    while time.time() < endtime:
        motors.motor1.setSpeed(440)
        motors.motor2.setSpeed(-420)
        time.sleep(0.25)


def backwards(x):
    endtime = time.time() + x
    while time.time() < endtime:
        motors.motor1.setSpeed(-440)
        motors.motor2.setSpeed(420)
        time.sleep(0.25)
#=========create mvoes list==================#
moves = []

#=========load movement data from txt file==================#
time.sleep(1)
lines = np.loadtxt('replaydata1.txt')
for line in lines:
    moves.append(line)
    
#=========initialize the state of the button==================#
state = True


#=========retrieve data from list and use data to drive robot==================#    
              #set variable for input from button

    
print('set it up now')
time.sleep(25)

if state == 0: #check if button is pressed
    print('worked')
    file = open('replaydata1.txt','r')  #open text file of movement data
    for n in range(len(moves)):         #cycle through list of movement data
        m = int(moves[n])               #get individual data points from
        if m == 1:                      #list
            right(x)                    #use data points to move motors based
                                #on movement data
            
        if m == 2:
            left(x)
            
            
            
        if m == 3:
            backwards(x)
            
            
            
        if m == 4:
            forwards(x)
            
        
        


    

    


