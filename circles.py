from math import pi
def circle_area(r):
    rent= pi*(r**2)
    return rent
#test function     
radii= [2,0,-3,2+5j,True,"radius"]
message= "Area of circles with r= {radius} is {area}."

for r in radii:
    a= circle_area(r)
    print(message.format(radius=r,area=a))
