
from apixu.client import ApixuClient, ApixuException
from phue import Bridge
from flashlights import *

api_key = 'f380fb4c9f9042eba2c131723171409'
client = ApixuClient(api_key)

current = client.getCurrentWeather(q='55344')
tempnow = current['current']['temp_f']

b = Bridge('192.168.65.129')

lightstr = ['', '', '']

for x in range (0, 3):
    lightstr[x] = getlights(x + 1)

tempnow = (tempnow**3)*.00002+(tempnow**2)*.0035+tempnow*.4176-5.7344
x = (tempnow + 10)*.0046087 + .14 #This normalized the high for the gamut conversion
y = (x**3)*6.055-(x**2)*10.074+x*5.1201-.4264
color = {'transitiontime' : 1, 'on' : True, 'bri' : 250, 'xy' : [x, y]}
for y in range (1, 4):
    b.set_light(y, color)
time.sleep(10)
    
for x in range (0, 3):
    revertlights(x + 1, lightstr[x])












