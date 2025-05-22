#Challenge 35 Extension(Technically 34)
def area():
#Defines the function for calculating area
    shapeArea = length * width
    print(f"Area = {shapeArea}cm squared")

def perimeter():
#Defines the function for calculating perimeter
    shapePerimeter = (length * 2) + (width * 2)
    print(f"Perimeter = {shapePerimeter}cm squared")

def volume():
#Defines the function for calculating perimeter
    shapeVolume = length * width * height
    print(f"Volume = {shapeVolume}cm cubed")
    
length = int(input("Enter the length of the rectange(cm): "))
width = int(input("Enter the width of the rectange(cm): "))
#Gets length and width

response = "None"
while response not in ("a", "p", "v"):
    response = input("Do you want area, perimeter or volume? Enter a, p or v: ")
    response = response.lower()
#Has user tell if they want area perimeter or volume

if response == "a":
    area()
#Displays area
elif response == "p":
    perimeter()
#Displays perimeter
elif response == "v":
    height = int(input("Enter the height of the rectangular prism(cm): "))
    volume()
    