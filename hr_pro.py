class Employee:
    #Employee class here
    def __init__(self, name, age, salary, employment_year ):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return 2020 - self.employment_year
    
    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %s" % (self.name, self.age, self.salary, self.get_working_years())
    

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage ):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %s" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

        
def main():
	# main code here
    user_input = 0
    employees = [] 
    managers = []
    print("Welcome to HR Pro 2019")
    while True:
        print("Options:")
        print("	1. Show Employees")
        print("	2. Show Managers")
        print("	3. Add An Employee")
        print("	4. Add A Manager")
        print("	5. Exit")
        print("")

        user_input = input("What would you like to do? ")
        if user_input == 5:
            break
        elif user_input == 1:
            print("Employees")
            for e in employees:
                print(e)
        elif user_input == 2:
            for m in managers:
                print("Managers")
                print(m)
        elif user_input == 3:
            new_e_name = input("Name: ")
            new_e_age = input("Age: ")
            new_e_salary = input("Salary: ")
            new_e_year = input("Employement year: ")
            new_e = Employee(new_e_name, new_e_age,new_e_salary,new_e_year)
            employees.append(new_e)
            print("Employee added succesfully")
        elif user_input == 4:
            new_m_name = input("Name: ")
            new_m_age = input("Age: ")
            new_m_salary = input("Salary: ")
            new_m_year = input("Employement year: ")
            new_m_perc = input("Bonus Percentage: ")
            new_m = Manager(new_m_name, new_m_age,new_m_salary,new_m_year, new_m_perc)
            managers.append(new_m)
            print("Manager added succesfully")
        else:
            print("invalid input")
        


if __name__ == '__main__':
	main()
