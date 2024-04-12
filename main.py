"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: AbdulRahman Hassan Bangura
Date: 08/04/24
"""

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
try: 
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = items[3].strip()

                ### REQUIREMENT:
                ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
                mortgage = Mortgage(amount, rate, frequency, int(amortization))

                
                ### REQUIREMENT:
                ### PRINT THE MORTGAGE OBJECT
                print(mortgage)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError:
    
    print("The file was not found.")