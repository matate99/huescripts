
from apixu.client import ApixuClient, ApixuException
from phue import Bridge
import time
from flashlights import *

api_key = 'f380fb4c9f9042eba2c131723171409'
client = ApixuClient(api_key)

current = client.getCurrentWeather(q='55344')
forecast = client.getForecastWeather(q='55344')

#print (current['current']['feelslike_f'])  # show temprature in F
#print (forecast['forecast']['forecastday'][0]['day']['maxtemp_f'])  # show temprature in F

highday = forecast['forecast']['forecastday'][0]['day']['maxtemp_f'] #high in F
tempnow = current['current']['temp_f']
highbroken = forecast['forecast']['forecastday'][0]['hour'][6]['temp_f'] #high in F

print (tempnow)

for x in range (0, 24):
    highbroken = forecast['forecast']['forecastday'][0]['hour'][x]['temp_f']
    print (highbroken)



b = Bridge('192.168.65.129')

lightstr = ['', '', '']

for x in range (0, 3):
    lightstr[x] = getlights(x + 1)

#
'''

high = (high**3)*.00002+(high**2)*.0035+high*.4176-5.7344
x = (high + 10)*.0046087 + .14 #This normalized the high for the gamut conversion
y = (x**3)*6.055-(x**2)*10.074+x*5.1201-.4264
color = {'transitiontime' : 1, 'on' : True, 'bri' : 100, 'xy' : [x, y]}
b.set_light(1, color)
time.sleep(60)

color1 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'xy' : [x, y]}
b.set_light(1, color1)

'''


for x in range (0, 12):
    high = x * 10 - 10
    print (high)
    high = (high**3)*.00002+(high**2)*.0035+high*.4176-5.7344
    x = (high + 10)*.0046087 + .14 #This normalized the high for the gamut conversion
    y = (x**3)*6.055-(x**2)*10.074+x*5.1201-.4264
    color = {'transitiontime' : 1, 'on' : True, 'bri' : 250, 'xy' : [x, y]}
    for y in range (0, 3):
        b.set_light(3, color)
    time.sleep(4)
    
for x in range (0, 3):
    revertlights(x + 1, lightstr[x])












