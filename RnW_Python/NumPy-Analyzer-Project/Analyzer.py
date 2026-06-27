import numpy as np


class Analytics:
    
    def create_array(self):
        while True:
            print("\nSelect the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            
            sbc = int(input("Enter your choice: "))
        
        
            if sbc == 1:
                
                elements = list(map(int, input(f"Enter elements for array (separated by the space): ").split()))
                arr = np.array(elements)
                print()
                print(arr)
                return arr
                
                
            elif sbc == 2:
                
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                
                total = rows*cols
                
                elements = list(map(int, input(f"Enter {total} elements for array (separated by the space): ").split()))
                
                length = len(elements)
                
                if length == total:
                
                    arr = np.array(elements).reshape(rows,cols)
                
                    print("\nArray Created successfully:")
                    print(arr)
                    return arr
                
                else:
                    print("You entered more/less elements ! ")
                
            
            else:
                print("Invalid Choice !")
                
                
    def math_operations(self,arr):
        
        while True:
            print("\nChoose a Mathematical Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            
            sbc = int(input("\nEnter your choice: "))
            
            elements = list(map(int, input(f"Enter {arr.size} elements for array (separated by the space): ").split()))
            
            arr2 = np.array(elements).reshape(arr.shape)
            
            print("\nOriginal Array:")
            print(arr)
                
            print("\nSecond Array:")
            print(arr2)
                
            if sbc == 1:
                print(f"\nResult of Addition:")
                print(arr + arr2)
                return
                    
            elif sbc == 2:
                print("\nResult of Substraction:")
                print(arr - arr2)
                return
                    
            elif sbc == 3:
                print("\nResult of Multiplication:")
                print(arr * arr2)
                return
                    
            elif sbc == 4:
                print("\nResult of Division:")
                print(arr / arr2)
                return
            
            else:
                print("Invalid Choice !")
                    
            
    def combine_split(self,arr):
        
        while True:
            print("\nChoose an Operation:")
            print("1. Combine Arrays")
            print("2. Split Arrays")
            
            sbc = int(input("Enter your choice: "))
            
            if sbc == 1:
                while True:
                    print("\nChoose how you want to combine:")
                    print("1. Combine Array Vertically")
                    print("2. Combine Array Horizontally")
                    
                    combine = int(input("Enter your choice: "))
                    
                    if combine == 1:
                        elements = input(f"\nEnter the elements of another array to combine ({arr.size} elements separated by space): ").split()
                        nums = [int(x) for x in elements]
                        
                        arr3 = np.array(nums).reshape(arr.shape)
                        
                        print("\nOriginal Array:")
                        print(arr)
                        
                        print("\nSecond Array:")
                        print(arr3)
                        
                        
                        print("\nCombined Array (Vertical Stack):")
                        print(np.vstack((arr,arr3)))
                        return
                        
                    elif combine == 2:
                        elements = input(f"\nEnter the elements of another array to combine ({arr.size} elements separated by space): ").split()
                        nums = [int(x) for x in elements]
                        
                        arr3 = np.array(nums).reshape(arr.shape)
                        
                        print("\nOriginal Array:")
                        print(arr)
                        
                        print("\nSecond Array:")
                        print(arr3)
                        
                        
                        print("\nCombined Array (Horizontal Stack):")
                        print(np.hstack((arr,arr3)))
                        return
                    
                    else:
                        print("Invalid Choice !")
            
            
            elif sbc == 2:
                
                print("Your array's length is:",arr.size)
                parts = int(input("Enter the number of part you want to split: "))
                length = arr.size
                
                if length%parts==0:
          
                    arr3 = np.split(arr,parts)
                    
                    print("\nOriginal Array:")
                    print(arr)
                    print("\nSplited Array:")
                    print(arr3)
                    return
                
                else:
                    print(f"{arr.size} elements can not divide in {parts} parts !")
                
            else:
                print("Invalid Choice !") 
                
    
    def search_sort_array(self,arr):
        
        while True:
            print("\nChoose an Option:")
            print("1. Search a Value")
            print("2. Sort the Array")
            
            sbc = int(input("Enter your choice: "))
            
            if sbc == 1:
                
                element = int(input("Enter any one number you want to search: "))
                
                if element in arr:
        
                    print(np.where(arr==element))
                    return
                else:
                    print(f"Element {element} not found in array.")
                    
                
            elif sbc == 2:
                
                while True:
                    
                    print("Choose how you want to sort:")
                    print("1. Sort Row-wise")
                    print("2. Sort Column-wise")
                    
                    sort = int(input("Enter your choice: "))
                    
                    if sort == 1:
                        arr4 = np.sort(arr,axis = 1)
                        
                        print("\nOriginal Array:")
                        print(arr)
                        
                        print("\nSorted Array (Sorting applied row-wise.):")
                        print(arr4)
                        return
                    
                    elif sort == 2:
                        arr4 = np.sort(arr,axis = 0)
                        
                        print("\nOriginal Array:")
                        print(arr)
                        
                        print("\nSorted Array (Sorting applied column-wise.):")
                        print(arr4)
                        return
                    
                    else:
                        print("Invalid Choice !")
                
            else:
                print("Invalid Choice !")
                
    def statistical_oprs(self,arr):
        
        while True:
            print("\nChoose an Aggregate/Stastical Operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            
            sbc = int(input("Enter your choice: "))
            
            if sbc == 1:   
                print(np.sum(arr))   
                return     
            elif sbc == 2:    
                print(np.mean(arr)) 
                return              
            elif sbc == 3:
                print(np.median(arr))
                return                   
            elif sbc == 4:
                print(np.std(arr)) 
                return       
            elif sbc == 5:
                print(np.var(arr))
                return
                               
   
     
obj = Analytics()
        

print("Welcome to the NumPy Analyzer !")
print("===================================")

arr = None


while True:
    print("\nChoose an Option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search or Sort Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        arr = obj.create_array()
         
    elif choice == 2:
        obj.math_operations(arr)
                
    elif choice == 3:
        obj.combine_split(arr)
        
    elif choice == 4:
        obj.search_sort_array(arr)
        
    elif choice == 5:
        obj.statistical_oprs(arr)
        
    elif choice == 6:
        print("\nThank you for using the NumPy Analyzer!")
        print("Goodbye !")
        break      
    
    else:
        print("Invalid Choice ! ") 
            


