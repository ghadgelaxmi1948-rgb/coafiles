def conversion(decimal_number):
    if decimal_number < 0:
        print("Please enter a non-negative integer.")
        return None
    binary = bin(decimal_number)[2:]
    octal = oct(decimal_number)[2:]
    hexadecimal = hex(decimal_number).upper()[2:]
    print("Decimal: {}\nBinary: {}\nOctal: {}\nHexadecimal: {}".format(decimal_number, binary, octal, hexadecimal))
    return None

print("Enter a decimal number:")
decimal_number = int(input())
conversion(decimal_number)
    
