from enum import Enum 

class PaymentMode(Enum):
    PAYPAL = "PayPal"
    GOOGLEPAY = "GooglePay"
    CREDITCARD = "CreditCard"