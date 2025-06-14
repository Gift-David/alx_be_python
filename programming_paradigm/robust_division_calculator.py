

def safe_divide(numerator, denominator):
    try:
        denominator < 0
    except:
        raise ZeroDivisionError("Error: Can't divide by zero")
    try:
        numerator, denominator
    except ValueError:
        print("Error: Cannot divide by zero.")
    return numerator / denominator