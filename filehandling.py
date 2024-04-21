# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Hello, this is line 1\n")
        file.write("12345\n")
        file.write("Python File Handling\n")
except PermissionError:
    print("Permission denied. Unable to create or write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied. Unable to read the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading completed.")

# File Appending
try:
    # Open file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
except PermissionError:
    print("Permission denied. Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending completed.")
