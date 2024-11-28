class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90  


class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.options = {
            'SportWheels': 0,
            'SportEngine': 0,
            'SportInterior': 0,
            'GPS': 0,
            'SelfDriving': 0
        }

    def add_sport_wheels(self, include_option):
        self.options['SportWheels'] = 1000.00 if include_option.upper() == 'Y' else 0

    def add_sport_engine(self, include_option):
        self.options['SportEngine'] = 3000.00 if include_option.upper() == 'Y' else 0

    def add_sport_interior(self, include_option):
        self.options['SportInterior'] = 2000.00 if include_option.upper() == 'Y' else 0

    def add_gps(self, include_option):
        self.options['GPS'] = 5000.00 if include_option.upper() == 'Y' else 0

    def add_self_driving(self, include_option):
        self.options['SelfDriving'] = 10000.00 if include_option.upper() == 'Y' else 0

    def price_with_options(self):
        total_options_price = sum(self.options.values())
        return self.sticker_price + total_options_price



luxury_car = Luxury("Rolls-Royce", "Phantom", 450000)


luxury_car.add_sport_wheels('Y')       
luxury_car.add_sport_engine('N')       
luxury_car.add_sport_interior('Y')     
luxury_car.add_gps('Y')                
luxury_car.add_self_driving('N')       


print(f"Base price for {luxury_car.make} {luxury_car.model}: ${luxury_car.sticker_price:,.2f}")
print(f"Discounted price: ${luxury_car.discount_price():,.2f}")
print(f"Price with selected options: ${luxury_car.price_with_options():,.2f}")
