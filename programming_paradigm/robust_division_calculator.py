def safe_divide(numerator, denominator):
    try:
        float(numerator) // float(denominator)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except ValueError:
        print('Error: Please enter numeric values only.')
    else:        
        print(f'The result ot th division is ' {float(numerator // denominator)} ) 
    



