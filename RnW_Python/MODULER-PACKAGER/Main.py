import datetime
import math
import uuid
import time

import my_file
import random_data


def module_attributes():
    print("\nExplore Module Attributes:")
            
    module_name = input("Enter module name to explore: ")
            
    try:
        module = __import__(module_name)
        
        print(f"\nAvailable attributes in {module_name} module: ")
        print(dir(module))
        
    except:
        print("\nInvalid module name! Please try again.")

print("=================================")
print("Welcome to Multi-Utility Toolkit")
print("=================================")

if __name__ == "__main__":

    while True:
        
        print("\nChoose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            while True:
                print("\nDatetime and Time Operations:")
                print("1. Display Current Date and Time")
                print("2. Calculate Difference between Two Dates/Times")
                print("3. Format Date into Custom Format")
                print("4. Countdown Timer")
                print("5. Back to Main Menu")
            
                subchoice = int(input("\nEnter your choice: "))
                    
                if subchoice == 1: 
                    print(datetime.datetime.now())
                elif subchoice == 2:
                    first_date = input("Enter first date (dd-mm-yyyy): ")
                    second_date = input("Enter second date (dd-mm-yyyy): ")
                    
                    format = "%d-%m-%Y"
                    
                    f_date = datetime.datetime.strptime(first_date,format).date()
                    s_date = datetime.datetime.strptime(second_date,format).date()
                    
                    difference = s_date - f_date
                    print(difference)
                    
                elif subchoice == 3:
                    date = datetime.datetime.now().date()
                    
                    format_1 = f"{date.day}-{date.month}-{date.year}"
                    format_2 = f"{date.year}-{date.month}-{date.day}"
                    format_3 = date.strftime("%d %B,%Y")
                    
                    while True:
                        print("\nChoose Format Type:")
                        print("1. dd-mm-yyyy")
                        print("2. yyyy-mm-dd")
                        print("3. dd month name, year")
                        print("4. Exit")
                        
                        choice = int(input("\nEnter your choice(1/2/3): "))
                        
                        if choice == 1:
                            print(format_1)
                        elif choice == 2:
                            print(format_2)
                        elif choice == 3:
                            print(format_3)
                        elif choice == 4:
                            print("Exited !")
                            break
                        else:
                            print("Invalid Choice !")
                    
                elif subchoice == 4:
                    seconds = int(input("Enter time in second: "))
                    
                    for i in range(seconds,0,-1):
                        print(i)
                        time.sleep(1)
                        
                    print("Time's up !")
                    
                elif subchoice == 5:
                    print("Going to Main Menu...")
                    break 
                else:
                    print("Invalid Choice !!")
                    
        elif choice == 2:
            while True:
                print("\nMathematical Operations:")
                print("1. Calculate Factorial")
                print("2. Solve Compound Interest")
                print("3. Area of Geometric Shapes")
                print("4. Back to Main Menu")
                
                subchoice = int(input("\nEnter your choice: "))
                
                if subchoice == 1:
                    num = int(input("Enter a num: "))
                    print(math.factorial(num))
                
                elif subchoice == 2:
                    amount = int(input("Enter principal amount: "))
                    interest = float(input("Enter rate of interest (in %): "))
                    year = float(input("Enter time (in year): "))
                    
                    rate = interest/100
                    c_rate = rate+1
                    final_rate = c_rate*c_rate
                    compound_interest = amount*final_rate
                    print("Compound Interest: ",compound_interest)
                
                elif subchoice == 3:
                    while True:
                        print("\nChoose Shape:")
                        print("1. Triangle")
                        print("2. Square")
                        print("3. Rectangle")
                        print("4. Circle")
                        print("5. Exit")
                        
                        shape = int(input("\nEnter your choice: "))
                        
                        if shape == 1:
                            base = float(input("Enter the base of triangle: "))
                            height = float(input("Enter the height of triangle: "))
                            
                            area_tirangle = 0.5*base*height
                            
                            print("The area of triangle is: ",area_tirangle)
                            
                        elif shape == 2:
                            side = int(input("Enter the sides of square: "))
                            print("The area of square is: ",side*side)
                            
                        elif shape == 3:
                            lenght = float(input("Enter the length of rectangle: "))
                            width = float(input("Enter the width of rectangle: "))
                            
                            print("The area of rectangle is: ",lenght*width)
                            
                        elif shape == 4:
                            radius = float(input("Enter the radius of circle: "))
                            pi = 3.14
                            area = pi*radius*radius
                            print("The area of circle is: ",area)
                        
                        elif shape == 5:
                            print("Exited !")
                            break
                        
                        else:
                            print("Invalid Choice !")
                                        
                elif subchoice == 4:
                    print("Going to Main Menu...")
                    break
                
                else:
                    print("Invalid Choice !!")
                    
        elif choice == 3:
            while True:
                print("\nRandom Data Generation:")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Main Menu")
                
                subchoice = int(input("\nEnter Your Choice: "))
                
                if subchoice == 1:
                    print(random_data.random_num())
                elif subchoice == 2:
                    print(random_data.random_list())
                elif subchoice == 3:
                    print(random_data.random_pass())
                elif subchoice == 4:
                    print(random_data.random_otp())
                elif subchoice == 5:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !!")
                    
                
        elif choice == 4:
            print("\nGenerate Unique Identifiers:")
            print()
            print(uuid.uuid4())
            
        elif choice == 5:
            while True:
                print("\nFile Operations:")
                print()
                print("1. Create a new file")
                print("2. Writing to a file")
                print("3. Read from a file")
                print("4. Append to a file")
                print("5. Back to Main Menu")
                
                subchoice = int(input("\nEnter your choice: "))
                
                if subchoice == 1:
                    print(my_file.creating())
                elif subchoice == 2:
                    print(my_file.writing())
                elif subchoice == 3:
                    print(my_file.reading())
                elif subchoice == 4: 
                    print(my_file.appending())
                elif subchoice == 5:
                    print("Going to Main Menu...")
                    break
                else:
                    print("Invalid Choice !!")
                    
            
        elif choice == 6:
            
            module_attributes()
                
        elif choice == 7:
            
            print("\n===============================================")    
            print("Thank you for using the Multi-Utility Toolkit !")
            print("===============================================")    
            
        else:
            print("\nGiven choice is Invalid !!")