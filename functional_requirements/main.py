from payment_system import PaymentMode, PaymentProcessor, checkout

def main():
    processor = PaymentProcessor()
    
    for mode in processor.get_supported_methods():
        success = processor.checkout(mode, 150.75)
        print(f"Result: {'Nice job!' if success else 'Sorry, it fail!'}")
    
    if __name__ == "__main__":
        main()