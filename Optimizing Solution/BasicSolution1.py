def is_binary_string(s):
    # Check if the given string contains only 0s and 1s.
    for char in s:
        if char != '0' and char != '1':
            return False
    return True


def is_prime(n):
    # Check if a number is prime using a simple method.
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to the square root
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def find_prime_numbers_basic(binary_string, limit):
    # Check if the input is a valid binary string
    if not is_binary_string(binary_string):
        return []

    length = len(binary_string)
    primes = []

    # Generate all possible substrings
    for start in range(length):
        for end in range(start + 1, length + 1):
            substring = binary_string[start:end]

            # Convert binary to decimal (simple approach)
            decimal_value = 0
            for bit in substring:
                decimal_value = decimal_value * 2 + int(bit)

            # Check if it's prime and less than the limit
            if decimal_value < limit and is_prime(decimal_value):
                # Check if already in the list (simple linear search)
                if decimal_value not in primes:
                    primes.append(decimal_value)

    # Sort the primes
    primes.sort()

    return primes


def format_output(primes):
    # Format the output according to the requirements
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
    # Process the input string and return the formatted output.
    try:
        binary_string, limit_str = input_str.split(',')
        limit = int(limit_str)

        # Find the prime numbers
        primes = find_prime_numbers_basic(binary_string, limit)

        # Format and return the output
        return format_output(primes)

    except ValueError:
        return "0: Invalid input format. Please use the format 'binary_string,limit'"


def main():
    # Main function to process input and display output.
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

    # For very long strings, limit processing time to 60 seconds
    max_time = 60

    print("\nTesting with the 10 given test cases:")
    for i, test_case in enumerate(test_cases):
        print(f"Test case {i + 1}: {test_case}")
        start_time = time.time()

        try:
            # Set a timeout of 60 seconds
            result = process_input(test_case)
            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f"Result: {result}")
            print(f"Time taken: {elapsed_time:.6f} seconds")

            # Add to code comments
            print(f"# Test case {i + 1}: {test_case}")
            print(f"# Result: {result}")
            print(f"# Time: {elapsed_time:.6f} seconds")

            # Stop if we exceed the time limit
            if elapsed_time > max_time:
                print(f"Exceeded time limit of {max_time} seconds. Stopping.")
                break

        except Exception as e:
            print(f"Error processing test case: {str(e)}")
        print()


if __name__ == "__main__":
    main()