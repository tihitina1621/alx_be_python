def safe_divide(numerator, denominator):
    try:
        float(numerator) // float(denominator)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except ValueError:
        print('Please enter only floats.')
    else:
        numerator // denominator
    finally:
        print('thanl you')



