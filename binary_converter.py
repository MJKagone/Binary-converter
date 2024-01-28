'''
This is a simple binary conversion program that evolves over time as my skills develop.

Features:
-conversion between positive decimal, binary and hexadecimal integers
-inversion of binary digits
-conversion between binary code and text
'''

def binary_to_decimal(digit):
    digit = digit.replace(" ", "")
    try:
        for j in digit:
            if j in "10":
                pass
            else:
                return None
        sum = 0
        for i, number in enumerate(digit[::-1]):
            sum += int(number) * 2 ** i
        return sum
    except ValueError:
        pass
     
def decimal_to_binary(digit):
    try:
        sum = ""
        quotient = int(digit) // 2
        remainder = int(digit) % 2
        sum += str(remainder)
        while True:
            if quotient == 0:
                sum = sum [::-1]
                break
            elif quotient != 0:
                remainder = quotient % 2
                quotient = quotient // 2
                sum += str(remainder)
        while True:
            if len(sum) % 8 == 0:
                return sum
            else:
                sum = "0{}".format(sum)
    except ValueError:
        pass

def hexadecimal_to_decimal(digit):
    digit = digit.replace(" ", "")
    try:
        sum = 0
        hex_original = []
        hex_modified = []
        for i, number in enumerate(str(digit[::-1])):
            hex_original.append(number)
        hex_modified = ["10" if x == "a" or x == "A" else x for x in hex_original]       
        hex_modified = ["11" if x == "b" or x == "B" else x for x in hex_modified]      
        hex_modified = ["12" if x == "c" or x == "C" else x for x in hex_modified]
        hex_modified = ["13" if x == "d" or x == "D" else x for x in hex_modified]
        hex_modified = ["14" if x == "e" or x == "E" else x for x in hex_modified]
        hex_modified = ["15" if x == "f" or x == "F" else x for x in hex_modified]
        for j, number2 in enumerate(hex_modified):
            sum += int(number2) * 16 ** j
        return sum
    except NotImplementedError:
        pass    

def decimal_to_hexadecimal(digit):
    try:
        sum = ""
        quotient = int(digit) // 16
        remainder = int(digit) % 16
        if remainder == 10:
            remainder = "a"
        if remainder == 11:
            remainder = "b"
        if remainder == 12:
            remainder = "c"
        if remainder == 13:
            remainder = "d"
        if remainder == 14:
            remainder = "e"
        if remainder == 15:
            remainder = "f"
        sum += str(remainder)
        while True:
            if quotient == 0:
                sum = sum [::-1]
                return sum
            elif quotient != 0:
                remainder = quotient % 16
                quotient = quotient // 16
                if remainder == 10:
                    remainder = "a"
                if remainder == 11:
                    remainder = "b"
                if remainder == 12:
                    remainder = "c"
                if remainder == 13:
                    remainder = "d"
                if remainder == 14:
                    remainder = "e"
                if remainder == 15:
                    remainder = "f"
                sum += str(remainder)
    except ValueError:
        pass    

def invert_binary(digit):
    digit = digit.replace(" ", "")
    inverse_digit = ""
    for i in digit:
        
        if i == "0":
            inverse_digit += "1"
            
        else:
            inverse_digit += "0"
    return inverse_digit

def binary_to_ascii(digit):
    digit = digit.replace(" ", "")
    text = ""
    while len(digit) % 8 != 0:
        digit = "0" + digit
    while len(digit) > 0:
        byte = digit[:8]
        digit = digit[8:]
        text += chr(int(byte, 2))
    return text

def ascii_to_binary(text):
    binary = ""
    for i in text:
        binary += decimal_to_binary(ord(i))
    binary = " ".join(binary[i:i+8] for i in range(0, len(binary), 8))
    return binary


def main():
    counter = 0
    while True:
        if counter == 0:
            choice = input("""What sort of conversion would you like to make? The options are:
- binary to decimal (bin-dec or 2-10)
- decimal to binary (dec-bin or 10-2)
- hexadecimal to decimal (hex-dec or 16-10)
- hexadecimal to binary (hex-bin or 16-2)
- decimal to hexadecimal (dec-hex or 10-16)
- binary to hexadecimal (bin-hex or 2-16)
- invert binary digits (invert)
- binary to ASCII (bin-ascii)
- ASCII to binary (ascii-bin)
- quit (q)
Your choice: """)
        elif counter > 0:
            choice = input("What sort of conversion would you like to make? Your choice: ")
        if choice == "q":
            quit()
        elif choice == "invert":
            digit = input("Type a binary number to invert: ")
        elif choice == "bin-ascii":
            digit = input("Type a binary number to convert to ASCII: ")
        elif choice == "ascii-bin":
            text = input("Type a text to convert to binary: ")
        else: 
            digit = input("Type a digit to convert: ")
        print("")
        if choice == "bin-dec" or choice == "2-10":
            print("Binary {} is {} in decimal form.\n".format(digit, binary_to_decimal(digit)))
        if choice == "dec-bin" or choice == "10-2":
            print("Decimal {} is {} in binary form.\n".format(digit, decimal_to_binary(digit)))
        if choice == "hex-dec" or choice == "16-10":
            print("Hexadecimal {} is {} in decimal form.\n".format(digit, hexadecimal_to_decimal(digit)))
        if choice == "hex-bin" or choice == "16-2":
            decimal = int(hexadecimal_to_decimal(digit))
            print("Hexadecimal {} is {} in binary form.\n".format(digit, decimal_to_binary(decimal)))
        if choice == "dec-hex" or choice == "10-16":
            print("Decimal {} is {} in hexadecimal form.\n".format(digit, decimal_to_hexadecimal(digit)))
        if choice == "bin-hex" or choice == "2-16":
            decimal = binary_to_decimal(digit)
            print("Binary {} is {} in hexadecimal form.\n".format(digit, decimal_to_hexadecimal(decimal)))
        if choice == "invert" or choice == "i":
            print("The inverse of {} is {}.\n".format(digit, invert_binary(digit)))
        if choice == "bin-ascii":
            print(digit + ' is "' + binary_to_ascii(digit) + '" in ASCII\n')
        if choice == "ascii-bin":
            print(text + ' is "' + ascii_to_binary(text) + '" in binary\n')
        else:
            pass
        counter += 1

if __name__ == "__main__":
    main()
