"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""


from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """Manages and calculates mortgage payments."""

    def __init__(self, loan_amount, rate, frequency, amortization):
        """
        Initializes a new Mortgage instance with given parameters.
        Parameters:
            self, loan_amount, rate, frequency, amortization.
        Returns:
            str: Deposit confirmation message.
        Throws: 
            ValueError for invalid rate
            ValueError for invalid frequency
            ValueError for invalid amoritization
        """

        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        try:
            self.__rate = MortgageRate[rate]
        except KeyError:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__frequency = PaymentFrequency[frequency]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

    def get_loan_amount(self):
        
        return self.__loan_amount

    def set_loan_amount(self, value):
        
        if value > 0:
            self.__loan_amount = value
        else:
            raise ValueError("Loan Amount must be positive.")
        
    def get_rate(self):
        
        return self.__rate

    def set_rate(self, rate_str):
        
        try:
            self.__rate = MortgageRate[rate_str]
        except KeyError:
            raise ValueError("Rate provided is invalid.")
        
    def get_frequency(self):
        
        return self.__frequency

    def set_frequency(self, frequency_str):
        
        try:
            self.__frequency = PaymentFrequency[frequency_str]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")
        
    def get_amortization(self):
        
        return self.__amortization

    def set_amortization(self, value):
        
        if value in VALID_AMORTIZATION:
            self.__amortization = value
        else:
            raise ValueError("Amortization provided is invalid.")
        
    def calculate_payment(self) -> float:
        """
        Calculates and returns the monthly mortgage payment.
        Parameters:
            self
        Returns:
            float: payment
        """
        period_rate = self.__rate.value / self.__frequency.value
        
        total_payments = self.__frequency.value * self.__amortization
        
        present_value = self.__loan_amount

        payment = (period_rate * present_value) / (1 - (1 + period_rate) ** -total_payments)
        return round(payment, 2)
    
    def __str__(self):
        """
        Provides a string representation of the mortgage details including calculated payment.
        Parameters:
            self
        Returns:
            str: updated data
        """
        formatted_amount = "${:,.2f}".format(self.__loan_amount)
        formatted_rate = "{:.2f}%".format(self.__rate.value * 100)
        formatted_payment = "${:,.2f}".format(self.calculate_payment())

        return (f"Mortgage Amount: {formatted_amount} "
                f"Rate: {formatted_rate} "
                f"Amortization: {self.__amortization} "
                f"Frequency: {self.__frequency.name.capitalize()} "
                f"-- Calculated Payment: {formatted_payment}")
    
    def __repr__(self):
        """
        Provides a formal string representation of the Mortgage instance
        Parameters:
            self
        Returns:
            str: updated data
        """
        return f"[{self.__loan_amount}, {self.__rate.value}, {self.__amortization}, {self.__frequency.value}]"