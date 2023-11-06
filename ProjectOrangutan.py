print("\n**********************************************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Rain", "Foggy","Windy",'Icy',"Sunny","Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather() once in our Vehicle Responce System - VRS
weatherAlert = weather()

# VRS() function will allow my vehicle to respond based weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 MPH")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 45 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 30 MPH")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 10 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 60 MPH")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated your alarm by 25 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 MPH")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated your alarm by 60 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 25 MPH")
    elif weatherAlert == "Sunny":
        print("The weather forcast is calling for calling for a",weatherAlert, "day. Enjoy your drive to work")
    else:
        print("The weather forcast is calling for calling for a",weatherAlert, "day. Enjoy your drive to work")

vehicleResponseSystem()
