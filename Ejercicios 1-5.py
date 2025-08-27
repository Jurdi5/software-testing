import re

# 1. Function that checks if a given number is positive, negative, or zero
def check_number(num: float) -> str:
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# 2. Function that validates user passwords
def validate_password(password: str) -> bool:
    # At least 8 characters
    if len(password) < 8:
        return False
    # At least one uppercase, lowercase, digit, and special character
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%&]", password):
        return False
    return True


# 3. Function that calculates discount based on purchase amount
def calculate_discount(total_amount: float) -> float:
    if total_amount < 100:
        discount = 0
    elif 100 <= total_amount <= 500:
        discount = 0.10
    else:
        discount = 0.20
    return total_amount * (1 - discount)


# 4. Function that processes user orders in an e-commerce system
def process_order(order_items: list[dict]) -> float:
    """
    order_items is a list of dictionaries:
    [
        {"name": "item1", "price": 50, "quantity": 3},
        {"name": "item2", "price": 20, "quantity": 12}
    ]
    """
    total = 0
    for item in order_items:
        price = item["price"]
        quantity = item["quantity"]

        if 1 <= quantity <= 5:
            discount = 0
        elif 6 <= quantity <= 10:
            discount = 0.05
        else:  # quantity > 10
            discount = 0.10

        total += (price * quantity) * (1 - discount)
    return total


# 5. Function that calculates shipping costs
def calculate_shipping(total_weight: float, method: str) -> float:
    method = method.lower()
    if method == "standard":
        if total_weight <= 5:
            return 10
        elif total_weight <= 10:
            return 15
        else:
            return 20
    elif method == "express":
        if total_weight <= 5:
            return 20
        elif total_weight <= 10:
            return 30
        else:
            return 40
    else:
        raise ValueError("Invalid shipping method. Use 'standard' or 'express'.")


# -------------------------
# Ejemplos de uso
# -------------------------
print(check_number(-7))                      # Negative
print(validate_password("Abc123!@"))         # True
print(calculate_discount(450))               # 405.0
print(process_order([
    {"name": "Laptop", "price": 1000, "quantity": 2},
    {"name": "Mouse", "price": 50, "quantity": 12}
]))  # 1000*2 + (50*12 con 10% desc)
print(calculate_shipping(8, "express"))      # 30
