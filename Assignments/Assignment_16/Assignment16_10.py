
def main():
    """
    Docstring for main
    Accept name from user and display length of its name.
    """
    try:
        print("Enter the name:", end=" ")
        name = input()
        
        print (len(name))
        
    except Exception as eobj:
        print(eobj)
    

if __name__ == "__main__":
    main()