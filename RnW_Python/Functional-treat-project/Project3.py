record = []

def input_data():
    global record
    user_input = input("Enter data for a 1D array (separated by spaces): ")
    record = list(map(float, user_input.split()))
    
    print("Data has been stored successfully!")

def display_data():
    print("Data Summary:")
    print(f"- Total elements: {len(record)}")
    print(f"- Minimum value: {min(record)}")
    print(f"- Maximum value: {max(record)}")
    print(f"- Sum of all vales: {sum(record)}")
    print(f"- Average value: {sum(record)/len(record) if record else 0}")
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_menu():
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}")
    
def filter_data():
    threshold = int(input("Enter a threshold value to filter data above this value: "))
    
    filtered_value = list(filter(lambda x: x >= threshold, record))
    
    print("Filtered data (values >= threshold):")
    print(filtered_value)
    
def sort_data():
    print("Choose sorting option:")
    print("1. Ascending Order")
    print("2. Descending Order")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        sorted_data = sorted(record)
        print("Sorted data in Ascending order: ")
    else:
        sorted_data = sorted(record, reverse=True)
        print("Sorted data in Descending order: ")
    print(sorted_data)
    
def data_statistics():
        
    print("Dataset Statistics:")
    print(f"- Minimum value: {min(record)}")
    print(f"- Maximum value: {max(record)}")
    print(f"- Sum of all vales: {sum(record)}")
    print(f"- Average value: {sum(record)/len(record) if record else 0}")


while True:
    
    print("Welcome to the Data Analyzer and Transformer Program.")
    
    print("Main Menu:")
    
    print("1. Input Data")
    print("2. Display Data")
    print("3. Calculate Factorial")
    print("4. Filter Data by threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    
    choice = int(input("Please enter your choice (1-7): "))
    print()
    
    if choice == 1:
        input_data()
    elif choice == 2:
        display_data()
    elif choice == 3:
        factorial_menu()
    elif choice == 4:
        filter_data()
    elif choice == 5:
        sort_data() 
    elif choice == 6:
        data_statistics()
    elif choice == 7:
        print("Thank you for using Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
                 
    
        
        