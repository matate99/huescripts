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
    b.set_light(1, yellowfast)
    b.set_light(3, bluefast)
    time.sleep(1)
    b.set_light(3, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(3, bluefast)
    time.sleep(1)
    b.set_light(3, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(3, bluefast)
    time.sleep(1)
    b.set_light(3, yellowfast)
    b.set_light(1, bluefast)
    time.sleep(1)
    b.set_light(1, yellowfast)
    b.set_light(3, bluefast)


    #b.set_light(1, 'on', True)
    #b.set_light(1, 'bri', 0, transitiontime=1200)
    #b.set_light(1, 'hue', 40000, transitiontime=600)

    # Prints if light 1 is on or not
    print(b.get_light(3, 'hue'))
    print(b.get_light(1, 'hue'))

    revertlights(1, light1)
    revertlights(3, light3);


    #r = requests.put('http://192.168.65.129/api/kl4Il3ktRM6vEN7yO0sDuwUvWKby4UHEfr4tN3d4/lights/1/state', data={"hue": 50000})

    #print(r.text)


outs = 0
runs = 0
calls = 0
now = datetime.datetime.now()
game = mlbgame.day(now.year, now.month, now.day, home='Brewers', away='Brewers')[0]
myoverview = mlbgame.overview(game.game_id)


if myoverview.home_team_name == 'Brewers':
    home = 1
    away = 0
elif myoverview.away_team_name == 'Brewers':
    home = 0
    away = 1

print(myoverview.status)
while myoverview.status == 'Preview' or myoverview.status == 'Warmup':
    calls = calls + 1
    myoverview = mlbgame.overview(game.game_id)
    now = datetime.datetime.now()
    print(calls, myoverview.time_date)
    print(now)
    time.sleep(300)
     
while myoverview.status == 'In Progress':

    calls = calls + 1
    myoverview = mlbgame.overview(game.game_id)
    now = datetime.datetime.now()

    if home == 1:
        if myoverview.home_team_runs > runs:
            runs = myoverview.home_team_runs
            flashlights()
            print ('RUNS RUNS RUNS RUNS RUNS RUNS RUNS RUNS')
    elif away == 1:
        if myoverview.away_team_runs > runs:
            runs = myoverview.away_team_runs
            flashlights()
            print ('RUNS RUNS RUNS RUNS RUNS RUNS RUNS RUNS')
            
    #print(game.home_team_runs)
    print(myoverview.status, myoverview.balls, myoverview.strikes, myoverview.outs)
    print(calls, now)
    time.sleep(3)
    if myoverview.outs == 3:
        time.sleep(24)
        outs = 0
    elif myoverview.outs > outs:
        outs = myoverview.outs
        print ('Youre out of there')
        time.sleep(24)





