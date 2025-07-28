def check_pwd(password):
    if len(password) < 8 or len(password) > 20:
        return False
    return True