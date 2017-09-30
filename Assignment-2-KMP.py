# defines function "main"
def main():
    # performs an infinite loop in the function "splitter"
    while True:
        # calls function "splitter"
        splitter()
# defines function "splitter"
def splitter ():
    # prompts user for string input of their name
    name = input("Enter Your Name (Use '-' in Between Spaces): ")
    # split the names and input into lists
    splitnames = name.split("-")
    # loop as much times as there are numbers of names in the separated names list
    for i in range(0, len(splitnames)):
        # assign the respective index value to a temporary variable
        temp = splitnames[i]
        # prints the first letter of that value in uppercase
        print(temp[0].upper(), end="")
    # loops in new line
    print("")
# calls function "main"
main()
