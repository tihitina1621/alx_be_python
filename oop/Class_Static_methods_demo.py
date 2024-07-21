class Calculator:
    calculation_type = 'Arithmetic Operations'
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def multiply(cls,a,b):
        cls.a = a
        cls.b = b
        print(f'Calcualtion type: {cls.calculation_type}')
        return a * b
sum_result = Calculator.add(10, 5)
print(f"The sum is: {sum_result}")
# Using the class method
product_result = Calculator.multiply(10, 5)
print(f"The product is: {product_result}")