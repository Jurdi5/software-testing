# -*- coding: utf-8 -*-


# PR test: agregado para poder enviar a revisión

"""
White-box code examples.
"""
import re


def is_even(num):
    """
    Checks if a number is even.
    """
    return num % 2 == 0


def divide(a, b):
    """
    Simple division function.
    """
    result = 0
    if b != 0:
        result = a / b
    return result


def get_grade(score):
    """
    Grade function.
    """
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade


def is_triangle(a, b, c):
    """
    Determines if 3 numbers can form a triangle.
    """
    if a + b > c and a + c > b and b + c > a:
        return "Yes, it's a triangle!"

    return "No, it's not a triangle."


# 1
def check_number_status(number):
    """
    Checks if a given number is positive, negative, or zero.
    """
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


# 2
def validate_password(password):
    """
    Validates user passwords.
    """
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter,
    # one digit, and one special character.
    if (
        not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"\d", password)
        or not re.search(r"[!@#$%&]", password)
    ):
        return False

    return True


# 3
def calculate_total_discount(total_amount):
    """
    Calculates the discount for a customer's purchase based on the total amount.
    """
    if total_amount < 100:
        return 0

    if 100 <= total_amount <= 500:
        return 0.1 * total_amount

    return 0.2 * total_amount


# 4
def calculate_order_total(items):
    """
    Processes user orders in an e-commerce system.
    The function calculates the total price of the items in the order,
    applying different discounts based on the quantity of each item.
    """
    total_price = 0

    for item in items:
        quantity = item["quantity"]
        price_per_item = item["price"]

        # Apply discounts based on quantity
        if 1 <= quantity <= 5:
            total_price += quantity * price_per_item
        elif 6 <= quantity <= 10:
            total_price += 0.95 * quantity * price_per_item  # 5% discount
        else:
            total_price += 0.9 * quantity * price_per_item  # 10% discount

    return total_price


# 5
def calculate_items_shipping_cost(items, shipping_method):
    """
    Calculates shipping costs for an online shopping system.
    The function calculates shipping costs based on the total weight of the
    items in the order and the shipping method chosen by the customer.
    """
    total_weight = sum(item["weight"] for item in items)

    if shipping_method == "standard":
        if total_weight <= 5:
            return 10

        if 5 < total_weight <= 10:
            return 15

        return 20

    if shipping_method == "express":
        if total_weight <= 5:
            return 20

        if 5 < total_weight <= 10:
            return 30

        return 40

    raise ValueError("Invalid shipping method")


# 6
def validate_login(username, password):
    """
    Validates user login credentials.
    """
    if 5 <= len(username) <= 20 and 8 <= len(password) <= 15:
        return "Login Successful"

    return "Login Failed"


# 7
def verify_age(age):
    """
    Determines whether a person is eligible for a certain service based on their age.
    """
    if 18 <= age <= 65:
        return "Eligible"

    return "Not Eligible"


# 8
def categorize_product(price):
    """
    Determines the price category of a product based on its price.
    """
    if 10 <= price <= 50:
        return "Category A"

    if 51 <= price <= 100:
        return "Category B"

    if 101 <= price <= 200:
        return "Category C"

    return "Category D"


# 9
def validate_email(email):
    """
    Validates email addresses.
    """
    if 5 <= len(email) <= 50 and "@" in email and "." in email:
        return "Valid Email"

    return "Invalid Email"


# 10
def celsius_to_fahrenheit(celsius):
    """
    Converts temperatures from Celsius to Fahrenheit.
    """
    if -100 <= celsius <= 100:
        return (celsius * 9 / 5) + 32

    return "Invalid Temperature"

# 23
class TrafficLight:
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """

    def __init__(self):
        """
        Defines the traffic light initial state.
        """
        self.state = "Red"

    def change_state(self):
        """
        Function that changes the traffic light state.
        """
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def get_current_state(self):
        """
        Provides the current traffic light state.
        """
        return self.state


# 1
    def test_check_number_status_positive(self):
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_status_negative(self):
        self.assertEqual(check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    # 2
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Valid1@pw"))

    def test_validate_password_too_short(self):
        self.assertFalse(validate_password("Ab1@"))

    def test_validate_password_missing_uppercase(self):
        self.assertFalse(validate_password("valid1@pw"))

    def test_validate_password_missing_digit(self):
        self.assertFalse(validate_password("Invalid@pw"))

    def test_validate_password_missing_special(self):
        self.assertFalse(validate_password("Invalid1pw"))

    # 3
    def test_calculate_total_discount_less_than_100(self):
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_between_100_and_500(self):
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_more_than_500(self):
        self.assertEqual(calculate_total_discount(600), 120)

    # 4
    def test_calculate_order_total_no_discount(self):
        items = [{"quantity": 2, "price": 10}]
        self.assertEqual(calculate_order_total(items), 20)

    def test_calculate_order_total_5_percent_discount(self):
        items = [{"quantity": 6, "price": 10}]
        self.assertEqual(calculate_order_total(items), 57)  # 6*10*0.95

    def test_calculate_order_total_10_percent_discount(self):
        items = [{"quantity": 12, "price": 10}]
        self.assertEqual(calculate_order_total(items), 108)  # 12*10*0.9

    # 5
    def test_calculate_items_shipping_cost_standard_low_weight(self):
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_mid_weight(self):
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_high_weight(self):
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_low_weight(self):
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_mid_weight(self):
        items = [{"weight": 9}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_high_weight(self):
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_method(self):
        items = [{"weight": 3}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "fast")

    # 6
    def test_validate_login_success(self):
        self.assertEqual(validate_login("username", "Password1"), "Login Successful")

    def test_validate_login_fail_short_username(self):
        self.assertEqual(validate_login("usr", "Password1"), "Login Failed")

    def test_validate_login_fail_short_password(self):
        self.assertEqual(validate_login("username", "short"), "Login Failed")

    # 7
    def test_verify_age_eligible(self):
        self.assertEqual(verify_age(30), "Eligible")

    def test_verify_age_not_eligible_underage(self):
        self.assertEqual(verify_age(15), "Not Eligible")

    def test_verify_age_not_eligible_overage(self):
        self.assertEqual(verify_age(70), "Not Eligible")

    # 8
    def test_categorize_product_category_a(self):
        self.assertEqual(categorize_product(20), "Category A")

    def test_categorize_product_category_b(self):
        self.assertEqual(categorize_product(80), "Category B")

    def test_categorize_product_category_c(self):
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_category_d(self):
        self.assertEqual(categorize_product(500), "Category D")

    # 9
    def test_validate_email_valid(self):
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_validate_email_invalid_no_at(self):
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_invalid_short(self):
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    # 10
    def test_celsius_to_fahrenheit_valid(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_celsius_to_fahrenheit_invalid(self):
        self.assertEqual(celsius_to_fahrenheit(200), "Invalid Temperature")


# 23
class TrafficLight:
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """

    def __init__(self):
        """
        Defines the traffic light initial state.
        """
        self.state = "Red"

    def change_state(self):
        """
        Function that changes the traffic light state.
        """
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def get_current_state(self):
        """
        Provides the current traffic light state.
        """
        return self.state


# --- Tests para TrafficLight ---
import unittest

class TestTrafficLight(unittest.TestCase):
    """Unit tests for TrafficLight"""

    def setUp(self):
        self.light = TrafficLight()

    def test_initial_state(self):
        """El semáforo inicia en rojo"""
        self.assertEqual(self.light.get_current_state(), "Red")

    def test_change_state_red_to_green(self):
        """De rojo debe pasar a verde"""
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """De verde debe pasar a amarillo"""
        self.light.state = "Green"
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """De amarillo debe volver a rojo"""
        self.light.state = "Yellow"
        self.light.change_state()
        self.assertEqual(self.light.get)

# 24
class UserAuthentication:
    """
    A user authentication system with states "Logged Out" and "Logged In."
    """

    def __init__(self):
        """
        Defines the user initial state.
        """
        self.state = "Logged Out"

    def login(self):
        """
        Function to login a user.
        """
        if self.state == "Logged Out":
            self.state = "Logged In"
            return "Login successful"

        return "Invalid operation in current state"

    def logout(self):
        """
        Function to logout a user.
        """
        if self.state == "Logged In":
            self.state = "Logged Out"
            return "Logout successful"

        return "Invalid operation in current state"


# 25
class DocumentEditingSystem:
    """
    A document editing system with states "Editing" and "Saved."
    """

    def __init__(self):
        """
        Defines the initial state.
        """
        self.state = "Editing"

    def save_document(self):
        """
        Function to save a document.
        """
        if self.state == "Editing":
            self.state = "Saved"
            return "Document saved successfully"

        return "Invalid operation in current state"

    def edit_document(self):
        """
        Function to edit a document.
        """
        if self.state == "Saved":
            self.state = "Editing"
            return "Editing resumed"

        return "Invalid operation in current state"


# 26
class ElevatorSystem:
    """
    An elevator system with states "Idle," "Moving Up," and "Moving Down."
    """

    def __init__(self):
        """
        Defines the elevator initial state.
        """
        self.state = "Idle"

    def move_up(self):
        """
        Function to move up the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Up"
            return "Elevator moving up"

        return "Invalid operation in current state"

    def move_down(self):
        """
        Function to move down the elevator.
        """
        if self.state == "Idle":
            self.state = "Moving Down"
            return "Elevator moving down"

        return "Invalid operation in current state"

    def stop(self):
        """
        Function to stop the elevator.
        """
        if self.state in ["Moving Up", "Moving Down"]:
            self.state = "Idle"
            return "Elevator stopped"

        return "Invalid operation in current state"


# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        print(f"The account {self.account_number} has a balance of {self.balance}")


class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True


# 28
class Product:  # pylint: disable=too-few-public-methods
    """
    Product class.
    """

    def __init__(self, name, price):
        """
        Set the product details.
        """
        self.name = name
        self.price = price

    def view_product(self):
        """
        Function to display the product details.
        """
        msg = f"The product {self.name} has a price of {self.price}"
        print(msg)
        return msg


class ShoppingCart:
    """
    Shopping cart class.
    """

    def __init__(self):
        """
        Initialize the shopping cart.
        """
        self.items = []

    def add_product(self, product, quantity=1):
        """
        Function to add a product to the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product, quantity=1):
        """
        Function to remove a product from the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.items.remove(item)
                else:
                    item["quantity"] -= quantity
                break

    def view_cart(self):
        """
        Function to display the shopping cart content.
        """
        for item in self.items:
            print(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def checkout(self):
        """
        Function to checkout the items from the shopping cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        print(f"Total: ${total}")
        print("Checkout completed. Thank you for shopping!")

# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        print(f"The account {self.account_number} has a balance of {self.balance}")


class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True


# 28
class Product:  # pylint: disable=too-few-public-methods
    """
    Product class.
    """

    def __init__(self, name, price):
        """
        Set the product details.
        """
        self.name = name
        self.price = price

    def view_product(self):
        """
        Function to display the product details.
        """
        msg = f"The product {self.name} has a price of {self.price}"
        print(msg)
        return msg


class ShoppingCart:
    """
    Shopping cart class.
    """

    def __init__(self):
        """
        Initialize the shopping cart.
        """
        self.items = []

    def add_product(self, product, quantity=1):
        """
        Function to add a product to the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product, quantity=1):
        """
        Function to remove a product from the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.items.remove(item)
                else:
                    item["quantity"] -= quantity
                break

    def view_cart(self):
        """
        Function to display the shopping cart content.
        """
        for item in self.items:
            print(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def checkout(self):
        """
        Function to checkout the items from the shopping cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        print(f"Total: ${total}")
        print("Checkout completed. Thank you for shopping!")

        # -*- coding: utf-8 -*-
"""
Unit tests for exercises 27 and 28.
"""
import unittest
from io import StringIO
from unittest.mock import patch



class TestBankingSystem(unittest.TestCase):
    """
    Unit tests for BankingSystem and BankAccount (Exercise 27).
    """

    def setUp(self):
        self.bank = BankingSystem()

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_success(self, mock_stdout):
        """
        Checks that a valid user can log in.
        """
        result = self.bank.authenticate("user123", "pass123")
        self.assertTrue(result)
        self.assertIn("User user123 authenticated successfully.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_failure(self, mock_stdout):
        """
        Checks authentication fails with invalid credentials.
        """
        result = self.bank.authenticate("user123", "wrongpass")
        self.assertFalse(result)
        self.assertIn("Authentication failed.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_authenticate_already_logged_in(self, mock_stdout):
        """
        Checks that a user already logged in cannot log in again.
        """
        self.bank.authenticate("user123", "pass123")
        result = self.bank.authenticate("user123", "pass123")
        self.assertFalse(result)
        self.assertIn("User already logged in.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_success_regular(self, mock_stdout):
        """
        Checks a successful regular money transfer.
        """
        self.bank.authenticate("user123", "pass123")
        result = self.bank.transfer_money("user123", "receiver456", 100, "regular")
        self.assertTrue(result)
        self.assertIn("Money transfer of $100 (regular transfer)", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_invalid_type(self, mock_stdout):
        """
        Checks transfer fails with an invalid transaction type.
        """
        self.bank.authenticate("user123", "pass123")
        result = self.bank.transfer_money("user123", "receiver456", 50, "invalid")
        self.assertFalse(result)
        self.assertIn("Invalid transaction type.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_not_authenticated(self, mock_stdout):
        """
        Checks transfer fails when sender is not authenticated.
        """
        result = self.bank.transfer_money("user123", "receiver456", 100, "regular")
        self.assertFalse(result)
        self.assertIn("Sender not authenticated.", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_transfer_money_insufficient_funds(self, mock_stdout):
        """
        Checks transfer fails if funds are insufficient.
        """
        self.bank.authenticate("user123", "pass123")
        result = self.bank.transfer_money("user123", "receiver456", 2000, "express")
        self.assertFalse(result)
        self.assertIn("Insufficient funds.", mock_stdout.getvalue())


class TestShoppingCart(unittest.TestCase):
    """
    Unit tests for Product and ShoppingCart (Exercise 28).
    """

    def setUp(self):
        self.cart = ShoppingCart()
        self.prod1 = Product("Laptop", 1000)
        self.prod2 = Product("Mouse", 50)

    def test_add_product_new_item(self):
        """
        Checks a product can be added to the cart.
        """
        self.cart.add_product(self.prod1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_add_product_existing_item(self):
        """
        Checks quantity increases when adding an existing product.
        """
        self.cart.add_product(self.prod2, 1)
        self.cart.add_product(self.prod2, 2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_partial(self):
        """
        Checks removing some quantity decreases correctly.
        """
        self.cart.add_product(self.prod1, 3)
        self.cart.remove_product(self.prod1, 1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_remove_product_entirely(self):
        """
        Checks removing all quantity removes product from cart.
        """
        self.cart.add_product(self.prod2, 1)
        self.cart.remove_product(self.prod2, 1)
        self.assertEqual(len(self.cart.items), 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_cart(self, mock_stdout):
        """
        Checks that viewing the cart prints correct details.
        """
        self.cart.add_product(self.prod1, 1)
        self.cart.view_cart()
        output = mock_stdout.getvalue()
        self.assertIn("1 x Laptop - $1000", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_checkout(self, mock_stdout):
        """
        Checks that checkout prints total and confirmation.
        """
        self.cart.add_product(self.prod1, 1)
        self.cart.add_product(self.prod2, 2)
        self.cart.checkout()
        output = mock_stdout.getvalue()
        self.assertIn("Total: $1100", output)
        self.assertIn("Checkout completed.", output)


if __name__ == "__main__":
    unittest.main()
