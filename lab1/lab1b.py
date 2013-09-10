# lab1b.py
# @author Felix Ekdahl
# Student-ID: felno295
# Assignment 1B from: http://www.ida.liu.se/~TDDC66/python/la/la1.shtml

def reformat(list):
    newList = [] # Initialize an empty array for iteration.
    for i in range (0, len(list)): # Prepare an for-loop for complete iteration over the argument in the parameters.
        newList.append(eval(list[i])) # Append the newList with parsed strings. (String -> Integers)
    return newList; # Return the freshly stripped list.
        

def mult_pnr(list):
    returnArray = list # Init an empty array
    for i in range(0, len(list), 2): # Iterate over that array
        list[i]*=2 # Multiply every second number by 2
    return returnArray # Return it.

def normalize_array(list):
    newList = [] # Init an empty array
    for i in range(0, len(list)): # Iterate..
        if list[i] > 10:  # If it's higher than 10, we need to split it to 2 numbers as shown below
            newList.append(list[i]//10) 
            newList.append(list[i]%10)
            continue
        elif list[i] == 10:
            newList.append(1)
            continue
        else:
            newList.append(list[i]) # Else we can just add it to the array
    return newList

def sum_numbers(list):
    summation = 0
    for i in range(0, len(list)):
        summation += list[i] # Sum the numbers in the array together
    return summation

def identify(sum):
    foo = (((sum//10)+1)*10) - sum # Get the difference.
    return foo

def main():
    lastNumber = -1
    while True: # Simple bullshit to prevent nullpointers later in the code.
        x = list(input("Enter your personal number: "))
        if len(x) != 10:
            print ("You must supply a 10-number digit.")
        else:
            break
    x = reformat(x)
    lastNumber = x[9] # Pop the last object of the array after adding it to the comparison variable.
    x.pop(len(x)-1) # Remove the last element of the array.
    x = mult_pnr(x) # Multiply all the elements in the array
    x = normalize_array(x) # Split all numbers higher than 10 
    summa = sum_numbers(x) # Sum the numbers
    finalRes = identify(summa) # Get the final result of the computation
    if finalRes == lastNumber: # Check if it's valid!
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
