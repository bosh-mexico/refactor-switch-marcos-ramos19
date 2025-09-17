'''
Payment Modes
The system must support the following payment modes:

PayPal

GooglePay

CreditCard

Any unsupported or invalid payment mode should be handled gracefully with an error message.

Checkout Function
The system must provide a function named checkout that:

Takes a PaymentMode (enum) as input.

Takes the payment amount (double) as input.

Processes the payment based on the selected PaymentMode.

Processing Logic
For each payment mode, the system must print a confirmation message indicating:

The selected payment mode.

The amount being processed.

Placeholder logic should be available for future integration with actual payment processing APIs.
'''

from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# Checkout function
def checkout(mode: PaymentMode, amount: float):
    match mode:
        case PaymentMode.PAYPAL:
            print(f"Processing PayPal payment of ${amount:.2f}")
            # Add PayPal-specific logic here

        case PaymentMode.GOOGLEPAY:
            print(f"Processing GooglePay payment of ${amount:.2f}")
            # Add GooglePay-specific logic here

        case PaymentMode.CREDITCARD:
            print(f"Processing Credit Card payment of ${amount:.2f}")
            # Add Credit Card-specific logic here

        case _:
            print("Invalid payment mode selected!")

# Example usage
if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)