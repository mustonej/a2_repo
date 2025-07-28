def check_pwd(password):
    if len(password) < 8 or len(password) > 20:
        return False

    has_lowercase = False
    for character in password:
        if character >= 'a' and character <= 'z':
            has_lowercase = True
            break
    if not has_lowercase:
        return False
    return True