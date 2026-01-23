
def AcceptNumberOfElements():
    N = 0
    print("Number of elements:", end="  ")
    N = int(input())

    return N

def AcceptNumbersToStoreForList(N):
    numbers = list()
    for i in range(N):
        print("Enter the number [", i+1,"]:", end=" ")
        num = int(input())
        numbers.append(num)
    
    return numbers

