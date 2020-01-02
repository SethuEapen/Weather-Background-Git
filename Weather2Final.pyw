import ctypes
import math
import os.path
import requests, json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

setup = "C:/Program Files/Weather Background Changer/setup.txt"
file = open(setup, 'r')
f = file.readlines()
newList = []
for line in f:
    newList.append(line[:-1])
path = newList[0]
textSize = newList[1]
city_name = newList[2]
api_key = newList[3]
file.close()

created = ["thunder", "snow", "rain"]
clear = ["wind", "clouds", "clear"]

#Find time of day
time = datetime.now()
now = time.hour
dCycle = "night"
if now >= 4 and now < 7:
    dCycle = "morning"
elif now >= 7 and now < 18:
    dCycle = "day"
elif now >= 18 and now < 20:
    dCycle = "evening"


#Get the current weather
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404": 
    y = x["main"]
    z = x["weather"]
    weather_description = z[0]["main"]
    weather_detailed = z[0]["description"]
    temp = (9.0/5.0)*(y["temp"]-273.0)+32.0
else: 
    print(" City Not Found ") 


def showWeather():
    #pasting the weather to the base image
    foreground_folder_path = path + "/Weather/"
    image = Image.open(full_path)
    if weather_description.lower() == "thunderstorm" or weather_description.lower() == "snow" or weather_description.lower() == "rain":
        image2 = Image.open(foreground_folder_path + weather_description.lower() + ".png").convert("RGBA")
        image2 = image2.resize(image.size)
        image.paste(image2, (0,0), image2)
    elif not (weather_description.lower() == "clear" or weather_description.lower() == "wind" or weather_description.lower() == "clouds"):
        image2 = Image.open(foreground_folder_path + "fog.png").convert("RGBA")
        image2 = image2.resize(image.size)
        image.paste(image2, (0,0), image2)
    #Drawing the stats
    font_type = ImageFont.truetype("C:/WINDOWS/FONTS/ALGER.TTF", int(textSize))
    draw = ImageDraw.Draw(image)
    x, y = image.size
    fx, fy = font_type.getsize(city_name + ":")
    draw.text(xy=((x-fx-5),0), text=city_name + ":", fill=(255,255,255), font=font_type)
    fx, fy2 = font_type.getsize(weather_detailed)
    draw.text(xy=((x-fx-5),fy), text=weather_detailed, fill=(255,255,255), font=font_type)
    text = str(int(temp)) + "°F " 
    fx, fy3 = font_type.getsize(text)
    draw.text(xy=(x-fx-5, fy2+fy), text=text, fill=(255,255,255), font=font_type)
    text = "Last Updated: " + str(time.strftime("%I:%M:%S %p"))
    fx, fy4 = font_type.getsize(text)
    draw.text(xy=(x-fx-5, fy3+fy2+fy), text=text, fill=(255,255,255), font=font_type)
    image.save("C:/Program Files/Weather Background Changer/current.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Program Files/Weather Background Changer/current.jpg" , 0)

#what is the weather
full_path = path + '/' + dCycle + ".jpg"
if os.path.exists(full_path):
    showWeather()


