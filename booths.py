def booth(m, q, n=5):
    minimum = -(1 << (n - 1))
    maximum = (1 << (n - 1)) - 1

    if not (minimum <= m <= maximum and minimum <= q <= maximum):
        print(f"Enter numbers between {minimum} and {maximum}.")
        return

    mask = (1 << n) - 1
    A = 0
    M = m & mask
    Q = q & mask
    Q1 = 0

    print("Initial:")
    print(f"A = {A:0{n}b}")
    print(f"Q = {Q:0{n}b}")
    print(f"Q1 = {Q1}")

    for i in range(n):
        Q0 = Q & 1

        if Q0 == 0 and Q1 == 1:
            A = (A + M) & mask
        elif Q0 == 1 and Q1 == 0:
            A = (A - M) & mask

        combined = (A << (n + 1)) | (Q << 1) | Q1
        sign = A & (1 << (n - 1))
        combined >>= 1

        if sign:
            combined |= 1 << (2 * n)

        A = (combined >> (n + 1)) & mask
        Q = (combined >> 1) & mask
        Q1 = combined & 1

        print(f"\nStep {i + 1}:")
        print(f"A = {A:0{n}b}")
        print(f"Q = {Q:0{n}b}")
        print(f"Q-1 = {Q1}")

    product = (A << n) | Q
    if product & (1 << (2 * n - 1)):
        product -= 1 << (2 * n)

    print(f"Product = {product}")


m = int(input("Enter the multiplicand (m): "))
q = int(input("Enter the multiplier (q): "))

booth(m, q, n=5)