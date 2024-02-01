#Trevor Nolan

#CS175L

#restaurant


vegitarian = input("Is anyone in your party vegitarian?(yes/no): ").lower()
vegan = input("Is anyone in your party vegan?(yes/no): ").lower()
gluten_free = input("is anyone in your party Gluten Free?(yes/no): ").lower()
print()
if vegitarian == "yes" and vegan == "yes" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
elif vegitarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
elif vegitarian == "yes" and vegan == "no" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company" +
          "\nMamas Fine Italian")
elif vegitarian == "no" and vegan == "no" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company" +
          "\nMamas Fine Italian" +
          "\nJoes Gourmet Burgers")
elif vegitarian == "no" and vegan == "no" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen" +
          "\nMain Street Pizza Company")

elif vegitarian == "no" and vegan == "yes" and gluten_free == "yes":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
elif vegitarian == "no" and vegan == "yes" and gluten_free == "no":
    print("here are your restaurant choices." +
          "\n"
          "\nCorner cafe" +
          "\nThe Chef's Kitchen")
