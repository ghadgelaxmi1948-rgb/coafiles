print("Memory Hierarchy Analysis")

levels = int(input("Enter number of memory levels (2 or 3): "))

if levels not in (2, 3):
    print("Invalid choice! Select 2 or 3 levels.")

else:
    size = []
    cost = []
    access_time = []
    hit_ratio = []

    for i in range(levels):
        print(f"\nMemory Level {i + 1}")

        s = float(input("Enter size: "))
        c = float(input("Enter cost per bit: "))
        t = float(input("Enter access time: "))
        h = float(input("Enter hit ratio (%): "))

        size.append(s)
        cost.append(c)
        access_time.append(t)
        hit_ratio.append(h / 100)

    if (any(s <= 0 for s in size)
            or any(c < 0 for c in cost)
            or any(t < 0 for t in access_time)
            or any(h < 0 or h > 1 for h in hit_ratio)):
        print("Invalid input!")

    else:
        # Calculate average cost per bit
        total_size = 0
        total_cost = 0

        for i in range(levels):
            total_size += size[i]
            total_cost += size[i] * cost[i]

        avg_cost = total_cost / total_size

        # Calculate average access time
        avg_time = access_time[0]
        miss_probability = 1

        for i in range(levels - 1):
            miss_probability *= (1 - hit_ratio[i])
            avg_time += miss_probability * access_time[i + 1]

        print("\n--- Results ---")
        print("Total memory size =", total_size)
        print("Total memory cost =", total_cost)
        print("Average cost per bit =", round(avg_cost, 4))
        print("Average access time =", round(avg_time, 4))