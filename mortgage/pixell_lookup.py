"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: AbdulRahman Hassan Bangura
Date: 08/04/2024
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""

# Importing Enum class from the enum module.
from enum import Enum

class MortgageRate(Enum):
    """An enumeration representing valid mortgage rates."""
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

class PaymentFrequency(Enum):
    """An enumeration representing valid payment frequencies."""
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}
