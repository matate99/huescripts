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
    light3 = getlights(2)

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    #b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    #b.get_api()



    yellowfast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 11308}
    bluefast = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'hue' : 46014}
    b.set_light(1, yellowfast)
    b.set_light(2, bluefast)
    time.sleep(1)
    b.set_light(2, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(2, bluefast)
    time.sleep(1)
    b.set_light(2, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(2, bluefast)
    time.sleep(1)
    b.set_light(2, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(2, bluefast)


    #b.set_light(1, 'on', True)
    #b.set_light(1, 'bri', 0, transitiontime=1200)
    #b.set_light(1, 'hue', 40000, transitiontime=600)

    # Prints if light 1 is on or not
    print(b.get_light(3, 'hue'))
    print(b.get_light(1, 'hue'))

    revertlights(1, light1)
    revertlights(2, light3);


    #r = requests.put('http://192.168.65.129/api/kl4Il3ktRM6vEN7yO0sDuwUvWKby4UHEfr4tN3d4/lights/1/state', data={"hue": 50000})

    #print(r.text)

flashlights()




