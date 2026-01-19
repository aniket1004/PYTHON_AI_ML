
def AreaOfRectangle(length, width):
    """
    Docstring for Area of rectangle
    
    Arguments:
    param length: float
    param width: float

    Returns:
    area : Area of rectangle (float)
    """
    area = 0.0
    area = length * width

    return area

def main():
    try:
        print("Enter the length:")
        length = float(input())

        print("Enter the width:")
        width = float(input())

        if length <= 0.0 or width <= 0.0:
            print("Values should be greater than 0")
        else:
            Ret = AreaOfRectangle(length, width)
            print("Area of rectangle is:", Ret)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()

