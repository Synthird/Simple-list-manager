listOfValues = [
    "Hello world",
    "yay",
    "A",
    "B",
    "g",
    ""
    ]

def findInList(value):
    if value in listOfValues:
        return True
    
def printResult(printValue):
    print(f">>>> {printValue} <<<<")

print("What do you want to do with this list of values?")

while True:
    print(listOfValues)
    print("--- INDIVIDUAL VALUES ---")
    print("1 = Add something to the list\n2 = Remove something from the list\n3 = Find something in"
        " the list\n4 = Get the index of a value")
    print("--- LIST ORDERING ---")
    print("5 = Organize the list\n6 = Reverse the order")
    print("--- OTHER ---")
    print("7 = Count how many values there are\n8 = Clear the entire list\nAny other integer = Exit"
        "this program")
    
    choice = int(input("I want to: "))

    if choice == 1:
        addition = input("Add: ")

        listOfValues.append(addition)
        printResult(f"{addition} has been added to the list!")
    elif choice == 2:
        removing = input("Remove: ")

        if findInList(removing):
            listOfValues.remove(removing)
            printResult(f"{removing} has been removed from the list!")
        else:
            printResult(f"Cannot remove {removing} since it it's not in the list...")
    elif choice == 3:
        finding = input("I want to find: ")

        if findInList(finding):
            printResult(f"Found {finding} in the list!")
        else:
            printResult(f"Cannot find {finding} in the list...")
    elif choice == 4:
        findValue = input("Find the index of ")

        if findInList(findValue):
            printResult(f"The index of {findValue} is {str(listOfValues.index(findValue))}")
        else:
            printResult(f"Cannot find the value of {findValue} since it's not in the list")
    elif choice == 5:
        printResult("The list is now organized!")
        listOfValues.sort()
    elif choice == 6:
        printResult("The list is now reversed!")
        listOfValues.reverse()
    elif choice == 7:
        listLength = len(listOfValues)
        printResult(f"There are a total of {str(listLength)} values in the list")
    elif choice == 8:
        listOfValues.clear()
        printResult("The entire list is cleared!")
    else:
        break