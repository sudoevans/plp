class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.battery_level = 100

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def charge(self, minutes):
        self.battery_level += minutes // 10

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Color: {self.color}")
        print(f"Battery Level: {self.battery_level}%")

phone1 = Smartphone("Apple", "iPhone 14", 128, "Purple")
phone1.make_call("123-456-7890")
phone1.send_message("987-654-3210", "Hello!")
phone1.charge(30)
phone1.display_info()




# Activity Two

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # Abstract method

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running!")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming!")

# Example usage:
dog = Dog("Buddy")
bird = Bird("Tweety")
fish = Fish("Nemo")

dog.move()
bird.move()
fish.move()