def find_first_repeating_character(s):
    char_count= {}

    for char in s:
        if char in char_count:
            print("First repeating character:", char)
            print("Memory address:", id(char))
            return char
        else:
            char_count[char]= 1

    return None

    print(find_first_repeating_character("hello"))