import math


def main():
    print(display_title())
    print("Base delivery for a 1 lb package is $7.95 for a 2 hour or less delivery.  Add "
          "$2 for a 1 hour or less delivery. ")

    valid = False
    while not valid:
        time = input("Enter 2 for 2 hour or less or a 1 for 1 hour or less: ")
        try:
            time = int(time)
        except ValueError:
            print("Please enter a numeric value.")
            continue
        except Exception as e:
            print("Please enter a numeric value.")
            continue

        if time == 1 or time == 2:
            valid = True
        else:
            print(" ")

    valid = False
    while not valid:
        weight = input("Enter weight of package in POUNDS ONLY PLEASE! $1 per pound"
                       "starting at 2 lbs up to 50 lbs: ")
        try:
            weight = float(weight)
        except ValueError:
            print("Please enter a numeric value.")
            continue
        except Exception as e:
            print("Please enter a numeric value.")
            continue

        if weight > 50 or weight < 0:
            print("Please enter a weight between 0 and 50")
            print(" ")
        else:
            valid = True

    print("Total delivery price for package: " + get_delivery_price(weight, time))
    print(" ")

    valid = False
    while not valid:
        var = input("Continue (y/n)? ")
        var = var.lower()

        if var == "y":
            main()
        elif var == "n":
            print("Bye")
            valid = True
        else:
            continue


def display_title():
    title = "\nISQA 4900 Metro Courier Service Delivery Calculator!"
    return title


def get_delivery_price(weight, time):

    if weight < 2:
        price = 7.95
    else:
        price = 7.95 + math.ceil(weight-2)

    if time == 1:
        price += 2.00

    return str(price)


main()
