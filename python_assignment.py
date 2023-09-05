class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        results = [emp for emp in self.employees if emp.age == age]
        return results

    def search_by_name(self, name):
        results = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        return results

    def search_by_salary(self, operator, salary):
        if operator == ">":
            results = [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            results = [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            results = [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":
            results = [emp for emp in self.employees if emp.salary <= salary]
        else:
            results = []
        return results

    def display_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Matching records:")
            for emp in results:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    table = EmployeeTable()

    # Sample data
    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        age = int(input("Enter age to search: "))
        results = table.search_by_age(age)
    elif choice == "2":
        name = input("Enter name to search: ")
        results = table.search_by_name(name)
    elif choice == "3":
        operator = input("Enter operator (>, <, <=, >=): ")
        salary = float(input("Enter salary to search: "))
        results = table.search_by_salary(operator, salary)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    table.display_results(results)
