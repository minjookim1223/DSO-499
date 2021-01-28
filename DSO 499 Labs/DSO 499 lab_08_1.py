# This program could be the foundation to organize a list of cars using dictionary
# Could be used primarily by automobile industry


def main():

    carDict = {}  # dictionary to contain all brands and model
    car = ""
    model = ""
    cont = "y"

    while cont == "y":
        brand = input("What is the brand that you want to enter?: ")
        model = input("What is the model name?: ")
        carDict[brand] = model

        cont = input("Would you like to continue? y/n: ")
        if cont != "y" and cont != "n":
            print("You have submitted wrong input.")
            print("The system will now quit.")

    print("\nHere is the list of cars that you have:")
    print(carDict)


main()
