def restoring_division(dividend, divisor, n=4):
    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    if dividend < 0 or divisor < 0 or dividend >= (1 << n) or divisor >= (1 << n):
        print(f"Enter numbers between 0 and {(1 << n) - 1}.")
        return

    A = 0
    Q = dividend
    M = divisor
    mask = (1 << n) - 1

    print("Initial:")
    print(f"A  = {A:0{n}b}")
    print(f"Q  = {Q:0{n}b}")
    print(f"Q0 = {Q & 1}")
    print(f"M  = {M:0{n}b}")

    for i in range(n):
        # Left shift A and Q together
        combined = (A << n) | Q
        combined = (combined << 1) & ((1 << (2 * n)) - 1)

        A = (combined >> n) & mask
        Q = combined & mask

        print(f"\nStep {i + 1}: After left shift")
        print(f"A  = {A:0{n}b}")
        print(f"Q  = {Q:0{n}b}")
        print(f"Q0 = {Q & 1}")

        # Subtract divisor
        A = A - M

        if A < 0:
            A = A + M       # Restore A
            Q = Q & ~1      # Set Q0 = 0
            result = "Negative: Restore A, Q0 = 0"
        else:
            Q = Q | 1       # Set Q0 = 1
            result = "Non-negative: Q0 = 1"

        print(f"\nStep {i + 1}: After subtraction/restoration")
        print(result)
        print(f"A  = {A:0{n}b}")
        print(f"Q  = {Q:0{n}b}")
        print(f"Q0 = {Q & 1}")

    print(f"\nQuotient  = {Q}")
    print(f"Remainder = {A}")


dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

restoring_division(dividend, divisor)