from .payment_modes import PaymentMode
from .strategies import PayPalStrategy, GooglePayStrategy, CreditCardStrategy

class PaymentProcessor:
    
    def __init__(self):
        self._strategies = {
            PaymentMode.PAYPAL: PayPalStrategy(),
            PaymentMode.GOOGLEPAY: GooglePayStrategy(),
            PaymentMode.CREDITCARD: CreditCardStrategy(),
        }
    
    def checkout(self, mode:PaymentMode, amount:float) -> bool:
        if amount <= 0:
            print("❌ Invalid Amount")
            return False
        if mode not in self._strategies:
            print("❌ Payment method not supported")
            return False
        
        strategy = self._strategies[mode]
        return strategy.process(amount)
    
    def add_payment_method(self, mode:PaymentMode, strategy):
        self._strategies[mode] = strategy
    
    def get_supported_methods(self):
        return list(self._strategies.keys())