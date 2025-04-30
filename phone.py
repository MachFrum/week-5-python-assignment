class Smartphone:
    def __init__(self, brand, model, battery=100):
        # Initialize smartphone attributes
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def use(self, minutes):
        # Basic battery consumption
        self.battery = max(0, self.battery - minutes)
        print(f"📱 Used {minutes} mins | Battery: {self.battery}%")
    
    def charge(self):
        # Restore full battery
        self.battery = 100
        print("🔋 Fully charged!")
    
    def get_info(self):
        # Display basic info
        return f"{self.brand} {self.model}"

class WaterproofPhone(Smartphone):  # Inheritance
    def __init__(self, brand, model, waterproof_rating):
        super().__init__(brand, model)
        # I Added a feature for subclass
        self.waterproof_rating = waterproof_rating
    
    def use(self, minutes):  # Polymorphism (method overriding)
        # Waterproof phones use more battery
        self.battery = max(0, self.battery - minutes * 2)
        print(f"🌊 Used underwater {minutes} mins | Battery: {self.battery}%")

# Usage
normal_phone = Smartphone("Apple", "iPhone SE")
waterproof_phone = WaterproofPhone("Samsung", "Galaxy S23", "IP68")

normal_phone.use(30)    # 📱 Used 30 mins | Battery: 70%
waterproof_phone.use(30) # 🌊 Used underwater 30 mins | Battery: 40%

print(normal_phone.get_info())    # Apple iPhone SE
print(waterproof_phone.get_info()) # Samsung Galaxy S23