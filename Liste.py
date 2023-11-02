def inputFunction():    # Create a Function
    nameList = []       # Create empty list outside of loop, so it wont reset during looping
    while True:         # Infinite Bool loop
        name = input("Enter Name: ") 
        if name == '':      # if input Empty returns 'nameList' t other function
            return nameList
        elif name.lower() == "e":
            print("Shut Down")
            exit()
        else:
            nameList.append(name)   # Adds name to the nameList
            print(nameList)     # Checks that Append works

def listFunction():     # Create another function
    nestedList = []     # Creates an empty list that will never be wiped during execution
    while True:         # Another infinite loop
        nameList = inputFunction()  # Fetches the nameList from other Function by calling it
        nestedList.append(nameList) # Add list into an empty list, creating a nested List (List within a list)
        print("Length", len(nestedList)) # We see Nested list length
        print(nestedList)   # Print the entire Nested List
        print(len(nestedList[0]))   # we see that index[0] len is the amount of elements inside
        print(nestedList[0][1]) # Fetch the first index second element
listFunction() # Calls the Function