#Challenge 35(Technically 34)
def area():
#Defines the function for calculating area
    shapeArea = length * width
    print(f"Area = {shapeArea}cm")

def perimeter():
#Defines the function for calculating perimeter
    shapePerimeter = (length * 2) + (width * 2)
    print(f"Perimeter = {shapePerimeter}cm")
    
length = int(input("Enter the length of the rectange(cm): "))
width = int(input("Enter the width of the rectange(cm): "))
#Gets length and width

response = "None"
while response not in ("a", "p"):
    response = input("Do you want area, perimeter? Enter a or p: ")
    response = response.lower()
#Has user tell if they want area or perimeter

if response == "a":
    area()
#Displays area
elif response == "p":
    perimeter()
#Displays perimeter