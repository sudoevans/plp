filename=input("What is the file name? with extension :")

with open(filename, 'w') as file:
    file.write("This is added info...")
    file.close() 

# Handling with errors
def read_file_with_error_handling(filename):

    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print("An I/O error occurred while reading the file.")

# Get filename from user
filename = input("Enter the filename: ")
read_file_with_error_handling(filename)



    



