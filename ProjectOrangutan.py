print("*************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Functuion that lists Gas Stations, randomly choosing one, and Return its value
def gasLevelGauge():
    gasLevelList =["Empty","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel

#Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def listOfGasStation():
    gasStations =["Shell","Speedway","Exxon","Meijers","Costco","Marathon","BP","Circle K","Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby
    

# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlret():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQaurterTank = round(random.uniform(25.1,50),1)
