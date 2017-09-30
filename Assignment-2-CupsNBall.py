# defines function "name"
def main():
    # calls function "temorarytrashbin"
    temporarytrashbin()
# defines function "temporarytrashbin"
def temporarytrashbin ():
    # declares a preset list of starting point
    cups = [1, 0, 0]
    # prints the original unmixed list
    print(cups)
    # prompts user for string input to declare moves
    pick = input("Pick Moves A/B/C: ")
    # loops as much times as there are number of moves
    for i in range(0, len(pick)):
        # checks if the input is letter A, and do the action respective to each of them
        if pick[i] == "A":
            temp = cups[0]
            cups[0] = cups[1]
            cups[1] = temp
        # checks if the input is letter B, and do the action respective to each of them
        if pick[i] == "B":
            temp = cups[1]
            cups[1] = cups[2]
            cups[2] = temp
        # checks if the input is letter C, and do the action respective to each of them
        if pick[i] == "C":
            temp = cups[0]
            cups[0] = cups[2]
            cups[2] = temp
    # calls the function "final" with argument variable "cups"
    final(cups)
# defines function "final" with argument "cups"
def final(cups):
    if cups[0] == 1:
        print(1)
    if cups[1] == 1:
        print(2)
    if cups[2] == 1:
        print(3)
# calls function "main"
main()
