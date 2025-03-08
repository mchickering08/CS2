def emails():
    email_counts = {}                                                                   #Dictionary to store email addresses and their counts
    with open("mbox-long.txt") as file:
        for line in file:                                                               #For every line in the file
            if line.startswith("From:"):                                                #If line starts with "From"
                email = line.split()[1]                                                 #Extract email address from the line
                email_counts[email] = email_counts.get(email, 0) + 1                    #Increment count
    count_list = [(count, email) for email, count in email_counts.items()]              #Create a list of tuples (count, email)
    count_list.sort(reverse=True)                                                       #Sort the list in reverse order based on count
    print(count_list[0])                                                                #Print the person with the most commits

def sort_by_day():
    hcount = dict()                                                                     #Create empty dictionary
    times = []                                                                          #Create empty list
    with open("mbox-long.txt") as file:
        for line in file: 
            words = line.split()
            if len(words) > 2 and words[0] == 'From':                                   #Select lines with 'From'
                hr = words[5].split(':')                                                #Select hour (5th index) and split string with colon
                hcount[hr[0]] = hcount.get(hr[0], 0) + 1                                #Increase count for each hour
            else:
                continue
        for k,v in hcount.items():                                                      #K = hour, v = count
            times.append((k,v))                                                         #Append tuples to list
        times.sort()                                                                    #Sort list by hour
        for k,v in times:                                                               #Loop through list of tuples
            print(k,v)                                                                  #Print counts sorted by hour

def letter_frequency():
    letter_counts = {}
    with open("mbox-long.txt", 'r') as file:
        text = file.read().lower()                                                      #Convert to lowercase
        for char in text:
            if char.isalpha():                                                          #Only count letters
                letter_counts[char] = letter_counts.get(char, 0) + 1 
    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True) #Sort by frequency in descending order
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")


emails()
sort_by_day()
letter_frequency()