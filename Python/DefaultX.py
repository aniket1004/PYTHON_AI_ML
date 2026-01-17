
def EmployeeInfo(name, age, salary, city = "Mumbai"):
    print("Name is", name, sep= " : ")
    print("Age is", age, sep= " : ")
    print("Salary is", salary, sep= " : ")
    print("City is", city, sep= " : ")


def main():
    
    EmployeeInfo("Rahul", 25, 2000.50)
    EmployeeInfo("Rahul", 25, 2000.50, "Pune")

if __name__ == "__main__":
    main()