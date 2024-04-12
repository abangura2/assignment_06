"""
Description: A class used to test the Mortgage class.
Author: AbdulRahman Hassan Bangura
Date: 08/04/24
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""


from unittest import TestCase 
from mortgage.mortgage import Mortgage 
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    
    def test_init_raises_value_error_for_invalid_amount(self):
        """Test that __init__ raises a ValueError for invalid amount."""
        with self.assertRaises(ValueError):
            Mortgage(-100, 'FIXED_5', 'MONTHLY', 25)

    def test_init_raises_value_error_for_invalid_rate(self):
        """Test that __init__ raises a ValueError for invalid rate."""
        with self.assertRaises(ValueError):
            Mortgage(100000, 'INVALID_RATE', 'MONTHLY', 25)

    def test_init_raises_value_error_for_invalid_frequency(self):
        """Test that __init__ raises a ValueError for invalid frequency."""
        with self.assertRaises(ValueError):
            Mortgage(100000, 'FIXED_5', 'INVALID_FREQUENCY', 25)

    def test_init_raises_value_error_for_invalid_amortization(self):
        """Test that __init__ raises a ValueError for invalid amortization."""
        with self.assertRaises(ValueError):
            Mortgage(100000, 'FIXED_5', 'MONTHLY', 35)

    def test_loan_amount_mutator_with_negative_value(self):
        """Test that setting the loan amount to a negative value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        with self.assertRaises(ValueError):
            mortgage.set_loan_amount(-100)

    def test_loan_amount_mutator_with_zero(self):
        """Test that setting the loan amount to zero."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        with self.assertRaises(ValueError):
            mortgage.set_loan_amount(0)

    def test_loan_amount_mutator_with_positive_value_value(self):
        """Test that setting the loan amount to a positive value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        new_loan_amount = 150000
        mortgage.set_loan_amount(new_loan_amount)
        self.assertEqual(mortgage.get_loan_amount(), new_loan_amount)

    def test_rate_mutator_with_valid_enum_value(self):
        """Test setting the rate to a valid MortgageRate enum value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        new_rate = 'VARIABLE_1'  
        mortgage.set_rate(new_rate)
        self.assertEqual(mortgage.get_rate().name, new_rate)

    def test_rate_mutator_with_invalid_enum_value(self):
        """Test that setting the rate to an invalid MortgageRate enum value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        with self.assertRaises(ValueError):
            mortgage.set_rate('NON_EXISTENT_RATE')

    def test_frequency_mutator_with_valid_enum_value(self):
        """Test setting the frequency to a valid PaymentFrequency enum value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        new_frequency = 'BI_WEEKLY'
        mortgage.set_frequency(new_frequency)
        self.assertEqual(mortgage.get_frequency().name, new_frequency)

    def test_frequency_mutator_with_invalid_enum_value(self):
        """Test that setting the frequency to an invalid PaymentFrequency enum value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        with self.assertRaises(ValueError):
            mortgage.set_frequency('NON_EXISTENT_FREQUENCY')

    def test_amortization_mutator_with_valid_value(self):
        """Test setting the amortization to a valid value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25) 
        new_amortization = 15 
        mortgage.set_amortization(new_amortization)
        self.assertEqual(mortgage.get_amortization(), new_amortization)

    def test_amortization_mutator_with_invalid_value(self):
        """Test that setting the amortization to an invalid value."""
        mortgage = Mortgage(100000, 'FIXED_5', 'MONTHLY', 25)
        invalid_amortization = 3  
        with self.assertRaises(ValueError):
            mortgage.set_amortization(invalid_amortization)

    def test_init_properly_sets_attributes_for_valid_input(self):
        """Test that __init__ properly sets attributes for valid inputs."""
        loan_amount = 200000
        rate = 'FIXED_5'
        frequency = 'MONTHLY'
        amortization = 25

        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        self.assertEqual(mortgage.get_loan_amount(), loan_amount)
        self.assertEqual(mortgage.get_rate().name, rate)
        self.assertEqual(mortgage.get_frequency().name, frequency)
        self.assertEqual(mortgage.get_amortization(), amortization)

    def test_calculate_payment_example_case(self):
        """Test the calculate_payment method with a provided example."""
        mortgage = Mortgage(682912.43, 'FIXED_1', 'MONTHLY', 10)
        expected_payment = 7578.30
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

    def test_str_monthly_payment(self):
        """Test the __str__ method with a monthly payment."""
        mortgage = Mortgage(682912.43, 'FIXED_1', 'MONTHLY', 30)
        expected_start = "Mortgage Amount: $682,912.43 Rate: 5.99% Amortization: 30 Frequency: Monthly"
        self.assertTrue(str(mortgage).startswith(expected_start))

    def test_str_biweekly_payment(self):
        """Test the __str__ method with a biweekly payment."""
        mortgage = Mortgage(300000, 'FIXED_3', 'BI_WEEKLY', 25)
        expected_start = "Mortgage Amount: $300,000.00 Rate: 5.89% Amortization: 25 Frequency: Bi_weekly"
        self.assertTrue(str(mortgage).startswith(expected_start))

    def test_str_weekly_payment(self):
        """Test the __str__ method with a weekly payment."""
        mortgage = Mortgage(450000, 'VARIABLE_1', 'WEEKLY', 20)
        expected_start = "Mortgage Amount: $450,000.00 Rate: 6.79% Amortization: 20 Frequency: Weekly"
        self.assertTrue(str(mortgage).startswith(expected_start))
    
    def test_repr_accuracy(self):
        """Test the accuracy of the mortgage object's __repr__."""
        mortgage = Mortgage(682912.43, 'FIXED_3', 'MONTHLY', 30)
        
        expected_repr = "[682912.43, 0.0589, 30, 12]"
        
        self.assertEqual(repr(mortgage), expected_repr)