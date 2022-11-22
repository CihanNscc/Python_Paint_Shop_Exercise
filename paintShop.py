# Paint Shop Calculator
# Calculate how many gallons of paint required to paint a room.

# Import the math class, for using ceiling rounding
import math


# FUNCTIONS
# Intro messages
def ShowIntroMsgs():
    print("Welcome to the Paint Shop!")
    print("This program will calculate how many gallons of paint you need to paint a room.")


# Input
def getUserInput(dimensionName):
    while True:
        try:
            dimensionValue = float(input("\nEnter the " + dimensionName + " of the room, in feet: "))
            break
        except:
            print("Wrong entry. Please try again.")
    return dimensionValue


# Output
def showFinalOutputs(roomArea, paintGallons):
    print("\nThe total wall area of your room is {0} square feet.".format(roomArea))
    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(paintGallons))


# All calculations in a Class
class paintRoom:

    def __init__(self, length, width, height, squareFeetPerGallon):
        self.length = length
        self.width = width
        self.height = height
        self.squareFeetPerGallon = squareFeetPerGallon

    def calculateTotalArea(self):  # Calculate the total area
        return (self.length * self.height * 2) + (self.width * self.height * 2)

    def calculateNumGallons(self):  # Calculate how many gallons of paint required
        return math.ceil(((self.length * self.height * 2) + (self.width * self.height * 2)) / self.squareFeetPerGallon)


# Main Function (Order of execution)
def main():
    ShowIntroMsgs()

    currentRoom = paintRoom(getUserInput("length"), getUserInput("width"), getUserInput("height"), getUserInput("squareFeetPerGallon"))
    showFinalOutputs(currentRoom.calculateTotalArea(), currentRoom.calculateNumGallons())


main()  # Executing the program
