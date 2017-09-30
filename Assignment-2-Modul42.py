# defines function "main"
def main():
    # calls function "calcappend"
    calcappend()
# defines function "calcappend"
def calcappend():
    # prompts user for integer input
    times = int(input("How many numbers do you want to use? "))
    # created an empty list
    resultlist = []
    # loops as much times as the number of integers the user want to use
    for i in range(0, times):
        # prompts user for the number that will  be calculated
        num = int(input("Input Number: "))
        # runs the formula
        result = num % 42
        # move the result into the result list
        resultlist.append(result)
    # prints the number of unique characters in the list "resultlist"
    print(len(set(resultlist)), "Unique Characters")
# calls function "main"
main()
