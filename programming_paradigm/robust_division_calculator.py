def safe_divide(numerator, denominator):
    try:
        float(numerator) // float(denominator)
    except ZeroDivisionError:
        print('we cannot devide number by zero')
    except ValueError:
        print('Please enter only floats.')
    else:
        numerator // denominator
    finally:
        print('thanl you')



