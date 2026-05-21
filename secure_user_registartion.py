"""Project 1: Building a Secure User Registration System"""

# -------------------------------------------------------------------
# Simulated Database
# -------------------------------------------------------------------

registered_users = []
failed_registrations = []

# -------------------------------------------------------------------
# Validation Functions
# -------------------------------------------------------------------

def validate_name(name: str):
    """
    Validate that the name contains at least 3 characters.
    Args:
        name (str): The user's name.
    Returns:
        bool: True if valid, otherwise False.
    """
    return len(name) >= 3

def validate_email(email: str):
    """
    Validate that the email contains both '@' and '.'.
    Args:
        email (str): The user's email address.
    Returns:
        bool: True if valid, otherwise False.
    """
    return "@" in email and "." in email


def validate_password(password: str):
    """
    Validate password strength.
    Rules:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one digit
    Args:
        password (str): The user's password.
    Returns:
        bool: True if the conditions are met, otherwise False.
    """
    return len(password) > 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password)

# -------------------------------------------------------------------
# Orchestrator Validation Function
# -------------------------------------------------------------------

def validate_user_data(name: str, email: str, password: str):
    """
    Validate all user inputs.
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
    Returns:
        bool: True if all validations pass.
    Raises:
        ValueError: If any validation rule fails. Different value errors depending on each one.
    """
    if not validate_name(name):
        raise ValueError("Name must contain at least 3 characters.")
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.'.")
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long and contain one uppercase letter and one digit.")
    return True

# -------------------------------------------------------------------
# Registration Function
# -------------------------------------------------------------------

def create_user_account(name: str, email: str, password: str):
    """
    Create a new user account after validation.
    Args:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
    Returns:
        dict: Create user dictionary if registration succeeds.
        None: Limited dictionary if registration fails.
    Raises:
        ValueError: Internally raised during validation or duplicate checks.
    """
    try:
        validate_user_data(name, email, password)
        if any(user["email"] == email for user in registered_users):
            raise ValueError("An account with this email already exists.")
        user_record = {
            "name": name,
            "email": email,
            "password": password,
            "status": "active",
        }
        registered_users.append(user_record)
        return user_record
    except ValueError as error:
        failed_registrations.append(
            {"email": email, "error": str(error)}
        )
        return None

  # -------------------------------------------------------------------
# Testing Section
# -------------------------------------------------------------------

def run_tests():
    """
    Execute sample registration scenarios.
    A valid registration
    A duplicate email
    An invalid name
    An invalid email
    A weak password
    Returns:
        None
    """
    test_cases = [
        ("Charlie", "charlie.warren145@optusnet.com.au", "PhiGammaBeta456"),
        ("Chara", "charlie.warren978@optusnet.com.au", "PhiGammaBeta456"),
        ("CW", "charlie.warren143@gmail.com.au", "PhiGammaBeta456"),
        ("Charlie", "charliewarren795@optusnetcomau", "PhiBetaGamma456"),
        ("Charlie", "charlie.warren247@gmail.com", "Phi4")
    ]

    for index, (name, email, password) in enumerate(test_cases, start=1):
        print(f"\nTest {index}")
        result = create_user_account(name, email, password)

        if result:
            print("Registration successful:", result)
        else:
            print("Registration failed.")

    print("\nFinal Registered Users:")
    print(registered_users)

    print("\nFailed Registrations:")
    print(failed_registrations)

run_tests()
