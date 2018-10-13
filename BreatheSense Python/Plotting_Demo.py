#BreatheSense - SRM Hackathon 2018
#Developer - Dhairya Parikh
#This program shows the basic plotting of Energy Values.

#initializations of the Libraries we are going to use
#--------------------------------------------------------------------------------------------
from __future__ import print_function 
from sys import platform
from os import system
from imp import load_source
from os.path import join
import time
import numpy as np
import matplotlib.pyplot as plt
import array
#--------------------------------------------------------------------------------------------
#walabot initialization to define the path of SDK for both windows and linux platforms
#--------------------------------------------------------------------------------------------
if platform == 'win32':
    modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
        'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')     
wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()
#--------------------------------------------------------------------------------------------

plt.axis([0,1000,0,100]) #pyplot function for defining axis limits in order (xmin, xmax, ymin, ymax)
plt.ion()   #enabling interactive plotting making graph visualization easier.

count = 0

def PrintBreathingEnergy(energy):
    global count
    count+=1
    system('cls' if platform == 'win32' else 'clear')
    print('Energy = {}'.format(energy * 1e7))  
    plt.scatter(count,energy*1000)    #pyplot function that allows us to scatter plot breathing 'energy' values
    plt.pause(0.005)
    Breathecount = energy*1000;
	
def BreathingApp():
    # Walabot_SetArenaR - input parameters
    minInCm, maxInCm, resInCm = 20, 80, 1
    # Walabot_SetArenaTheta - input parameters
    minIndegrees, maxIndegrees, resIndegrees = -4, 4, 2
    # Walabot_SetArenaPhi - input parameters
    minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees = -4, 4, 2
    # Initializes walabot lib
    wlbt.Initialize()
    # 1) Connect : Establish communication with walabot.
    wlbt.ConnectAny()
    # 2) Configure: Set scan profile and arena
    # Set Profile - to Sensor-Narrow.
    wlbt.SetProfile(wlbt.PROF_SENSOR_NARROW)
    # Setup arena - specify it by Cartesian coordinates.
    wlbt.SetArenaR(minInCm, maxInCm, resInCm)
    # Sets polar range and resolution of arena (parameters in degrees).
    wlbt.SetArenaTheta(minIndegrees, maxIndegrees, resIndegrees)
    # Sets azimuth range and resolution of arena.(parameters in degrees).
    wlbt.SetArenaPhi(minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees)
    # Dynamic-imaging filter for the specific frequencies typical of breathing
    wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_DERIVATIVE)
    # 3) Start: Start the system in preparation for scanning.
    wlbt.Start()
    # 4) Trigger: Scan (sense) according to profile and record signals to be
    # available for processing and retrieval.
    while True:
        appStatus, calibrationProcess = wlbt.GetStatus()
        # 5) Trigger: Scan(sense) according to profile and record signals
        # to be available for processing and retrieval.
        wlbt.Trigger()
        # 6) Get action: retrieve the last completed triggered recording
        energy = wlbt.GetImageEnergy()
        # PrintBreathingEnergy(energy)
        PrintBreathingEnergy(energy)
		# 7) Stop and Disconnect.
    wlbt.Stop()
    wlbt.Disconnect()
    print('Terminate successfully')

if __name__ == '__main__':
    BreathingApp()
