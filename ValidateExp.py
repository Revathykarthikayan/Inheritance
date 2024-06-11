import re
def validate_input(input_str, input_type):
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'bd_mobile': r'^(\+88)?01[3-9]\d{8}$',
        'us_telephone': r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$',
        'strong_password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    }

    pattern = patterns.get(input_type)
    if not pattern:
        raise ValueError("Invalid input type. Choose from 'email', 'bd_mobile', 'us_telephone', 'strong_password'")

    if re.match(pattern, input_str):
        return True
    else:
        return False



print(validate_input("example@example.com", "email"))  # True
print(validate_input("+8801712345678", "bd_mobile"))  # True
print(validate_input("01712345678", "bd_mobile"))  # True
print(validate_input("(123) 456-7890", "us_telephone"))  # True
print(validate_input("123-456-7890", "us_telephone"))  # True
print(validate_input("123.456.7890", "us_telephone"))  # True
print(validate_input("StrongPass@1234a", "strong_password"))  # False
print(validate_input("StrongPass@1234Ab", "strong_password"))  # True
print(validate_input("WeakPass123", "strong_password"))  # False
print(validate_input("S!tr0ngP@ssword1234", "strong_password"))  # True
