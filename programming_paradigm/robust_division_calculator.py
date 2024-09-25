def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        float(numerator) // float(denominator)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except ValueError:
        print('Error: Please enter numeric values only.')
    else:        
        print(f'The result of the division is {float(numerator // denominator)}' ) 
    



