# OOP Concepts in Python: Class Design & Polymorphism 🐍

This repository contains solutions to two programming activities focused on Object-Oriented Programming (OOP) concepts in Python: **class design** and **polymorphism**. Below is an overview of how the assignment was tackled.

---

## 📱 Assignment 1: Smartphone Class Design

### **Features Implemented**
#### `Smartphone` Class (Base Class)
- **Attributes**: 
  - `brand` (e.g., Apple/Samsung)
  - `model` (e.g., iPhone SE/Galaxy S23)
  - `battery` (defaults to 100%)
- **Methods**:
  - `use(minutes)`: Reduces battery by `minutes` consumed.
  - `charge()`: Restores battery to 100%.
  - `get_info()`: Returns formatted device info.
- **Constructor**: Initializes `brand`, `model`, and optional `battery`.

#### `WaterproofPhone` Class (Subclass of `Smartphone`)
- **Inheritance**: Inherits all attributes/methods from `Smartphone`.
- **Extended Features**:
  - New attribute: `waterproof_rating` (e.g., "IP68").
  - **Polymorphism**: Overrides `use()` method to drain battery twice as fast underwater.
- **Encapsulation**: Battery management is handled internally.

### **Code Example**
```python
# Create smartphone objects
normal_phone = Smartphone("Apple", "iPhone SE")
waterproof_phone = WaterproofPhone("Samsung", "Galaxy S23", "IP68")

# Demonstrate usage and polymorphism
normal_phone.use(30)     # 📱 Battery: 70%
waterproof_phone.use(30) # 🌊 Battery: 40% (drains faster)
```

---

## 🐍 Activity 2: Polymorphism with Animals

### **Features Implemented**
- **Base Class**: `Animal` with abstract `move()` method.
- **Subclasses**:
  - `Fish`: Overrides `move()` to print "Swimming 🐟"
  - `Bird`: Overrides `move()` to print "Flying 🦅"
  - `Snake`: Overrides `move()` to print "Slithering 🐍"
- **Polymorphism**: A list of `Animal` objects calls their unique `move()` implementations.

### **Code Example**
```python
animals = [Fish(), Bird(), Snake()]

for creature in animals:
    creature.move()
# Output:
# Swimming 🐟
# Flying 🦅
# Slithering 🐍
```

---

## 🚀 How to Run
1. **Prerequisites**: Python 3.x installed.
2. **Files**:
   - `phone.py`: Contains the `Smartphone` and `WaterproofPhone` classes.
   - `animals.py`: Contains the `Animal` hierarchy.
3. **Execution**:
   - Run the files directly to see the output:
     ```bash
     python phone.py
     python animals.py
     ```

---

## 📝 Key OOP Concepts Demonstrated
- **Inheritance**: `WaterproofPhone` extends `Smartphone`.
- **Polymorphism**: Overridden `move()` and `use()` methods.
- **Encapsulation**: Internal battery management in `Smartphone`.

Feel free to explore the code and experiment with new subclasses! ✨
