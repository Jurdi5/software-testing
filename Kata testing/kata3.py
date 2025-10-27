import re
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    errors: str

def validate_password(password: str) -> ValidationResult:
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    if len(re.findall(r"\d", password)) < 2:
        errors.append("The password must contain at least 2 numbers")

    if not re.search(r"[A-Z]", password):
        errors.append("password must contain at least one capital letter")

    if not re.search(r"[^\w\s]", password):
        errors.append("password must contain at least one special character")

    return ValidationResult(is_valid=not errors, errors="\n".join(errors))