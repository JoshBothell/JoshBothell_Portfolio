# September 8, 2020
# Josh Bothell
# CS1400 Section 02
# Assignment 1
# Goal of the project is to create a program that calculates the distance to pull back a slingshot/catapult
# based on an angle and distance to a target affectionately referred to as 'the professor'

# importing libraries
import math
import time

# establishing constants
M = 0.065  # Mass of the egg
K = 25  # Elastic constant
G = 9.8  # Gravitational constant (on earth)


# setting up a function to calculate 'x', as well as doing some error checking.
def egg_yeet(distance, theta):
    try:
        x = math.sqrt((M * G * distance) / (K * math.sin(2 * theta)))
        return x
    except (ValueError, ZeroDivisionError):
        print("Uh oh, looks like some of your values were not valid. Let's start over.")
        return "error"


# main loop takes inputs and handles exit. also does some general error checking.
def main():
    loop = True
    while loop:
        try:
            response = input("Hello, please enter the exact distance to the professor in meters,\n"
                             "or type 'exit' to exit the program\n")
            if response.lower() == "exit":
                print("goodbye!")
                print("...")
                time.sleep(2)
                loop = False
            else:
                distance = float(response)
                theta = math.radians(float(input("Thank you!\n"
                                                 "Please enter the angle of elevation in exact degrees: ")))
                x = egg_yeet(distance, theta)
                if x == "error":
                    input("...")
                    continue
                x = '{:04.3f}'.format(x)  # formats the distance to be prettier
                print("You should pull back the slingshot", x, "meters to nail the professor!\n"
                                                               "hit enter to continue")
                input()
                continue
        except ValueError:
            print("Oops, that wasn't a valid input, let's try again.\n")
            continue


# running main loop
main()
