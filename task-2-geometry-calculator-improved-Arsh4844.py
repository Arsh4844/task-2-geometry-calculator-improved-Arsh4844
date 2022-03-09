#while loop is used in starting to loop user wrong input
#user is asked to select shape
#if user select square it will ask side of square and calculate area and perimeter with their formula
#result will be printed and break function used to stop the loop
#if user select 2 it is for rectangle and system will ask length and width in cms
#area and perimeter will be calculated and print in the end
#if user select circle it will ask for the radius in cm and calculate area and perimeter.
#in case user enter wrong input system will loop the yserinput variable again
#author = Arshdeep Singh
#Date Created = jan 31, 2022
#date modified = jan 31, 2022
#This program will ask user to select of which geometry shape he/she want to calculate area and perimeter 
#after selecting by user its dimensions are asked as per the shape and result is presented below
geometry = True#variable created for loop
while geometry == True:#while loop used till user enter a valid input
    userinput = input("Select a geometry shape \n 1) Square \n 2) Rectangle \n 3) Circle \n :-").strip()
    if userinput == "1":
        print("You selected Square")
        a = float(input("Please enter length of Square in cm :- "))#variable a is denoted as side of square
        Area = a*a#Formula for area calculation of square
        perimeter = 4 * a#formula for perimeter 
        print("Area = " + str(Area) + " cm sq")
        print("Perimeter = "+ str(perimeter) + " cm" )
        break#break function used to stop the loop
    elif userinput == "2":
        print("You selected Rectangle")
        l = float(input("Enter Length of rectangle in cm :- "))
        w = float(input("Enter Width of rectangle in cm :-"))
        Area = l*w#area of rectangle
        perimeter = 2*(l+w)#perimeter of rectangle
        print("Area = " + str(Area) + " cm sq")
        print("Perimeter = "+ str(perimeter) + " cm" )
        break
    elif userinput == "3":
        print("You selected Circle")
        r = float(input("Please enter radius of circle in cm :- "))
        Area = 3.14*r*r#Area of circle
        perimeter = 2*3.14*r#perimeter of circle
        print("Area = " + str(Area) + " cm sq")
        print("Perimeter = "+ str(perimeter) + " cm" )
        break
    else:
        print("Invalid input")#if user enter wrong input
        geometry == True

    


