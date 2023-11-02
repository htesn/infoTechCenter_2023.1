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
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQaurterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low,checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The Closest gas station is",listOfGasStation(),"which is",milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a Quarter of a Tank of gasoline,checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The Closest gas station is", listOfGasStation(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has a half of a tank which is enough to get to your destinations.")
    elif gasLevelIndicator == "Three quarter Tank":
        print("Your gas tank is at three quarter tank!")
    else:
        print("Your gas tank is full -Yeah! - Congratulation! -Vroom Vroom!")


gasLevelAlert()




