# 11
def validate_credit_card(card_number):
    """
    Validates credit card numbers.
    """
    if 13 <= len(card_number) <= 16 and card_number.isdigit():
        return "Valid Card"

    return "Invalid Card"


# 12
def validate_date(year, month, day):
    """
    Validates dates.
    """
    if 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
        return "Valid Date"

    return "Invalid Date"


# 13
def check_flight_eligibility(age, frequent_flyer):
    """
    Checks the eligibility of a passenger to book a flight.
    """
    if 18 <= age <= 65 or frequent_flyer:
        return "Eligible to Book"

    return "Not Eligible to Book"


# 14
def validate_url(url):
    """
    Validates URLs.
    """
    if len(url) <= 255 and url.startswith("http://") or url.startswith("https://"):
        return "Valid URL"

    return "Invalid URL"


# 15
def calculate_quantity_discount(quantity):
    """
    Calculates discounts based on the quantity of a product.
    """
    if 1 <= quantity <= 5:
        return "No Discount"

    if 6 <= quantity <= 10:
        return "5% Discount"

    return "10% Discount"


# 16
def check_file_size(size_in_bytes):
    """
    Checks if the size is valid for a file.
    """
    if 0 <= size_in_bytes <= 1048576:  # 1 MB in bytes
        return "Valid File Size"

    return "Invalid File Size"


# 17
def check_loan_eligibility(income, credit_score):
    """
    Checks if and which loan can be granted based on the income and credit score.
    """
    if income < 30000:
        return "Not Eligible"

    if 30000 <= income <= 60000:
        if credit_score > 700:
            return "Standard Loan"

        return "Secured Loan"

    if credit_score > 750:
        return "Premium Loan"

    return "Standard Loan"


# 18
def calculate_shipping_cost(weight, length, width, height):
    """
    Calculates the shipping cost based on the package weight and dimensions.
    """
    if weight <= 1 and length <= 10 and width <= 10 and height <= 10:
        return 5

    if (
        1 < weight <= 5
        and 11 <= length <= 30
        and 11 <= width <= 30
        and 11 <= height <= 30
    ):
        return 10

    return 20


# 19
def grade_quiz(correct_answers, incorrect_answers):
    """
    Grades online quizzes based on the number of correct and incorrect answers.
    """
    if correct_answers >= 7 and incorrect_answers <= 2:
        return "Pass"

    if correct_answers >= 5 and incorrect_answers <= 3:
        return "Conditional Pass"

    return "Fail"


# 20
def authenticate_user(username, password):
    """
    Authenticates users based on their username and password.
    """
    if username == "admin" and password == "admin123":
        return "Admin"

    if len(username) >= 5 and len(password) >= 8:
        return "User"

    return "Invalid"


# 21
def get_weather_advisory(temperature, humidity):
    """
    Provides weather advisories based on temperature and humidity.
    """
    if temperature > 30 and humidity > 70:
        return "High Temperature and Humidity. Stay Hydrated."

    if temperature < 0:
        return "Low Temperature. Bundle Up!"

    return "No Specific Advisory"


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
