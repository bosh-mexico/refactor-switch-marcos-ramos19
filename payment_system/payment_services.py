from payment_modes import PaymentMode
from payment_processors import PayPalProcessor, GooglePayProcessor, CreditCardProcessor

class PaymentService:
    def __init__(self):
        self.processors = {
            PaymentMode.PAYPAL: PayPalProcessor(),
            PaymentMode.GOOGLEPAY: GooglePayProcessor(),
            PaymentMode.CREDITCARD: CreditCardProcessor()
        }
    
    def checkout(self, mode:PaymentMode, amount:float) -> bool:
        if not isinstance(mode, PaymentMode):
            print("Error: Invalid payment mode!")
            return False
        
        if amount <= 0:
            print("Error: Amount must be greater than 0!")
            return False
        
        try: 
            processor = self.processors[mode]
            return processor.process(amount)
        except KeyError:
            print("Error: Unsupported payment mode!")
            return False
        
_service = PaymentService()

def checkout(mode: PaymentMode, amount: float) -> bool:
    return _service.checkout(mode, amount)