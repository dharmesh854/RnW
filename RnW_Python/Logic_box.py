print("Welcome to the Pattern Generator snd Number Analyzer !")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    total = 0
    
    if choice == 1:
        
        num_row = int(input("Enter the number of rows for the pattern: "))
        
        for i in range(1,num_row+1):
            for k in range(1,i+1):
                print("*",end="")
            print()
            
    elif choice == 2:
        
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        for number in range(start,end+1):
            if number%2 == 0:
                print("Number",number,"is Even")
            else:
                print("Number",number,"is Odd")
                
            total += number
            
        print("The sum of",start,"to",end,"is :",total) 
        
    elif choice == 3:
        print("Exiting the program. Goodbye !")
        break
        
    else:
        print("Invalid Choice !")
        
        
            
                 
        