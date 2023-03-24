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
        
    def calculatePerimiter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
        
    def calculateArea(self):
        global area
        area = self.width * self.height
        return area
    
    def displayInfo(self):
        print('\nWidth: {} cm'.format(self.width))
        print('Height: {} cm'.format(self.height))
        print('Area: {} cm squared'.format(area))
        
rectangle = Rectangle(0, 0)        

rectangle.width = float(input("Please enter the width of the Rectangle (in CM): "))
rectangle.height = float(input('Please enter the height of the Rectangle (in CM): '))

Rectangle.calculatePerimiter(rectangle)
Rectangle.calculateArea(rectangle)
Rectangle.displayInfo(rectangle)

