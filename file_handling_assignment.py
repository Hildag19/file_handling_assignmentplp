# File Creation
try:
    # Create and write to the file
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line here\n")
except IOError as e:
    print("Error occurred while writing to file:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    # Read and display the contents of the file
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")

# File Appending
try:
    # Open the file in append mode and add additional lines
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("67890\n")
        file.write("Yet another appended line\n")
except IOError as e:
    print("Error occurred while appending to file:", e)

