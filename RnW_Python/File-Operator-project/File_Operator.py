import datetime
now = datetime.datetime.now() 

class Option_1:
    
    def __init__(self):
        self.filename = "demo.txt"
        
    def add_entry(self,contain):
        
        with open(self.filename,"a") as file:
            file.write("----------------------------------\n")
            file.write(f"{contain}\n")

class Option_2:
    
    def __init__(self):
        self.filename = "demo.txt"
        
    def view_entry(self):
        with open("demo.txt","r") as file:
           
            contain = file.read()
            print(f"[{now}]")
            print(contain)
            
class Option_3:
    
    def __init(self):
        self.filename = "demo.txt"
        
    def search_entry(self):
        with open("demo.txt","r") as file:
            lines = file.readlines()
             
            keyword = input("Enter a keyword or date to search: \n")
            found = False
            
            for line in lines:
                if keyword in line:
                    print("----------------------------------")
                    print(f"[{now}]")
                    print(line) 
                    found = True
            if not found:
                print(f"\nNo entry found for the keyword: {keyword}")
              
class Option_4:
    
    def __init(self):
        self.filename = "demo.txt"
        
    def delete_entry(self):
        
        confirmation = input("Are you sure you want to delete all entrie? (yes/no): ")
        
        if confirmation == "yes":
            file =  open("demo.txt","w")
            file.close()  
            print("All journal entries have been deleted.")  
        else:
            print("No journal entries to delete.")
            

while True:

    print("\nWelcome to Personal Journal Manager!")
    print("Please select a oprion:")
    print()
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = int(input("User Input: "))
    
    if choice == 1:
        
        contain = input("Enter your journal entry: \n")
        
        obj = Option_1()
        obj.add_entry(contain)
            
        print("Entry added successfully!")
    
    elif choice == 2:
        
        print("\nYour Journal Entries:")
        obj = Option_2()
        obj.view_entry()

    elif choice == 3:
        
        obj = Option_3()
        obj.search_entry()
    
    elif choice == 4:
        
        obj = Option_4()
        obj.delete_entry()
        
    elif choice == 5:
        print("Thank you for using Personal Journal Manager. Goodbye!")
        
    else:
        print("Invalid option. Please select a valid option from the menu.")

        
        
        
        
            