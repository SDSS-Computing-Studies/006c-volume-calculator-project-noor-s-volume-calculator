#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:Harnoor
    # Modified:
    print("Welcome to our program")

def Sphere(measurement):
    radius=measurement[0]
    V=(4/3)*math.pi*math.pow(radius,3)
    return V
    

def RectangularPrism(measurement):
    length = measurement[0]
    height = measurement[1]
    width = measurement[2]
    V= length*height*width
    return V

def TriangularPrism(measurement):
    length = measurement[0]
    height = measurement[1]
    base = measurement[2]
    V= (1/2)*base*length*height
    return V

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("1=Rectangular Prism")
    print("2=Triangular Prism")
    print("3=Sphere")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    if shape==1:
        x=("Enter the length")
        y=("Enter the height")
        z=("Enter the width")
        prompts=[x,y,z,1]
        return prompts
    elif shape==2:
        x=("Enter the length")
        y=("Enter the height")
        z=("Enter the base")
        prompts=[x,y,z,1]
        return prompts
    elif shape ==3:
        x=("Enter the Radius")
        prompts=[x,1,2]

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements=[]
    
    if questions[-1]==1:
        a=int(input(questions[0]))
        a=measurements.insert(0,a)
        b=int(input(questions[1]))
        b=measurements.insert(1,b)
        c=int(input(questions[2]))
        c=measurements.insert(2,c)
        print(measurements)
        return measurements
    
    elif questions[-1]==2:
        a=int(input(questions[0]))
        a=measurements.insert(0,a)
        return measurements
    
    
def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    run=(1)
    while run!=2:
        instructions()
        a=int(input("Select which shape you wish to calculate"))
        b=getParams(a)
        c=getInputs(b)
        if a==1:
            answer=RectangularPrism(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==2:
            answer=TriangularPrism(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==3:
            answer=Sphere(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
    
        

main()
