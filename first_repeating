def find_first_repeating_character(s):
    char_count = {}  

    for char in s:
        if char in char_count:
            
            print(f"First repeating character: {char}")
            print(f"Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1

    
    print("No repeating character in the given string.")
    return None

input_string = input("Enter a string: ")
find_first_repeating_character(input_string)
