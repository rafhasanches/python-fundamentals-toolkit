n1 = int(input("Please enter your first number: "))
n2 = int(input("Please enter your second number: "))
choice = 0

while choice != 5:
    choice = int(input(
        "Please enter your choice\n1 for sum\n2 for multiplication\n3 for greater\n4 for new numbers\n5 Leave Program\n"))
    if choice == 1:
        sum = n1 + n2
        print("The sum is", sum)
    elif choice == 2:
        multiplication = n1 * n2
        print("The multiplication is", multiplication)
    elif choice == 3:
        if n1 > n2:
            print('{} is the greater than {}'.format(n1, n2))
        elif n1 < n2:
            print('{} is the greater than {}'.format(n2, n1))
        else:
            print('The numbers are equal')
    elif choice == 4:
        n1 = int(input("Please enter your NEW first number: "))
        n2 = int(input("Please enter your NEW second number: "))
    elif choice == 5:
        print("Thank you for using this program")
    else:
        print("Please enter a valid choice")
