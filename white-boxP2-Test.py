import unittest

from white-boxP2.py import (
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem,
    authenticate_user,
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_url,
)


class TestValidateCreditCard(unittest.TestCase):

    def test_validate_credit_card_too_short(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_too_long(self):
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")

    def test_validate_credit_card_valid_13_digits(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_16_digits(self):
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")


class TestValidateDate(unittest.TestCase):

    def test_validate_date_year_too_low(self):
        self.assertEqual(validate_date(1899, 5, 15), "Invalid Date")

    def test_validate_date_year_too_high(self):
        self.assertEqual(validate_date(2101, 5, 15), "Invalid Date")

    def test_validate_date_month_too_low(self):
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        self.assertEqual(validate_date(2000, 5, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        self.assertEqual(validate_date(2000, 5, 32), "Invalid Date")

    def test_validate_date_valid_lower_limits(self):
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_valid_upper_limits(self):
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_valid_mid_range(self):
        self.assertEqual(validate_date(2025, 6, 15), "Valid Date")


class TestCheckFlightEligibility(unittest.TestCase):

    def test_check_flight_eligibility_too_young_not_frequent(self):
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_check_flight_eligibility_too_old_not_frequent(self):
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_check_flight_eligibility_valid_age_range(self):
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_young_with_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(15, True), "Eligible to Book")

    def test_check_flight_eligibility_old_with_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_check_flight_eligibility_boundary_18(self):
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_check_flight_eligibility_boundary_65(self):
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")


class TestValidateUrl(unittest.TestCase):

    def test_validate_url_too_long(self):
        long_url = "http://" + "a" * 250
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_validate_url_no_protocol(self):
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_wrong_protocol(self):
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_valid_http(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        self.assertEqual(validate_url("https://example.com"), "Valid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):

    def test_calculate_quantity_discount_no_discount_lower(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_calculate_quantity_discount_no_discount_upper(self):
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5_percent_lower(self):
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_5_percent_upper(self):
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_calculate_quantity_discount_10_percent_large(self):
        self.assertEqual(calculate_quantity_discount(100), "10% Discount")


class TestCheckFileSize(unittest.TestCase):

    def test_check_file_size_zero(self):
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_within_limit(self):
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_at_limit(self):
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_over_limit(self):
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_file_size_negative(self):
        self.assertEqual(check_file_size(-1), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):

    def test_check_loan_eligibility_income_too_low(self):
        self.assertEqual(check_loan_eligibility(25000, 750), "Not Eligible")

    def test_check_loan_eligibility_mid_income_good_credit(self):
        self.assertEqual(check_loan_eligibility(40000, 710), "Standard Loan")

    def test_check_loan_eligibility_mid_income_poor_credit(self):
        self.assertEqual(check_loan_eligibility(40000, 650), "Secured Loan")

    def test_check_loan_eligibility_high_income_excellent_credit(self):
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_check_loan_eligibility_high_income_good_credit(self):
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_check_loan_eligibility_boundary_30000_good_credit(self):
        self.assertEqual(check_loan_eligibility(30000, 710), "Standard Loan")

    def test_check_loan_eligibility_boundary_60000_excellent_credit(self):
        self.assertEqual(check_loan_eligibility(60000, 760), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):

    def test_calculate_shipping_cost_small_package(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_small_package_boundary(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_medium_package(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_calculate_shipping_cost_medium_package_lower_boundary(self):
        self.assertEqual(calculate_shipping_cost(2, 11, 11, 11), 10)

    def test_calculate_shipping_cost_medium_package_upper_boundary(self):
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_calculate_shipping_cost_large_package(self):
        self.assertEqual(calculate_shipping_cost(6, 31, 31, 31), 20)

    def test_calculate_shipping_cost_oversized(self):
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)


class TestGradeQuiz(unittest.TestCase):

    def test_grade_quiz_pass_excellent(self):
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_pass_boundary(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_conditional_pass_boundary(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_conditional_pass(self):
        self.assertEqual(grade_quiz(6, 2), "Conditional Pass")

    def test_grade_quiz_fail_too_few_correct(self):
        self.assertEqual(grade_quiz(4, 3), "Fail")

    def test_grade_quiz_fail_too_many_incorrect(self):
        self.assertEqual(grade_quiz(7, 4), "Fail")

    def test_grade_quiz_fail_poor_performance(self):
        self.assertEqual(grade_quiz(2, 8), "Fail")


class TestAuthenticateUser(unittest.TestCase):

    def test_authenticate_user_admin(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_valid_user(self):
        self.assertEqual(authenticate_user("johndoe", "password123"), "User")

    def test_authenticate_user_username_too_short(self):
        self.assertEqual(authenticate_user("user", "password123"), "Invalid")

    def test_authenticate_user_password_too_short(self):
        self.assertEqual(authenticate_user("johndoe", "pass"), "Invalid")

    def test_authenticate_user_both_too_short(self):
        self.assertEqual(authenticate_user("user", "pass"), "Invalid")

    def test_authenticate_user_boundary_username(self):
        self.assertEqual(authenticate_user("user5", "password123"), "User")

    def test_authenticate_user_boundary_password(self):
        self.assertEqual(authenticate_user("johndoe", "pass1234"), "User")


class TestGetWeatherAdvisory(unittest.TestCase):

    def test_get_weather_advisory_high_temp_and_humidity(self):
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated."
        )

    def test_get_weather_advisory_high_temp_normal_humidity(self):
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")

    def test_get_weather_advisory_normal_temp_high_humidity(self):
        self.assertEqual(get_weather_advisory(25, 80), "No Specific Advisory")

    def test_get_weather_advisory_low_temperature(self):
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_boundary_zero(self):
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")

    def test_get_weather_advisory_normal_conditions(self):
        self.assertEqual(get_weather_advisory(20, 60), "No Specific Advisory")


class TestUserAuthentication(unittest.TestCase):

    def setUp(self):
        self.auth = UserAuthentication()
        self.assertEqual(self.auth.state, "Logged Out")

    def test_user_authentication_login_success(self):
        output = self.auth.login()
        
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_user_authentication_login_when_logged_in(self):
        self.auth.login()
        output = self.auth.login()
        
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")

    def test_user_authentication_logout_success(self):
        self.auth.login()
        output = self.auth.logout()
        
        self.assertEqual(self.auth.state, "Logged Out")
        self.assertEqual(output, "Logout successful")

    def test_user_authentication_logout_when_logged_out(self):
        output = self.auth.logout()
        
        self.assertEqual(self.auth.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")


class TestDocumentEditingSystem(unittest.TestCase):

    def setUp(self):
        self.doc_system = DocumentEditingSystem()
        self.assertEqual(self.doc_system.state, "Editing")

    def test_document_editing_system_save_success(self):
        output = self.doc_system.save_document()
        
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_document_editing_system_save_when_saved(self):
        self.doc_system.save_document()
        output = self.doc_system.save_document()
        
        self.assertEqual(self.doc_system.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_document_editing_system_edit_success(self):
        self.doc_system.save_document()
        output = self.doc_system.edit_document()
        
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(output, "Editing resumed")

    def test_document_editing_system_edit_when_editing(self):
        output = self.doc_system.edit_document()
        
        self.assertEqual(self.doc_system.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")


class TestElevatorSystem(unittest.TestCase):

    def setUp(self):
        self.elevator = ElevatorSystem()
        self.assertEqual(self.elevator.state, "Idle")

    def test_elevator_system_move_up_success(self):
        output = self.elevator.move_up()
        
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_elevator_system_move_up_when_moving(self):
        self.elevator.move_up()
        output = self.elevator.move_up()
        
        self.assertEqual(self.elevator.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_move_down_success(self):
        output = self.elevator.move_down()
        
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_elevator_system_move_down_when_moving(self):
        self.elevator.move_down()
        output = self.elevator.move_down()
        
        self.assertEqual(self.elevator.state, "Moving Down")
        self.assertEqual(output, "Invalid operation in current state")

    def test_elevator_system_stop_from_moving_up(self):
        self.elevator.move_up()
        output = self.elevator.stop()
        
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_elevator_system_stop_from_moving_down(self):
        self.elevator.move_down()
        output = self.elevator.stop()
        
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_elevator_system_stop_when_idle(self):
        output = self.elevator.stop()
        
        self.assertEqual(self.elevator.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")


if __name__ == "__main__":
    unittest.main()