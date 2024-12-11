def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    return sum(numbers) / len(numbers)

# Example usage:
my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")