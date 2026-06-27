import random
li = []


def random_num():
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    return random.randint(start,end)
    
def random_list():
    lst = input("Enter elements to make it's list: ")
    li.append(lst)
    print(li)
    
def random_pass():
    print(random.randint(10000000,99999999))
    
def random_otp():
    print(random.randint(100000,999999))

            
            
        
        
