def creating():
    try:
        filename = input("Enter file name: ")
        file = open(filename,"x")
        file.close()
        
        return f"\n{filename} file created successfully !! "
        
    except FileExistsError:
        return "File already exist !"
        
    
def writing():
    filename = input("Enter file name: ")
    file_content = input("Enter data to write: ")
    file = open(filename,"w")
    file.write(file_content)
    file.close()
    return "Data written successfully!"
    
    
def reading():
    try:
        filename = input("Enter file name: ")
        file = open(filename,"r")
        print("File Content:")
        content = file.read()
        print(content)
        file.close()
    
    except FileNotFoundError:
        return f"{filename} file not found !"
    
    
def appending():
    filename = input("Enter file name: ")
    file_content = input("Enter content to append: ")
    file = open(filename,"a")
    file.write(file_content)
    file.close()

        
    