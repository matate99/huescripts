
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

high = forecast['forecast']['forecastday'][0]['day']['maxtemp_f'] #high in F

b = Bridge('192.168.65.129')

lightsr = getlights(1)


high = (high**3)*.00002+(high**2)*.0035+high*.4176-5.7344
x = (high + 10)*.0046087 + .14 #This normalized the high for the gamut conversion
y = (x**3)*6.055-(x**2)*10.074+x*5.1201-.4264
color = {'transitiontime' : 1, 'on' : True, 'bri' : 100, 'xy' : [x, y]}
b.set_light(1, color)
time.sleep(60)

revertlights(1, lightsr)




#
'''

for x in range (0, 23):
    high = x * 5 - 10
    print (high)
    high = (high**3)*.00002+(high**2)*.0035+high*.4176-5.7344
    x = (high + 10)*.0046087 + .14 #This normalized the high for the gamut conversion
    y = (x**3)*6.055-(x**2)*10.074+x*5.1201-.4264
    color1 = {'transitiontime' : 1, 'on' : True, 'bri' : 100, 'xy' : [x, y]}
    b.set_light(1, color1)
    time.sleep(4)
    


color1 = {'transitiontime' : 1, 'on' : True, 'bri' : 254, 'xy' : [x, y]}
b.set_light(1, color1)

'''









