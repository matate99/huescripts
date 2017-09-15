from __future__ import print_function
import mlbgame, requests, time, datetime
from phue import Bridge
from flashlights import *

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
            flashbrewers()
            print ('RUNS RUNS RUNS RUNS RUNS RUNS RUNS RUNS')
    elif away == 1:
        if myoverview.away_team_runs > runs:
            runs = myoverview.away_team_runs
            flashbrewers()
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





