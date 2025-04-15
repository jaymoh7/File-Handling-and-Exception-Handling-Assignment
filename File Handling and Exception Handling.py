def process_file():
    """
    Main function to process a file with error handling.
    Reads content from a user-specified file, modifies it, and writes to a new file.
    """
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read {len(content)} characters from '{input_filename}'")
        
        # Ask for modification type
        print("\nHow would you like to modify the file?")
        print("1. Convert to uppercase")
        print("2. Convert to lowercase")
        print("3. Add line numbers")
        print("4. Replace a word")
        
        choice = input("Enter your choice (1-4): ")
        
        # Process content based on user's choice
        if choice == '1':
            modified_content = content.upper()
            modification_name = "uppercase"
        elif choice == '2':
            modified_content = content.lower()
            modification_name = "lowercase"
        elif choice == '3':
            lines = content.split('\n')
            modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
            modification_name = "line_numbered"
        elif choice == '4':
            word_to_replace = input("Enter the word to replace: ")
            replacement_word = input("Enter the replacement word: ")
            modified_content = content.replace(word_to_replace, replacement_word)
            modification_name = f"replaced_{word_to_replace}"
        else:
            print("Invalid choice. No modifications will be made.")
            modified_content = content
            modification_name = "unmodified"
        
        # Generate output filename
        output_filename = f"{input_filename.split('.')[0]}_{modification_name}.txt"
        
        # Ask user if they want to change the output filename
        custom_filename = input(f"Output will be written to '{output_filename}'. Enter a different name or press Enter to continue: ")
        if custom_filename:
            output_filename = custom_filename
        
        # Try to write to the output file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                print(f"Successfully wrote modified content to '{output_filename}'")
        except PermissionError:
            print(f"Error: You don't have permission to write to '{output_filename}'.")
        except IOError as e:
            print(f"Error writing to file '{output_filename}': {e}")
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except UnicodeDecodeError:
        print(f"Error: '{input_filename}' contains characters that cannot be decoded. It might be a binary file.")
    except IOError as e:
        print(f"Error reading file '{input_filename}': {e}")
    
    # Ask if user wants to process another file
    another = input("\nWould you like to process another file? (y/n): ")
    if another.lower() == 'y':
        process_file()


if __name__ == "__main__":
    print("File Processing Program")
    print("=======================")
    print("This program reads a file, modifies its content, and writes to a new file.\n")
    
    try:
        process_file()
        print("\nThank you for using the File Processing Program!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("The program will exit.")
