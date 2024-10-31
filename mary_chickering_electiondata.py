""""
┌───────────────────────────────────────────────────────────────────────────┐
│                              Election Data                                │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: N/N                                                                 │
│ Description: User enters a file name then top 10 words and their amounts  |
| used are returned and excel spreadsheet is made with csv for words written|
| more than five times                                                      |
└───────────────────────────────────────────────────────────────────────────┘
"""
import csv                                                                                   #imports csv library

def punctuation(line):
    """
    Removes the puncuation from a line

    Args:
        line of text (str): The user's desired line of text

    Returns:
        str: The user's desired line of text but removed of all the punctuation described

    """
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''                                          #all the different types of punctuation that will be removed
    for x in line.lower():                                                                   #creates a for loop for the characters in the line
        if x in punctuations:                                                                #if a character from the line is listed in the punctuations, complete the following
            line = line.replace(x, "")                                                       #replace the character with nothing/remove it
    return line                                                                              #return the line

fname = input('Enter the file name: ')                                                       #fname value is equal to the user's imput to the queston "Enter the file name"
try:                                                                                         #attempts the following code to test if the file can be opened
    fhand = open(fname)                                                                      #creates a value to open the file
except:                                                                                      #unless
    print('File cannot be opened:', fname)                                                   #print "file cannot be opened: name of file inserted"
    exit()                                                                                   #terminate the running system

counts = dict()                                                                              #value for counts is dict
for line in fhand:                                                                           #for every line in the file
    line = line.lower()                                                                      #convert the line to all lowercase
    line = punctuation(line)                                                                 #removes punctuation from the line
    words = line.split()                                                                     #splits line by words
    for word in words:                                                                       #for every word in the line
        if word in ("the", "and", "to", "of", "i", "a", "in", "for", "than", "our", "we", "that", "am", "is", "he", "us", "who", "my", "will", "so", "up", "with", "are", "be", "as", "she", "not", "on", "us", "you", "an", "when", "has", "have", "was", "but", "one", "would", "all", "their", "this", "they", "his", "about", "me", "know", "at", "us", "let", "by", "because", "out", "what", "your", "going", "from", "it", "like", "were", "where", "us"): #if words from speech are listed, do the following
            continue                                                                         #skip over the word
        if word not in counts:                                                               #if the word is not in counts value
            counts[word] = 1                                                                 #value of wordcount stays the same
        else:                                                                                #if the word is in the counts value
            counts[word] += 1                                                                #add that word to the wordcount of counts

sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))           #sorted dictionary is the dictionary sorted by the words with the highest values to the least values
K = 10                                                                                       #creates value for K
limited_dict = dict(list(sorted_dict.items())[0: K])                                         #limits the variable to only 10 items
final = (str(limited_dict))                                                                  #converts the limited dictionary into a string
print(final)                                                                                 #prints the final limited dictionary

fieldnames = ["Word", "Amount"]                                                              #list of the two fieldnames 
with open('presidentspeeches.csv', 'w', newline='') as csv_file:                             #open the presidentspeeches csv file, and creates a new line for every speech
    writer = csv.writer(csv_file)                                                            #write data directly into the csv file
    writer.writerow(fieldnames)                                                              #write rows for the two field names
    counter = 0                                                                              #sets the starting counter as zero
    for key, value in sorted_dict.items():                                                   #for every key and value in the sorted dictionary
        if value >= 5:                                                                       #if the value is greater than or equal to 5
            writer.writerow([key, value])                                                    #write a row the key and value in different columns divided by the comma
            counter = counter + 1                                                            #add one to the counter
            if counter == 10:                                                                #if the counter reaches 10
                break                                                                        #end the loop