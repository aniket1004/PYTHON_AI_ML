from functools import reduce
import AcceptInputModule
"""
Docstring for filter, map , reduce
    Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
    Map function will increase each number by 10. Reduce will return product of all that numbers
"""
Comparison = lambda No : No >= 70 and No <= 90
Increases = lambda No : No + 10
ProductOfNum = lambda No1, No2 : No1 * No2

def main():
    try:
        N = AcceptInputModule.AcceptNumberOfElements()
        numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

        compare_list = list(filter(Comparison, numbers))
        increase_list = list(map(Increases, compare_list))
        product = 0
        if increase_list is not None and len(increase_list) > 0:
            product = reduce(ProductOfNum, increase_list)

        print("Final output of the reduce is:", product)
        
    except ValueError as vobj:
        print("Input value should be numeric")
    except Exception as eobj:
        print(eobj)
    
if __name__ == "__main__":
    main()