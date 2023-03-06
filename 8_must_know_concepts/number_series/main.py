import helper

while True:
    print("==============================================")
    print("Select from the series to print.")
    print("Pattern 1. Square numbers.")
    print("Pattern 2. Add square number to the previous number.")
    print("Pattern 3. Cube numbers.")
    print("Pattern 4. Add Squares plus one to previous number.")
    print("Pattern 5. Add Cube plus one to previous number.")
    print("==============================================")

    pattern_option = int(input("Enter the option number: "))
    num_element = int(input("Required elements in the pattern: "))

    if pattern_option == 1:
        pattern_list = helper.square_pattern(num_element)
        print(pattern_list)

    elif pattern_option == 2:
        pattern_list = helper.add_square_pattern(num_element)
        print(pattern_list)

    elif pattern_option == 3:
        pattern_list = helper.cube_pattern(num_element)
        print(pattern_list)

    elif pattern_option == 4:
        pattern_list = helper.square_plus_one_pattern(num_element)
        print(pattern_list)

    elif pattern_option == 5:
        pattern_list = helper.cube_plus_one_pattern(num_element)
        print(pattern_list)

    # To come out of the while loop
    is_continue = input("Do you want to continue?(yes/no): ")

    # YES, yES, Yes
    if is_continue.lower() == 'yes':
        continue

    elif is_continue.lower() == 'no':
        break

    else:
        print("***********************************")
        print("Sorry I couldn't understand that.")
        print("***********************************")
        continue
