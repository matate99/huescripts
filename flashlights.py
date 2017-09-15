from __future__ import print_function
import mlbgame, requests, time, datetime

from phue import Bridge





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

def flashlights():
    #This function alternates the lights with the colors of the Milwaukee Brewers 
    b = Bridge('192.168.65.129')

    light1 = getlights(1)
    light3 = getlights(3)

    yellowfast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 11308}
    bluefast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 46014}
    for x in range (0, 8):
        b.set_light(1, yellowfast)
        b.set_light(3, bluefast)
        time.sleep(0.4)
        b.set_light(3, yellowfast)
        b.set_light(1, bluefast)
        time.sleep(0.4)

    revertlights(1, light1)
    revertlights(3, light3);


flashlights()




