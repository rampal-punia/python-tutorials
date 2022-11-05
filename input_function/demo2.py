print("=====Display A Number's Table=====")
print("Print table for a number.")
print("===================================")


def get_number_table(number):
    for count in range(1, 11):
        print(f"{number} X {count} = {count*number}")


def run():
    text = input("Enter a number: ")
    try:
        number = int(text)
    except Exception as ex:
        print(ex)
        print("Not a number!")
        return
    get_number_table(number)


option = "y"

while option == "y":
    run()
    option = (input("Run again?(y/n): ")).lower()
