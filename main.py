def process_list(input_list):
    # Check if the length of the input list is a multiple of 10
    if len(input_list) % 10 != 0:
        print("Error: The length of the list must be a multiple of 10.")
        return

    # Remove items at positions which are a multiple of 2 or 3
    result_list = [num for idx, num in enumerate(input_list) if (idx + 1) % 2 != 0 and (idx + 1) % 3 != 0]

    return result_list

# Example usage
try:
    input_list = list(map(int, input("Enter a list of integers separated by space: ").split()))
    result = process_list(input_list)
    if result is not None:
        print("Processed List:", result)
except ValueError:
    print("Error: Please enter a valid list of integers.")
