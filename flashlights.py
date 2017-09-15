from __future__ import print_function
import mlbgame, requests, time, datetime

from phue import Bridge





def getlights(light):
    b = Bridge('192.168.65.129')
    lighton = b.get_light(light, 'on')
    lighthue = b.get_light(light, 'hue')
    lightbri = b.get_light(light, 'bri')
    revert = {'transitiontime' : 10, 'on' : lighton, 'bri' : lightbri, 'hue' : lighthue}
    return revert;

def revertlights(light, command):
    b = Bridge('192.168.65.129')
    b.set_light(light, command);



def flashlights():
    b = Bridge('192.168.65.129')

    light1 = getlights(1)
    light3 = getlights(3)

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    #b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    #b.get_api()



    yellowfast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 11308}
    bluefast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 46014}
    for x in range (0, 3):
        b.set_light(1, yellowfast)
        b.set_light(3, bluefast)
        time.sleep(0.4)
        b.set_light(3, yellowfast)
        b.set_light(1, bluefast)
        time.sleep(0.4)
    


    print(b.get_light(3, 'hue'))
    print(b.get_light(1, 'hue'))

    revertlights(1, light1)
    revertlights(3, light3);


    #r = requests.put('http://192.168.65.129/api/kl4Il3ktRM6vEN7yO0sDuwUvWKby4UHEfr4tN3d4/lights/1/state', data={"hue": 50000})

    #print(r.text)

flashlights()




