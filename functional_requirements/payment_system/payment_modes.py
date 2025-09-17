from enum import Enum

class PaymentMode(Enum):
    PAYPAL = "paypal"
    GOOGLEPAY = "googlepay"
    CREDITCARD = "creditcard"