print("--- Python OOP Project: Employee Management System ---")
class Person:
    def __init__(self,name="lika",age=23):
        self.name = name
        self.age = age 
    def display(self):
        print(f"\nPerson created with name: {self.name} and age: {self.age}.")
    def display1(self):
            print(f"\nName: {self.name}\n age: {self.age}")

   
class Employee:
    def __init__(self,name="manish",age=12,id=1234,salary=20000000):
        self.name = name
        self.age = age 
        self.id = id 
        self.salary = salary 

    def show(self,name="Giya",age=12,id=1234,salary=20000000):
        print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.id}, and salary: ${self.salary}.")  

    def display(self):
        print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.id}, and salary: ${self.salary}.")
    def display1(self):
            print(f"Name: {self.name}\nAge: {self.age}\n ID: {self.id}\nSalary: ${self.salary}") 
    def set_ae(self,sy,i):
        self.sy = sy
        self.i = i   
    def get_se(self):
        return self.sy,self.i  
      
    def __del__(self):
        print(f"{self.name},{self.id} Employee deleted")

class Developer(Employee):
    def __init__(self,name,age,id,lang):
        self.name = name
        self.age = age 
        self.__id = id 
        self.lang = lang

    def display(self):
        print(f"Developer created with name: {self.name}, age: {self.age}, ID: {self.__id}, Language: {self.lang}")          
class Manager(Employee):
    def __init__(self,name,age,id,salary,dept):
        self.name = name
        self.age = age 
        self.id = id 
        self.salary = salary
        self.dept = dept

    def display(self):
        print(f"Manager created with name: {self.name}, age: {self.age}, ID: {self.id}, salary: ${self.salary}, and department: {self.dept}.")        
    def display1(self):
            print(f"Name: {self.name}\n Age: {self.age}\n ID: {self.id}\n Salary: ${self.salary}\n Department: {self.dept}") 
while True: 
    print("\nChoose an operation: \n1. Create a Person\n2. Create an Employee\n3. Create a Manager\n4. Show Details\n5. Update salary and id\n6. Delete Employee\n7. Create Developer\n8. Exit")
    num = int(input("\nEnter your choice: "))
    match num:
        case 1: 
            n = input("\nEnter name: ") 
            a = int(input("Enter Age: "))           
            p = Person(n,a) 
            p.display()
            print("\n--- Choose another operation ---")

        case 2:
            employee = {}
            name = input("\nEnter name: ") 
            age = int(input("Enter Age: "))  
            i_d = input("Enter Employee Id: ")
            sa = int(input("Enter Salary(in doller): ")) 
            print("check for super and subclass between employee and manager")       
        
            employee[i_d] = Employee(name,age,i_d,sa)
            d = Developer(name,age,i_d,sa)
            print(super(Employee,Manager))
            print(issubclass(Manager,Employee))
            d.display()
            employee[i_d].display()
            employee[i_d].show("lali",12,200)
            employee[i_d].show(89)
            
            print("\n--- Choose another operation ---")

        case 3:
            n_a = input("Enter Name: ")
            a_g = int(input("Enter Age: "))
            i_ds = input("Enter Employee Id: ")
            s_a = int(input("Enter Salary(in doller): "))
            d_p = input("Enter Department: ")
            m = Manager(n_a,a_g,i_ds,s_a,d_p)
            m.display()
            print("\n--- Choose another operation ---")

        case 4:
            print("\nChoose details to show: \n1. Person\n2. Employee\n3. Manager")
            nu = int(input("\nEnter your choice: "))    
            match nu:    
                case 1:
                    print("Person Details")
                    p = Person(n,a)    
                    p.display1()
                case 2:
                    print("Employee Details")
                    e = Employee(name,age,i_d,sa)
                    employee[i_d].display1()
                case 3:
                    print("Manager Details")
                    m = Manager(n_a,a_g,i_ds,s_a,d_p)    
                    m.display1()
            print("\n--- Choose another operation ---")
        
        case 5:
            sy = int(input("Enter your new salary: "))
            i = input("Enter your new id: ")
            employee[i] = Employee(name,age,i_d,sa)
            employee[i].set_ae(sy,i)
            print(employee[i].get_se())    
        case 6:
            employee[i] = Employee(name,age,i_d,sa)
            del employee[i]
        case 7:
            names = input("Enter Name: ")
            ags = int(input("Enter Age: "))
            ids = input("Enter Employee Id: ")
            lang = input("Enter language: ")
            d = Developer(names,ags,ids,lang) 
            d.display()   
        case 8:
            print("\nExiting the system.All resources have been freed.\n\nGoodbye!") 
        case _:
            print("Invalid Choice")    
            break           
