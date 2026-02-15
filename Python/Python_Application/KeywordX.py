
def EmployeeInfo(name, age, salary, city):
    print("Name is", name, sep= " : ")
    print("Age is", age, sep= " : ")
    print("Salary is", salary, sep= " : ")
    print("City is", city, sep= " : ")


def main():
    # Keyword
    EmployeeInfo(age=25, name="Rahul", city="Pune", salary=None)

if __name__ == "__main__":
    main()