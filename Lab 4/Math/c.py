import math
def area_poly(n, l):
    deg=360/(2*n)
    rad=(deg*math.pi)/180
    apoth=l/2*(1/math.tan(rad))
    p=n*l
    print(f"Area of polygon: {round(apoth*p/2, 1)}")
n=int(input("Number of sides: "))
l=int(input("Length of side: "))
area_poly(n,l)