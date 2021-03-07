from cs50 import get_string

# Define main


def main():
    # Get a valid number
    while (True):
        number = get_string("Number: ")
        if number.isdigit():
            break

    # Make sure it complies with Luhn's
    if (not check(number)):
        print("INVALID")
        exit(1)
        
    # Find its type and print it
    find_type(number)
    
# Define the function find type of number


def find_type(number):
    length = len(number)
    if (number[0] == '5'):
        if number[1] == '1' or number[1] == '2' or number[1] == '3' or number[1] == '4' or number[1] == '5':
            if (length == 13 or length == 16):
                print("MASTERCARD")
                return()
    elif (number[0] == '3'):
        if number[1] == '4' or number[1] == '7':
            if length == 15:
                print("AMEX")
                return()
        else:
            print("INVALID")
    elif (number[0] == '4'):
        if length == 13 or length == 16:
            print("VISA")
            return()
    print("INVALID")
    
# Define the function check a nnumber


def check(number):
    sum_of_digits = 0
    # Add the digits of select numbers multiplied by two
    i = len(number) - 2
    while i >= 0:
        extra = int(number[i]) * 2
        sum_of_digits += extra % 10
        if extra > 9:  # 2 digits
            sum_of_digits += int(extra / 10)
        i -= 2
    sum_others = 0
    i = len(number) - 1
    while i >= 0:
        sum_others += int(number[i])
        i -= 2
    if (sum_others + sum_of_digits) % 10 == 0:
        return True
    else:
        return False


# Call main
main()