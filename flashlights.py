from __future__ import print_function
import mlbgame, requests, time, datetime, sys

from phue import Bridge

if len(sys.argv) > 1:
    team = sys.argv[1]
else:
    team = ''

color1 = {'transitiontime' : 1, 'on' : False, 'bri' : 0, 'hue' : 000000}
color2 = {'transitiontime' : 1, 'on' : False, 'bri' : 0, 'hue' : 000000}

def getlights(light):
    #This function gets the existing light status and returns a command
    b = Bridge('192.168.65.129')
    lighton = b.get_light(light, 'on')
    lighthue = b.get_light(light, 'hue')
    lightbri = b.get_light(light, 'bri')
    revert = {'transitiontime' : 10, 'on' : lighton, 'bri' : lightbri, 'hue' : lighthue}
    return revert;


def revertlights(light, command):
    #This function changes the lights based on the given command
    b = Bridge('192.168.65.129')
    b.set_light(light, command);

def setbrewers():
    #This function sets the colors for the Milwaukee Brewers 

    global color1
    global color2

    color1 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 11308}
    color2 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 46014}

def setpackers():
    #This function sets the colors for the Milwaukee Brewers 

    global color1
    global color2

    color1 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 10008}
    color2 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 17510}

def flash():
    #This function alternates the lights with the set colors

    global color1
    global color2

    b = Bridge('192.168.65.129')

    light1 = getlights(1)
    light3 = getlights(3)

    for x in range (0, 8):
        b.set_light(1, color1)
        b.set_light(3, color2)
        time.sleep(0.4)
        b.set_light(3, color1)
        b.set_light(1, color2)
        time.sleep(0.4)

    revertlights(1, light1)
    revertlights(3, light3);

def flashbrewers():
    setbrewers()
    flash()

def flashpackers():
    setpackers()
    flash()





if team == 'Brewers':
    flashbrewers()

if team == 'Packers':
    flashpackers()



