#Trevor Nolan

#CS175L

#restaurant


vegetarian = input("Is anyone in your party vegetarian?(yes/no): ").lower()
vegan = input("Is anyone in your party vegan?(yes/no): ").lower()
gluten_free = input("is anyone in your party Gluten Free?(yes/no): ").lower()
print()
if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
    
elif vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company" +
          "\nMamas Fine Italian")
elif vegetarian == "no" and vegan == "no" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company" +
          "\nMamas Fine Italian" +
          "\nJoes Gourmet Burgers")
elif vegetarian == "no" and vegan == "no" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company")

elif vegetarian == "no" and vegan == "yes" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")

elif vegetarian == "no" and vegan == "yes" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")

elif vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nMain Street Pizza Company" +
          "\nCorner Cafe" +
          "\nThe Chef's Kitchen")
