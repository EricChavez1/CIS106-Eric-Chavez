class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90


class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.options = {
            'SportWheels': 0,
            'SportEngine': 0,
            'SportInterior': 0
        }

    def add_sport_wheels(self, include_option):
        self.options['SportWheels'] = 1000.00 if include_option.upper() == 'Y' else 0

    def add_sport_engine(self, include_option):
        self.options['SportEngine'] = 3000.00 if include_option.upper() == 'Y' else 0

    def add_sport_interior(self, include_option):
        self.options['SportInterior'] = 2000.00 if include_option.upper() == 'Y' else 0

    def price_with_options(self):
        total_options_price = sum(self.options.values())
        return self.sticker_price + total_options_price





car = Sport("Mclaren", "765 LT", 280000)

#hi lol
car.add_sport_wheels('Y')
car.add_sport_engine('N')
car.add_sport_interior('Y')




print(f"Base price for {car.make} {car.model}: ${car.sticker_price}")
print(f"Discounted price: ${car.discount_price()}")
print(f"Price with selected options: ${car.price_with_options()}")
