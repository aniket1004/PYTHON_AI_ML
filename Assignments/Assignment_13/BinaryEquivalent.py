
def BinaryEquivalent(iNo):
    binary = ""
    while iNo > 0:
        binary = binary + str(iNo % 2)
        iNo = iNo // 2
    binary_equivalent = ""
    for i in range(len(binary)-1, -1, -1):
        binary_equivalent = binary_equivalent + binary[i]
    return binary_equivalent

def main():
    try:
        print("Enter the number:")
        No = int(input())

        if No <= 0:
            print("Values should be greater than 0")
        else:
            binary = BinaryEquivalent(No)
            print("Binary Equivalent is:", binary)
    except ValueError as vobj:
        print(vobj)
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()