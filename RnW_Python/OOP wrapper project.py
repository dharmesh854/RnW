class Employee:
    
    def __init__(self,name,age,Id,salary):
        self.name = name
        self.age = age
        self.Id = Id
        self.salary = salary
        
    def getInfo(self):
        print(f"\nEmployee Name : {self.name} \n Age : {self.age} \n Employee ID : {self.Id} \n Salary : {self.salary} ")

        
class Manager(Employee):
    
    def __init__(self,name,age,Id,salary,department):
        super().__init__(name,age,Id,salary)
        self.department = department
        
    def getInfo(self):
        print(f"\nManager Name : {self.name} \n Age : {self.age} \n Manager ID : {self.Id} \n Salary : {self.salary} \n Department : {self.department} ")
                

class Developer(Employee):
    
    def __init__(self,name,age,Id,salary,department,language):
        super().__init__(name,age,Id,salary)
        self.department = department
        self.language = language
        
    def getInfo(self):
        print(f"\nDeveloper Name : {self.name} \n Age : {self.age} \n Developer ID : {self.Id} \n Salary : {self.salary} \n Department : {self.department} \n Language : {self.language} ")
        
       
emp = []
man = []
dev = []

def empInfo():
    name = input("\nEnter Employee Name: ")
    age = int(input("Enter Age: "))
    id = input("Enter Employee ID: ")
    salary = input("Enter Salary: ")
    
    print(f"\nEmployee created with Name : {name}, Age : {age}, ID : {id} and Salary : {salary}")
    
    obj = Employee(name,age,id,salary)
    
    emp.append(obj)
    
def manInfo():
    name = input("\nEnter Manager Name: ")
    age = int(input("Enter Age: "))
    id = input("Enter Manager ID: ")
    salary = input("Enter Salary: ")
    department = input("Enter Department: ")
    
    print(f"\nManager created with Name : {name}, Age : {age}, ID : {id}, Salary : {salary} and Department = {department}")
    
    obj = Manager(name,age,id,salary,department)
    
    man.append(obj)
    
def devInfo():
    name = input("\nEnter Developer Name: ")
    age = int(input("Enter Age: "))
    id = input("Enter Developer ID: ")
    salary = input("Enter Salary: ")
    department = input("Enter Department: ")
    language = input("Languages Known: ")
    
    print(f"\nDeveloper created with Name : {name}, Age : {age}, ID : {id}, Salary : {salary}, Department = {department} and Languages : {language}")
    
    obj = Developer(name,age,id,salary,department,language)
    
    dev.append(obj)
    
    

print("\n --- Pyhton OOP Project: Employee Management System ---\n")


while True:

    print("\nChoose an operation: ")
    print("1. Create a Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")
    
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:

        empInfo()
        print("\n--- Choose another operation ---")
        
    elif choice == 2:
        
        manInfo()
        print("\n--- Choose another operation ---")
        
    elif choice == 3:

        devInfo()
        print("\n--- Choose another operation ---")
        
    elif choice == 4:
        
        print("1. employee")
        print("2. Manager")
        print("3. Developer")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            
            print("\nEmployee Details: ")
            for em in emp:
                em.getInfo()      
            
        elif ch == 2:
            
            print("\nManager Details: ")
            for mn in man:
                mn.getInfo()
            
        elif ch == 3:
            
            print("\nDeveloper Details: ")
            for dv in dev:
                dv.getInfo()
            
        else:
            print("Invvalid Choice !!")
            
    elif choice == 5:
        
        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye !!")
        break
    
    else:
        print("Invalid choice !!")
            