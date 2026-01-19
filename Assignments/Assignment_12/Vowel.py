def IsVowel(char):
    """
    Docstring for IsVowel
    
    Arguments:
    :param char: Character given by user

    Returns:
    bool -> Character is vowel or not
    """
    if char is None or char == "":
        return False
    
    return (
        char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or
        char == "A" or char == "E" or char == "I" or char == "O" or char == "U"
    )

def main():
    
    print("Enter the character:")
    char = input()

    Ret = IsVowel(char)
    if Ret :
        print("Vowel")
    else:
        print("Not vowel")
    

if __name__ == "__main__":
    main()
