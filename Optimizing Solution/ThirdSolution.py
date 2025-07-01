def is_binary_string(s):
    """Check if the given string contains only 0s and 1s."""
    return all(c in '01' for c in s)


def is_prime(n):
    """Check if a number is prime using an optimized trial division method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors of form 6k±1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def find_prime_numbers_optimized(binary_string, limit):
    """
    Find all unique prime numbers hidden in the binary string that are less than the limit.
    Optimized implementation using more efficient methods.

    Args:
        binary_string (str): The binary string to search in
        limit (int): The upper limit for prime numbers

    Returns:
        list: Sorted list of unique prime numbers found
    """
    # Check if the input is a valid binary string
    if not is_binary_string(binary_string):
        return []

    # Use a set for O(1) lookup and to automatically handle duplicates
    result_primes = set()
    length = len(binary_string)

    # Process substrings more efficiently
    for start in range(length):
        # Skip substrings starting with '0' unless it's the only character
        if binary_string[start] == '0' and start < length - 1:
            # Only consider '0' by itself
            if is_prime(0) and 0 < limit:
                result_primes.add(0)
            continue

        # Build the decimal value incrementally for efficiency
        value = 0
        for end in range(start, length):
            # Shift left and add new bit (much faster than recreating substrings)
            value = (value << 1) | int(binary_string[end])

            # Skip if value exceeds our limit
            if value >= limit:
                break

            # Check if this value is prime
            if is_prime(value):
                result_primes.add(value)

    # Return sorted list of primes
    return sorted(result_primes)


def format_output(primes):
    """Format the output according to the requirements."""
    if not primes:
        return "0: Invalid binary strings"

    count = len(primes)

    if count < 6:
        # Show all primes if fewer than 6
        result = f"{count}: {', '.join(map(str, primes))}"
    else:
        # Show just the 3 smallest and 3 largest
        smallest = primes[:3]
        largest = primes[-3:]
        result = f"{count}: {', '.join(map(str, smallest))}, ..., {', '.join(map(str, largest))}"

    return result


def process_input(input_str):
    """Process the input string and return the formatted output."""
    try:
        binary_string, limit_str = input_str.split(',')
        limit = int(limit_str)

        # Find the prime numbers
        primes = find_prime_numbers_optimized(binary_string, limit)

        # Format and return the output
        return format_output(primes)

    except ValueError:
        return "0: Invalid input format. Please use the format 'binary_string,limit'"


def main():
    """Main function to process input and display output."""
    import time

    # Test with examples from the coursework
    examples = [
        "101011,99",
        "0110,5",
        "COMP,4",
    ]

    print("Testing with basic examples:")
    for i, example in enumerate(examples):
        print(f"Example {i + 1}: {example}")
        start_time = time.time()
        result = process_input(example)
        end_time = time.time()
        print(f"Result: {result}")
        print(f"Time taken: {(end_time - start_time) * 1000:.6f} ms")
        print()

    # Test with the 10 given test cases
    test_cases = [
        "0100001101001111,999999",  # Test case 1: 'CO'
        "01000011010011110100110101010000,999999",  # Test case 2: 'COMP'
        "1111111111111111111111111111111111111111,999999",  # Test case 3: 40 1's
        "0100001101001111010011010101000000110001001110000,999999999",  # Test case 4: 'COMP18'
        "010000110100111101001101010100000011000100111000001100001,123456789012",  # Test case 5: 'COMP181'
        "01000011010011110100110101010000001100010011100000110001001110010,123456789012345",  # Test case 6: 'COMP1819'
        "0100001101001111010011010101000000110001001110000011000100111001001000001,123456789012345678",
        # Test case 7: 'COMP1819!'
        "01000011010011110100110101010000001100010011100000110001001110010010000101000001,1234567890123456789",
        # Test case 8: 'COMP1819!A'
        "0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100,1234567890123456789",
        # Test case 9: 'COMP1819!AD'
        "010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011,12345678901234567890"
        # Test case 10: 'COMP1819!ADS'
    ]

    print("\nTesting with the 10 given test cases:")
    for i, test_case in enumerate(test_cases):
        print(f"Test case {i + 1}: {test_case}")
        start_time = time.time()

        try:
            # Set a timeout of 60 seconds (handled externally)
            result = process_input(test_case)
            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f"Result: {result}")
            print(f"Time taken: {elapsed_time:.6f} seconds")

            # Add to code comments
            print(f"# Test case {i + 1}: {test_case}")
            print(f"# Result: {result}")
            print(f"# Time: {elapsed_time:.6f} seconds")

            # Stop if we exceed 60 seconds
            if elapsed_time > 60:
                print(f"Exceeded time limit of 60 seconds. Stopping.")
                break

        except Exception as e:
            print(f"Error processing test case: {str(e)}")
        print()


if __name__ == "__main__":
    main()