def check_pwd(password):
    if len(password) < 8 or len(password) > 20:
        return False

    has_lowercase = False
    has_uppercase = False
    for character in password:
        if character >= 'a' and character <= 'z':
            has_lowercase = True
        if character >= 'A' and character <= 'Z':
            has_uppercase = True

    if not has_lowercase or not has_uppercase:
        return False
    return True