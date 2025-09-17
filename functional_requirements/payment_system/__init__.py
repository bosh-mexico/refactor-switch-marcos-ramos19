from .payment_modes import PaymentMode
from .processor import PaymentProcessor

def checkout(mode: PaymentProcessor, amount:float) -> bool:
    processor = PaymentProcessor()
    return processor.checkout(mode, amount)

__all__ = ['PaymentMode', 'PaymentProcessor', 'checkout']