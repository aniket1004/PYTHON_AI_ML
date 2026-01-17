
def EmployeeInfo(name, age, salary, city):
    print("Name is", name, sep= " : ")
    print("Age is", age, sep= " : ")
    print("Salary is", salary, sep= " : ")
    print("City is", city, sep= " : ")


def main():
    # Positional
    #EmployeeInfo("Rahul", 25, 2000.50, "Pune") # Correct
    #EmployeeInfo(25, "Rahul", "Pune", 2000.50) # Wrong

    # Keyword
    EmployeeInfo(age=25, name="Rahul", city="Pune", salary=2000.50)

if __name__ == "__main__":
    main()