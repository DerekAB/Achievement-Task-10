#Name:                  Task 10.py
#Author:                Derek Baker
#Date Created:          24-03-2023
#Date Last Modified:    24-03-2023
#
#Purpose:
#
#This program will calculate the area and perimeter of a rectangle and present the results back to the user

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
#Defining the class object attributes

    def calculatePerimiter(self):
        global perimeter
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
        #defining a method that will calculate the perimeter of the rectangle using the object's attributes
        
    def calculateArea(self):
        global area
        area = self.width * self.height
        return area
        #defining a method that will calculate the area of the rectangle using the object's attributes
        
    def displayInfo(self):
        print('\nWidth: {} cm'.format(self.width))
        print('Height: {} cm'.format(self.height))
        print('Perimeter: {} cm'.format(perimeter))
        print('Area: {} cm squared'.format(area))
        #method that will print out all the information that was input, as well as the perimeter and the area back to the user
        
rectangle = Rectangle(10, 12)        
#defing the variable as an object

rectangle.width = float(input("Please enter the width of the Rectangle (in CM): "))
rectangle.height = float(input('Please enter the height of the Rectangle (in CM): '))
#asking the user for the dimensions of the rectangle

Rectangle.calculatePerimiter(rectangle)
Rectangle.calculateArea(rectangle)
Rectangle.displayInfo(rectangle)
#calling the methods that will calculate and then print the results to the user
