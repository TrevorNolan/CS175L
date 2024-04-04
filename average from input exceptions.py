def calculate_average(filename):
    total = 0
    count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    current_number = float(line)
                    total += current_number
                    count += 1
                    print(f"I read in {count} number(s). Current number is: {current_number:8.2f}. Total is: {total:8.2f}")
                except ValueError:
                    print(f"Error: Could not convert '{line.strip()}' to a number.")
    except IOError:
        print("Error: Unable to open or read the file.")
        return 0

    if count > 0:
        average = total / count
        return average
    else:
        return 0  

filename = "numbers.txt"
average = calculate_average(filename)
print("Average of numbers in the file:", average)
