from database import create_user, verify_user
def register_user(name, email, password, role):
    if not name.strip():
        return False, "Enter your name."
    if not email.strip():
        return False, "Enter your email."
    if "@" not in email:
        return False, "Enter a valid email."
    if len(password) < 4:
        return False, "Password must contain at least 4 characters."
    if role not in ["student", "recruiter"]:
        return False, "Invalid account type."
    return create_user(
        name,
        email,
        password,
        role
    )
def login_user(email, password):
    if not email.strip() or not password:
        return None
    return verify_user(
        email,
        password
    )
