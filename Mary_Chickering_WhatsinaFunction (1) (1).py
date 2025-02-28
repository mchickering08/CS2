'''
┌───────────────────────────────────────────────────────────────────────────┐
│                           What's in a Function?                           │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: User will input a name and can choose from the list of       |
| options to decide what to do with the name (i.e. manipulate, split, etc)  |                             
└───────────────────────────────────────────────────────────────────────────┘
'''
import random
import sys

#First, last, middle, palendrome, initial, consisnents, voels
def remove_title(user_input):
    user_input = user_input.split(' ')  
    special_titles = ['dr.', 'sr.', 'jr.', 'sir.', 'ph.d', 'jr.', 'Dr.', 'Sr.', 'Jr.', 'Sir.', 'Esq.', 'Ph.d', 'Jr.'] 

    for name in user_input:                           
        if to_lowercase(name) in special_titles:
            user_input.remove(name)   
    return(user_input)
#Function to reverse and display the array
def reverse_array(user_input):
    first_name = get_first_name(user_input)
    return to_lowercase(first_name[::-1])
#Function to count vowels
def count_vowels(user_input):
    user_input = remove_title(user_input)
    vowels = list('aeiou')
    vowel_count = {v: 0 for v in vowels}

    for word in user_input:
        for char in word:
            if to_lowercase(char) in vowels:
                vowel_count[to_lowercase(char)] += 1    
    total_vowels = sum(vowel_count.values())
    return total_vowels, vowel_count
#Function to count consonants
def count_consonants(user_input):
    user_input = remove_title(user_input)
    consonants = list('bcdfghjklmnpqrstvwxyz')
    consonant_count = {c: 0 for c in consonants}
    for word in user_input:
        for char in word:
            if to_lowercase(char) in consonants:
                consonant_count[to_lowercase(char)] += 1    
    total_consonants = sum(consonant_count.values())
    return total_consonants, consonant_count
#Function to extract first name
def get_first_name(user_input):
    return remove_title(user_input)[0]                                           
#Function to extract last name
def get_last_name(user_input):
    user_input = remove_title(user_input)
    if len(user_input) > 1:
        return user_input[-1]
    else:
        return 'No last name'
#Function to extract middle name(s)
def get_middle_name(user_input):
    user_input = remove_title(user_input)
    if len(user_input) > 2:
        return ' '.join(user_input[1:-1])
    else:
        return 'No middle name'
#Function to check if last name contains a hyphen
def last_name_has_hyphen(user_input):
    return '-' in get_last_name(user_input)
#Function to convert to lowercase
def to_lowercase(user_input):
    return ''.join([chr(ord(char) + 32) if 'A' <= char <= 'Z' 
            else char for char in user_input])
#Function to convert to uppercase
def to_uppercase(user_input):
    return ''.join([chr(ord(char) - 32) if 'a' <= char <= 'z' 
            else char for char in user_input])
#Function to shuffle characters randomly
def randomize_name(user_input):
    first_name = list(get_first_name(user_input))
    random.shuffle(first_name)
    return to_lowercase(''.join(first_name))
#Function to check if first name is a palindrome
def is_first_name_palindrome(user_input):
    first_name = get_first_name(user_input)
    return to_lowercase(first_name) == reverse_array(first_name)
#Function to sort full name alphabetically
def sorted_full_name(user_input):
    user_input = remove_title(' '.join(user_input.split('-')))
    return ' '.join(sorted(user_input))
#Function to generate initials
def get_initials(user_input):
    user_input = remove_title(' '.join(user_input.split('-')))
    initials = ''

    for name in user_input:
        initials += to_uppercase(name[0])
    return initials
#Function to check if name contains a title/distinction
def has_title(user_input):
    titles = ['dr.', 'dr', 'doctor', 'sir.', 'sir', 'esq', 'ph.d', 'mrs.', 'ms.', 'mr.']
    user_input = to_lowercase(user_input)
    return any(title in user_input.split() for title in titles)
#BONUS: Function to replace vowels with asterisks (*)
def censor_vowels(user_input):
    user_input = ' '.join(remove_title(user_input))  # Remove titles first
    return ''.join('*' if to_lowercase(char) in 'aeiou'
        else char for char in user_input)
#BONUS: Function to count ASCII values sum
def ascii_sum(user_input):
    user_input = ' '.join(remove_title(user_input))
    return sum(ord(char) for char in user_input)
#BONUS pyramid
def print_pyramid(listed_user_input):
    n = len(listed_user_input)
    pyramid = ''
    for i in range(n):
        multiply = n - i - 1
        pyramid += '\n' + ' ' * multiply + ''.join(listed_user_input[:i+1])
    return pyramid
#Function to display menu
def menu():
    menu_list = '\nMenu:,1. Reverse name,2. Count vowels,3. Count consonants,4. Get first name,5. Get last name,6. Get middle name(s),7. Check if last name contains hyphen,8. Convert to lowercase,9. Convert to uppercase,10. Randomize name,11: Check if first name is a palendrome,12: Sort name in alphabetical order,13: Get initials,14: Check for titles/distinctions,15: Replace vowels with asterisks,16: Print ASCII scale sum,17: Print name in a pyramid'
    new_menu = menu_list.replace(',', '\n')
    print(new_menu)
# Main program
def main():
    while True:
        user_input = input('Enter your full name or a word: ')
        characters_to_check = '`1234567890-=\][;#/,~!@$%^&*()_+{|":?><}"]'
        letters_to_check = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm'
        
        if any(char in user_input for char in characters_to_check):
            print('Please enter only letters or a period')
            continue
        elif "  " in user_input or user_input == " ":
            print("Please enter letters")
            continue
        break
        
    while True:
        menu()
        choice = input('Enter your choice (1-17): ')
        
        if choice == '1':
            print('Reversed:', reverse_array(user_input))
        elif choice == '2':
            total_vowels, vowels = count_vowels(user_input)
            print('Total Vowels:', total_vowels, '\nBreakdown: ', vowels)
        elif choice == '3':
            total_consonants, consonants = count_consonants(user_input)
            print('Total Consonants:', total_consonants, '\nBreakdown: ',consonants)
        elif choice == '4':
            print('First Name:', get_first_name(user_input))
        elif choice == '5':
            print('Last Name:', get_last_name(user_input))
        elif choice == '6':
            print('Middle Name(s):', get_middle_name(user_input))
        elif choice == '7':
            print('Last name contains hyphen:', last_name_has_hyphen(user_input))
        elif choice == '8':
            print('Lowercase:', to_lowercase(user_input))
        elif choice == '9':
            print('Uppercase:', to_uppercase(user_input))
        elif choice == '10':
            print('Randomized Name:', randomize_name(user_input))
        elif choice == '11':
            print('First name is palindrome:', is_first_name_palindrome(user_input))
        elif choice == '12':
            print('Sorted Name:', sorted_full_name(user_input))
        elif choice == '13':
            print('Initials:', get_initials(user_input))
        elif choice == '14':
            print('Contains title/distinction:', has_title(user_input))
        elif choice == '15':
            print('Censored Vowels:', censor_vowels(user_input))
        elif choice == '16':
            print('ASCII sum:', ascii_sum(user_input))
        elif choice == '17':
            print('Text in a pyramid:', print_pyramid(list(user_input)))
        else:
            print('Invalid choice! Please select a valid option.')
            continue
        while True:
            play_again = input('Do you want to play again? (yes/no): ')
            if play_again.lower() == 'yes':
                print('Okay!')
                main()
            elif play_again.lower() == 'no':
                print('Darn')
                sys.exit()
            else:
                print('Please enter yes or no')
main()


#make the name allow a hyphen
#only randomizes first name
#sorted name prints my name
#does not print true for if i put dr.
#works if you put a space for the name