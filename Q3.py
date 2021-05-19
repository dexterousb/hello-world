#Q3) Python Program to Calculate the Area of a Triangle, square, and rectangle, circle by taking user input

#Triangle

#user input base ,height
base = float(input("Enter base of triangle:"))
height = float(input("Enter height of triangle:"))
areat = float(1/2*base*height)

#sqaure
side = float(input("Enter side of square:"))
areas = float(side*side)

#Rectangle
length = float(input("Enter length of rectangle:"))
breadth = float(input("Enter breadth of rectangle:"))
arear = float(length*breadth)

#Circle
radius = float(input("Enter radius of circle:"))
areac = float(3.14*radius*radius)

#display
print("Area of triangle is : " , areat)
print("Area of square is : " , areas)
print("Area of rectangle is : " , arear)
print("Area of circle is : " , areac)
