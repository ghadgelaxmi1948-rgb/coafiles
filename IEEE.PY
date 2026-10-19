import struct

def float_to_ieee754(num):
    packed = struct.pack('>f', num)
    binary_str = ''.join(f'{b:08b}' for b in packed)
    sign = binary_str[0]
    exponent = binary_str[1:9]
    mantissa = binary_str[9:]
    print(f"Decimal Number: {num}")
    print(f"Sign Bit (1b):  {sign}")
    print(f"Exponent (8b):  {exponent}")
    print(f"Mantissa (23b): {mantissa}")
    print(f"Full 32-bit Representation: {sign} {exponent} {mantissa}")
num = float(input("Enter a decimal number: "))
float_to_ieee754(num)
