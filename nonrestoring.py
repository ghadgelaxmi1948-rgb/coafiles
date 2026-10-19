def non_restoring_division(dividend, divisor, n=4):
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

        # Interpret A as signed 2's-complement
        if A & (1 << (n - 1)):
            A = A - (1 << n)

        print(f"\nStep {i + 1}: After left shift")
        print(f"A  = {A:0{n}b}")
        print(f"Q  = {Q:0{n}b}")
        print(f"Q0 = {Q & 1}")

        # Non-restoring operation
        if A >= 0:
            A = A - M
            operation = "A = A - M"
        else:
            A = A + M
            operation = "A = A + M"

        # Set Q0 based on the sign of A
        if A >= 0:
            Q = Q | 1
        else:
            Q = Q & ~1

        print(f"\nStep {i + 1}: {operation}")
        print(f"A  = {A if A >= 0 else (A + (1 << n)):0{n}b}")
        print(f"Q  = {Q:0{n}b}")
        print(f"Q0 = {Q & 1}")

    # Final correction
    if A < 0:
        A = A + M

    print("\nFinal result:")
    print(f"Quotient  = {Q}")
    print(f"Remainder = {A}")


dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

non_restoring_division(dividend, divisor)