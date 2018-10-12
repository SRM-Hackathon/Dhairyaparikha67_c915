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
b_magnitude = 0
b_counter = 0
nb_counter = 0
gen_counter = 0
lb_counter = 0
sb_counter = 0
i = 0
bn_counter = 0    #Breath Stop Detection

msg_array = []    #an unsized list created to store 'dots' & 'dashes'
wrd_array = []    #an unsized list created to store english alphabets


def BreatheSense(energy):    #the main function in BreatheSense where the breath detection,conversion to morse code and speech output takes place

    global counter
    global b_magnitude
    global b_counter      #Counter which increments when the user is breathing
    global nb_counter     #Counter which increments when user is not breathing
    global gen_counter    #general counter which increments in either case
    global lb_counter     #Counter which increments when a Long Breathe is detected
    global sb_counter	  #Counter which increments when a Short Breathe is detected
    global msg_array      #Array which stores the morse code message
	global wrd_array      #Array which stores the corresponding words to the messages

#Shown Below is the message sheet with 26 words	
#-----------------------------------------------------------------------------------------		
    dash = '-'
    dot = '.'
    m_a = ['.-']
    m_b = ['-...']
    m_c = ['-.-.']
    m_d = ['-..']
    m_e = ['.']
    m_f = ['..-.']
    m_g = ['--.']
    m_h = ['....']
    m_i = ['..']
    m_j = ['.---']
    m_k = ['-.-']
    m_l = ['.-..']
    m_m = ['--']
    m_n = ['-.']
    m_o = ['---']
    m_p = ['.--.']
    m_q = ['--.-']
    m_r = ['.-.']
    m_s = ['...']
    m_t = ['-']
    m_u = ['..-']
    m_v = ['...-']
    m_w = ['.--']
    m_x = ['-..-']
    m_y = ['-.--']
    m_z = ['--..']
    l_a = 'HI'
    l_b = 'NAME'
    l_c = 'IT'
    l_d = 'HOW'
    l_e = 'ARE'
    l_f = 'FOOD'
    l_g = 'YOU'
    l_h = 'IS'
    l_i = 'NEED'
    l_j = 'THIS'
    l_k = 'WORK'
    l_l = 'HELP'
    l_m = 'PROBLEM'
    l_n = 'ME'
    l_o = 'OTHER'
    l_p = 'PLEASE'
    l_q = 'THANKS'
    l_r = 'RIGHT'
    l_s = 'STAND'
    l_t = 'TALK'
    l_u = 'GOOD'
    l_v = 'BAD'
    l_w = 'LOOK'
    l_x = 'DHAIRYA'
    l_y = 'I'
    l_z = 'WANT'
#----------------------------------------------------------------------------------------------
    system('cls' if platform == 'win32' else 'clear')
    b_magnitude = energy*10000000
    
    counter+=1
    gen_counter+=1
	
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
        BreatheSense(energy)
		# 7) Stop and Disconnect.
    wlbt.Stop()
    wlbt.Disconnect()
    print('Terminate successfully')

if __name__ == '__main__':
    BreathingApp()
