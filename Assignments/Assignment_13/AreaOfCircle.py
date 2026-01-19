
import math

def AreaOfCircle(radius):
    """
    Docstring for Area of Circle
    
    Arguments:
    param radius: float

    Returns:
    area : Area of circle (float)
    """
    area = 0.0
    area = math.pi * radius * radius

    return area

def main():
    try:
        print("Enter the radius:")
        radius = float(input())

        if radius <= 0.0:
            print("Values should be greater than 0")
        else:
            Ret = AreaOfCircle(radius)
            print("Area of circle is:", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

