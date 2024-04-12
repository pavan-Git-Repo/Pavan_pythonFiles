def print_formatted(number):
    # your code goes here
    width = len(str(bin(n)))-2
    for num in range(1, n+1):
        decimal = int(num)
        octal = oct(num)
        hexadecimal = hex(num)
        binary = bin(num)

        print(str(decimal).rjust(width), octal[2:].rjust(width), hexadecimal[2:].title().rjust(width), binary[2:].rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)