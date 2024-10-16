listOfValues = [
    "Hello world",
    "yay",
    "BAAAAA!!",
    "Comfy",
    "MOOoooo..",
    "WOW!",
    "Paper",
    "Item"
]


def findInList(value):
    if value in listOfValues:
        return True


def printResult(printValue):
    print(f">>>> {printValue} <<<<")


def printHeading(printValue):
    print(f"--- {printValue} ---")


print("What do you want to do with this list of values?")

while True:
    print(listOfValues)
    printHeading("INDIVIDUAL VALUES")
    print("1 = Add something to the list")
    print("2 = Remove something from the list")
    print("3 = Find something in the list")
    print("4 = Get the index of a value in the list")
    printHeading("LIST ORDERING")
    print("5 = Organize the list")
    print("6 = Reverse the order")
    printHeading("OTHER")
    print("7 = Count how many values there are")
    print("8 = Clear the entire list")
    print("Any other integer = Exit this program")

    choice = int(input("I want to: "))

    if choice == 1:
        addition = input("I want to add: ")

        listOfValues.append(addition)
        printResult(f"{addition} has been added to the list!")
    elif choice == 2:
        removing = input("I want to remove: ")

        if findInList(removing):
            listOfValues.remove(removing)
            printResult(f"{removing} has been removed from the list!")
        else:
            printResult(f"Cannot remove {
                        removing} since it's not in the list...")
    elif choice == 3:
        finding = input("I want to find: ")

        if findInList(finding):
            printResult(f"Found {finding} in the list!")
        else:
            printResult(f"Cannot find {finding} in the list...")
    elif choice == 4:
        findValue = input("Find the index of ")

        if findInList(findValue):
            printResult(f"The index of {findValue} is {
                        str(listOfValues.index(findValue))}")
        else:
            printResult(f"Cannot find the index of {
                        findValue} since it's not in the list")
    elif choice == 5:
        printResult("The list is now organized!")
        listOfValues.sort()
    elif choice == 6:
        printResult("The order of the list has been reversed!")
        listOfValues.reverse()
    elif choice == 7:
        printResult(f"There are a total of {
                    str(len(listOfValues))} values in the list")
    elif choice == 8:
        listOfValues.clear()
        printResult("The entire list is now cleared!")
    else:
        break
