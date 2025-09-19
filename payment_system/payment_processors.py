from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod 
    def process(self, amount:float) -> bool:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount: .2f}")
        
        print("→ PayPal payment processed successfully!")
        return True
    
    def get_name(self) -> str:
        return "PayPal"

class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        print(f"Processing GooglePay payment of ${amount: .2f}")
        
        print("→ GooglePay payment processed successfully!")
        return True
    
    def get_name(self) -> str:
        return "GooglePay"
    
class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> bool:
        print(f"Processing Credit Card payment of ${amount: .2f}")
        
        print("→ Credit Card payment processed successfully!")
        return True
    
    def get_name(self) -> str:
        return "Credit Card"
