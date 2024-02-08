#Trevor Nolan

#CS175L

#restaurant

while True:
    vegetarian = input("Is anyone in your party vegetarian?(yes/no): ").lower()
    vegan = input("Is anyone in your party vegan?(yes/no): ").lower()
    gluten_free = input("Is anyone in your party Gluten Free?(yes/no): ").lower()
    print()

    if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen")

    elif vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen")

    elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen" +
              "\nMain Street Pizza Company" +
              "\nMama's Fine Italian")

    elif vegetarian == "no" and vegan == "no" and gluten_free == "no":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen" +
              "\nMain Street Pizza Company" +
              "\nMama's Fine Italian" +
              "\nJoe's Gourmet Burgers")

    elif vegetarian == "no" and vegan == "no" and gluten_free == "yes":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen" +
              "\nMain Street Pizza Company")

    elif vegetarian == "no" and vegan == "yes" and gluten_free == "yes":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen")

    elif vegetarian == "no" and vegan == "yes" and gluten_free == "no":
        print("Here are your restaurant choices:" +
              "\n"
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen")

    elif vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
        print("Here are your restaurant choices:" +
              "\n"
              "\nMain Street Pizza Company" +
              "\nCorner Cafe" +
              "\nThe Chef's Kitchen")

    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

    print()
    choice = input("Would you like to search again? (yes/no): ").lower()
    print()
    if choice != "yes":
        break
    
