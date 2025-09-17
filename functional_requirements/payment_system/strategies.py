from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process(self, amount:float) -> bool:
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
class PayPalStrategy(PaymentStrategy):
    def process(self, amount:float) -> bool:
        print(f"✅ PayPal payment: ${amount:.2f}")
        return True
    
    @property
    def name(self) -> str:
        return "PayPal"
    
class GooglePayStrategy(PaymentStrategy):
    def process(self, amount:float) -> bool:
        print(f"✅ GooglePay payment: ${amount:.2f}")
        return True
    
    @property
    def name(self) -> str:
        return "GooglePay"

class CreditCardStrategy(PaymentStrategy):
    def process(self, amount:float) -> bool:
        print(f"✅ Credit Card payment: ${amount:.2f}")
        return True
    
    @property
    def name(self) -> str:
        return "Credit Card"