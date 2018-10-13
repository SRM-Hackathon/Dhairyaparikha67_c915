#BreatheSense Project - SRM Hackathon 
#This file is the basic API provided by the Walabot
#This program enables the Walabot to convert Breathing Patterns into Energy Values.
#This program sends the Energy values to a MQTT Client 
#My project will be using the energy values.

from __future__ import print_function 
from os import system
from sys import platform
from imp import load_source
from os.path import join
import time
import json
import paho.mqtt.client as mqtt
import threading
import sys 

mqttc = mqtt.Client("BreatheData", clean_session=False)
mqttc.username_pw_set("zcvkuouj", "xUVwWu2tKS6q")
mqttc.connect("m15.cloudmqtt.com", 14487, 60)

              
if platform == 'win32':
    modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
        'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')     
wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()

        
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
        mqttc.publish("sensor/temp", payload=energy*10000000, qos=0)
        time.sleep(2)
        
            
    # 7) Stop and Disconnect.
    wlbt.Stop()
    wlbt.Disconnect()
    wlbt.Clean()
    print('Terminate successfully')
if __name__ == '__main__':
    BreathingApp()
