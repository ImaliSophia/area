
#this program calculates area
print("We will be calculating area.")
print("For a rectangular shape type 1,for a circle type 2,for a triangle type 3 and for a trapizium type 4")
choice = int(input("Type your choice"))
if choice == 1:
    print("you chose rectangular shape")
    L = int (input("Enter your length"))
    W = int (input("Enter your width"))
    Area = L*W
    print("The area of your rectangular shape is",str(Area)+"sq cm")
elif choice == 2:
    print("You chose circle")
    r = int(input("Enter the radius"))
    Area = 3.14*(r**2)
    print("The area of your circle is",str (Area) + "sq cm")
elif choice == 3:
    print("You chose a triangle")
    H = int(input("Enter the height"))
    B = int(input("Enter the base"))
    Area = (B*H)/2
    print("The area of your triangle is",str(Area) + "sq cm")
elif choice == 4:
    print("You chose trampizium")
    A = int(input("Enter the shorter length"))
    B = int(input("Enter the longer length"))
    H = int(input("Enter the height"))
    Area = ((A+B)/2)*H
    print("The area of your trapizium is",str(Area) + "sq cm")



    
