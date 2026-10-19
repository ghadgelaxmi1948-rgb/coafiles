# Speedup, Efficiency and Throughput

n = int(input("Enter number of instructions: "))
k = int(input("Enter number of pipeline stages: "))
f = float(input("Enter clock frequency (in Hz): "))

# Clock cycle time
t = 1 / f

# Execution time without pipelining
non_pipeline_time = n * k * t

# Execution time with pipelining
pipeline_time = (k + n - 1) * t

# Speedup
speedup = non_pipeline_time / pipeline_time

# Efficiency
efficiency = speedup / k

# Throughput
throughput = n / pipeline_time

print("\n--- Results ---")
print(f"Speedup = {speedup:.2f}")
print(f"Efficiency = {efficiency * 100:.2f}%")
print(f"Throughput = {throughput:.2f} instructions/second")