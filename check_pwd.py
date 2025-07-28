def check_pwd(password):
    if len(password) < 8 or len(password) > 20:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_symbol = False

    for character in password:
        if character >= 'a' and character <= 'z':
            has_lowercase = True
        if character >= 'A' and character <= 'Z':
            has_uppercase = True
        if character >= '0' and character <= '9':
            has_digit = True
        if character in "~`!@#$%^&*()_+-=":
            has_symbol = True

    if not has_lowercase or not has_uppercase or not has_digit or not has_symbol:
        return False
    return True