import AcceptInputModule
from concurrent.futures import ThreadPoolExecutor

def Summation(numbers):
    Sum = 0
    for num in numbers:
        Sum += num
    return Sum

def Product(numbers):
    Product = 1
    for num in numbers:
        Product = Product * num
    return Product

def main():
    N = AcceptInputModule.AcceptNumberOfElements()
    numbers = AcceptInputModule.AcceptNumbersToStoreForList(N)

    executor = ThreadPoolExecutor(max_workers=2)
    
    result_summation = executor.submit(Summation, numbers)

    result_product = executor.submit(Product, numbers)

    print("Summation of given list is:", result_summation.result())
    print("Product of given list is:", result_product.result())

if __name__ == "__main__":
    main()
    