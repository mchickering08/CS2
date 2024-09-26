""""
┌───────────────────────────────────────────────────────────────────────────┐
│                               GCDS PostOffice                             │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: If user enters decimal as zip code, it will round                   │
│ Description: User enters their package dimensions and zip code then code  |
| produces total cost of mail                                               │
└───────────────────────────────────────────────────────────────────────────┘
"""
def get_postcard(height, length, thickness): 
    """
    Defines the postcard function with height, length, and thickeness as variables

    Args:
        height, length, thickness (int): The user package's height, length, and thickness

    Returns:
        str: The package type

    """
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:      #conditional statement for if the length is in between 3.5-4.25, the height in between 3.5-6, and thickness in between .007 and 0.16
        return "Regular Postcard"                                                       #returns type as regular postcard
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and .007 <= thickness <= .015:     #conditional statement for if the length is in between 4.25-6, the height in between 6-11.5, and thickness in between .007 and 0.15
        return "Large Postcard"                                                         #returns type as large postcard
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 <= thickness <= .25:   #conditional statement for if the length is in between 3.5-6.125, the height in between 5-11.5, and thickness in between .007 and 0.15
        return "Regular Envelope"                                                       #returns type as regular envelope
    elif 6.125 < length < 24 and 11 <= height <= 18 and .25 <= thickness <= .5:         #conditional statement for if the length is in between 6.125-24, the height in between 11-18, and thickness in between .25-.5
        return "Large Envelope"                                                         #returns type as large envelope
    elif length + (height + thickness)*2 <= 84:                                         #conditional statement for if the length, height, and thickness multiplied by two is less than 84
        return "Package"                                                                #returns type as package
    elif 84 <= length + (height + thickness)*2 <= 130:                                  #conditional statement for if the length, height, and thickness multiplied by two is more than 84 and less than 130
        return "Large Package"                                                          #returns type as large package
    else:                                                                               #conditional statement for if none of the other conditions apply
        return "Unmailable"                                                             #return type as unmailable
    
def get_zone(zip):     
    """
    Returns the zip code zone with the user's given zipcodes

    Args:
        zip (int): The user's zipcode

    Returns:
        int: zone number

    """                                                         
    if 1 <= zip <= 6999:                                                               #conditional statement for if the zip is between 1 and 6999
        return 1                                                                       #returns type as zone 1
    elif 7000 <= zip <= 19999:                                                         #conditional statement for if the zip is between 7000 and 19999
        return 2                                                                       #returns type as zone 2
    elif 20000 <= zip <= 35999:                                                        #conditional statement for if the zip is between 20000 and 35999
        return 3                                                                       #returns type as zone 3
    elif 36000 <= zip <= 62999:                                                        #conditional statement for if the zip is between 36000 and 62999
        return 4                                                                       #returns type as zone 4
    elif 63000 <= zip <= 84999:                                                        #conditional statement for if the zip is between 63000 and 84999
        return 5                                                                       #returns type as zone 5
    elif 85000 <= zip <= 99999:                                                        #conditional statement for if the zip is between 85000 and 99999
        return 6                                                                       #returns type as zone 6
    
def get_costs(postage_type, zones):     
    """
    Returns the cost based on the postcard and zones

    Args:
        postage type (str), zones (int): User's postage type and postal zone

    Returns:
        int: final cost

    """                                         
    if postage_type == "Regular Postcard":                                             #conditional statement for if the postage type equals "regular postcard"
        return .20 + .03*zones                                                         #returns total cost by adding .20 then adding .03 multiplied by the number of zones
    elif postage_type == "Large Postcard":                                             #conditional statement for if the postage type equals "large postcard"
        return .37 + .03*zones                                                         #returns total cost by adding .37 then adding .03 multiplied by the number of zones
    elif postage_type == "Regular Envelope":                                           #conditional statement for if the postage type equals "regular envelope"
        return .37 + .04*zones                                                         #returns total cost by adding .37 then adding .04 multiplied by the number of zones
    elif postage_type == "Large Envelope":                                             #conditional statement for if the postage type equals "large envelope"
        return .60 + .05*zones                                                         #returns total cost by adding .60 then adding .05 multiplied by the number of zones
    elif postage_type == "Package":                                                    #conditional statement for if the postage type equals "package"
        return 2.95 + .25*zones                                                        #returns total cost by adding .2.95 then adding .25 multiplied by the number of zones
    elif postage_type == "Large Package":                                              #conditional statement for if the postage type equals "large package"
        return 3.95 + .35*zones                                                        #returns total cost by adding .3.95 then adding .25 multiplied by the number of zones
    

def main():    
    """
    Runs all the functions together to produce total cost

    Args:
        none

    Prints:
        int: final cost

    """
    while True:                                                                        #defines main function
        dimensions = input("enter l, h, t, zip1, zip2: ").split(",")                   #asks the user to enter the length, height, thickness, zip1, and zip2 and splits up the variables by a comma
        if len(dimensions) != 5:                                                       #if the length of the list does not equal 5
            print("Please enter 5 input numbers")                                      #asks the user to input a valid number
        else:                                                                          #contitonal else statement
            try:                                                                       #attempts the following code to check for errors in user input
                height = float(dimensions[0])                                          #length a float, and the first term in dimensions
                length = float(dimensions[1])                                          #height is a float, and the second term in dimensions
                thickness = float(dimensions[2])                                       #thickness is a float, and the third term in dimensions
                zip1 = int(dimensions[3])                                              #zip1 is an integer, and the fourth term in dimensions
                zip2 = int(dimensions[4])                                              #zip2 is an integer, and the fifth term in dimensions
                postage_type = get_postcard(length, height, thickness)                 #length, height, thickness are plugged into get_postcard function and returned as postage_type
                
                if postage_type == "Unmailable":                                       #conditional statement for if the postage_type is returned as "Unmailable"
                        print("Unmailable")                                            #print "unmailable"
                        continue                                                       #goes to top of the while true loop
                
                zones = abs(get_zone(zip1)-get_zone(zip2))                             #zones is the absolute value of zip1's zone minus zip2's zone
                total_cost = (get_costs(postage_type, zones))                          #postage_type and zones are plugged into get_costs function to get total cost
                formatted_cost = str(total_cost).lstrip("0")                           #formatted cost is the total cost but as a string and the zero before the decimal point is stripped
                print(formatted_cost)                                                  #prints the formatted cost
                break                                                                  #breaks the while true loop
            except ValueError:                                                         #if valueerror occurs
                print("Dummy you put the wrong data type")                             #asks user to enter the write data type                                     #breaks the while true loop
main()                                                                                 #runs the main function                                                                       