def print_x(size):
    # Validate the input size
    if size < 3 or size % 2 == 0:
        print("Please enter an odd number greater than or equal to 3.")
        return

    for i in range(size):
        for j in range(size):
            # Print * for the diagonal conditions
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print() 

if __name__ == "__main__":
    try:
        # Take user input
        n = int(input("Enter the size of the 'X' (odd number >= 3): "))
        print_x(n)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
