def number_pattern(n):

    string_numbers = ''

    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    for i in range(1,n+1):
        string_numbers += str(i) + " "

    return string_numbers[:-1]
    
print(number_pattern(4))