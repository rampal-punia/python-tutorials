print("Enter your age to know the ticket price.")
print("Enter 'quit' to end the program.")
print("=============================================")


while True:
    age = input("Enter your age: ")
    ticket_price = 100
    if age.lower() == "quit":
        break
    else:
        try:
            age = int(age)
            if age < 4:
                print(f"The ticket amount is ZERO.")
            elif 3 < age < 13:
                print(f"The ticket amount is {ticket_price/2}.")
            else:
                print(f"The ticket amount is {ticket_price}.")
        except:
            print("Sorry, I couldn't understand that.")
            print("Please try again!!!")
