def fibonacci(limit):
    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]
    
    # Generate Fibonacci numbers until reaching the limit
    while sequence[-1] + sequence[-2] <= limit:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

def main():
    # Prompt the user to enter a limit for the Fibonacci sequence
    limit = int(input("Enter the limit for the Fibonacci sequence: "))
    
    # Generate Fibonacci numbers up to the specified limit
    fib_sequence = fibonacci(limit)
    
    # Print the Fibonacci sequence
    print("Fibonacci sequence up to", limit, ":", fib_sequence)

if __name__ == "__main__":
    main()
print("Helllo Worlds@@@!!!!!!!")
