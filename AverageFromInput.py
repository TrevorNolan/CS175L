def calculate_average(filename):
    total = 0
    count = 0
    
    # Open the file for reading
    file = open(filename, 'r')
    
    # Iterate over each line in the file
    for line in file:
        # Convert each line to a float and add it to the total
        current_number = float(line)
        total += current_number
        # Increment the count of numbers
        count += 1
        # Print current status
        print(f"I read in {count} number(s) Current number is: {current_number:8.2f} Total is: {total:8.2f}")

    # Close the file
    file.close()
    
    # Calculate the average
    if count > 0:
        average = total / count
        return average
    else:
        return 0  # If the file is empty, return 0 as the average

# File name
filename = "numbers.txt"

# Calculate and print the average
average = calculate_average(filename)
print("Average of numbers in the file:", average)
