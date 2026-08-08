list1 = []
list2= []

first = input("Enter two decimals values separated by a space (or type -1.0 to stop):")

while first.strip() != '-1.0':
    split_first = first.split()
    if len(split_first) == 2:
        wind = float(split_first[0])
        rain = float(split_first[1])
        list1.append(wind)
        list2.append(rain)
    else:
        print("Invalid input. Please enter exactly two decimal values separated by a space.")

    first = input("Enter two decimals values separated by a space (or type -1.0 to stop):")

average1 = sum(list1) / len(list1)
print("The average rain is: {:.1f}".format(average1), "inches")

average2 = sum(list2) / len(list2)
print("The average wind is:", average2, "mph")

wheatersev = (average1 * 10) + average2
print("The wheater severity for these", len(list1), "readings is:",wheatersev)
