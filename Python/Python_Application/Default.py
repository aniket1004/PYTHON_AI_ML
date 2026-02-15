
def EmployeeInfo(name, age, salary, city = "Pune"):
    print("Name is", name, sep= " : ")
    print("Age is", age, sep= " : ")
    print("Salary is", salary, sep= " : ")
    print("City is", city, sep= " : ")


def main():
    
    EmployeeInfo(age=25, name="Rahul", salary=2000.50)

if __name__ == "__main__":
    main()