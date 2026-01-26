import sys

def main():
    border = "-" * 50
    print(border)
    print("------------- Marvellous  Automation -------------")
    print(border, end="\n\n")
    
    if len(sys.argv) == 2:
        
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform ")
            print("This is automation script")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ____")
            print("Argument2 : ____")
        
        else:
            print("Use the given flag as:")
            print("--U : Use to display the usage")
            print("--H : Use to display the help")

    else:
        print("Invalid number of command line arguments")   
        print("Use the given flag as:")
        print("--U : Use to display the usage")
        print("--H : Use to display the help")

    print("")
    print(border)
    print("----------- Thank you for using our script--------")
    print("------------- Marvellous Infosystems -------------")
    print(border, end="\n\n")

if __name__ == "__main__":
    main()