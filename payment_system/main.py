from payment_services import checkout, PaymentService
from payment_modes import PaymentMode

def main():
    amount = 150.75
    
    print("=== Payment System Demo ===\n")
    
    for mode in PaymentMode:
        success = checkout(mode, amount)
        print(f"Success: {success}\n")
        
    print("--- Error Cases ---")
    checkout("invalid", amount)
    checkout(PaymentMode.PAYPAL, -10)
    
if __name__ == "__main__":
    main()