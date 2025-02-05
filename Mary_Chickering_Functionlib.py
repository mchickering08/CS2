import random
import sys

#Function to reverse and display the array
def reverse_array(char_array):
    return char_array[::-1]

#Function to count vowels
def count_vowels(char_array):
    vowels = "aeiouAEIOU"
    vowel_count = {v: 0 for v in vowels}
    
    for char in char_array:
        if char in vowel_count:
            vowel_count[char] += 1
    
    total_vowels = sum(vowel_count.values())
    return total_vowels, vowel_count

#Function to count consonants
def count_consonants(char_array):
    vowels = "aeiouAEIOU"
    consonants = [char for char in char_array if char.isalpha() and char not in vowels]
    
    consonant_count = {}
    for char in consonants:
        consonant_count[char] = consonant_count.get(char, 0) + 1
    
    return len(consonants), consonant_count

#Function to extract first name
def get_first_name(char_array):
    name = "".join(char_array)
    return name.split()[0] if " " in name else name

#Function to extract last name
def get_last_name(char_array):
    name = "".join(char_array)
    return name.split()[-1] if " " in name else name

#Function to extract middle name(s)
def get_middle_name(char_array):
    name = "".join(char_array).split()
    return " ".join(name[1:-1]) if len(name) > 2 else ""

#Function to check if last name contains a hyphen
def last_name_has_hyphen(char_array):
    last_name = get_last_name(char_array)
    return "-" in last_name

#Function to convert to lowercase
def to_lowercase(char_array):
    return [chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in char_array]

#Function to convert to uppercase
def to_uppercase(char_array):
    return [chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in char_array]

#Function to shuffle characters randomly
def randomize_name(char_array):
    shuffled_array = char_array[:]
    random.shuffle(shuffled_array)
    return shuffled_array

#Function to display menu
def menu():
    menu_list = "\nMenu:,1. Reverse name,2. Count vowels,3. Count consonants,4. Get first name,5. Get last name,6. Get middle name(s),7. Check if last name contains hyphen,8. Convert to lowercase,9. Convert to uppercase,10. Randomize name"
    new_menu = menu_list.replace(",", "\n")
    print(new_menu)

# Main program
def main():
    user_input = input("Enter your full name or a word: ")
    char_array = list(user_input)

    while True:
        menu()
        choice = input("Enter your choice (1-17): ")
        
        if choice == "1":
            print("Reversed:", "".join(reverse_array(char_array)))
        elif choice == "2":
            total_vowels, vowels = count_vowels(char_array)
            print(f"Total Vowels: {total_vowels}, Breakdown: {vowels}")
        elif choice == "3":
            total_consonants, consonants = count_consonants(char_array)
            print(f"Total Consonants: {total_consonants}, Breakdown: {consonants}")
        elif choice == "4":
            print("First Name:", get_first_name(char_array))
        elif choice == "5":
            print("Last Name:", get_last_name(char_array))
        elif choice == "6":
            print("Middle Name(s):", get_middle_name(char_array))
        elif choice == "7":
            print("Last name contains hyphen:", last_name_has_hyphen(char_array))
        elif choice == "8":
            print("Lowercase:", "".join(to_lowercase(char_array)))
        elif choice == "9":
            print("Uppercase:", "".join(to_uppercase(char_array)))
        elif choice == "10":
            print("Randomized Name:", "".join(randomize_name(char_array)))
        else:
            print("Invalid choice! Please select a valid option.")
        while True:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                print("Okay!")
                main()
            elif play_again.lower() == "no":
                print("Darn")
                sys.exit()
            else:
                print("Please enter yes or no")
main()
