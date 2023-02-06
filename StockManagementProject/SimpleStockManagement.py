class StockItem:
    stock_category = "Car accessories"

    def __init__(self, code, quantity, price):
        self.__code = code
        self.__quantity = quantity
        self.__price = price

    # setters
    def set_stock_code(self, code):
        self.__code = code

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    # getters
    def get_stock_code(self):
        return self.__code

    def get_quantity(self):
        return self.__quantity

    def get_price_with_vat(self):
        return "{:.2f}".format(round(self.__price * 1.175, 2))

    def get_price_without_vat(self):
        return "{:.2f}".format(self.__price)

    def get_stock_name(self):
        return "Unknown stock name"

    def get_stock_description(self):
        return "Unknown stock description"

    # increase/sell stock
    def increase_stock(self, amount):
        if (amount < 1):
            print("Error: Stock increase cannot be less than 1.")
            return
        self.__quantity += amount
        if (self.__quantity > 100):
            self.__quantity -= amount
            print("Error: Stock amount cannot exceed 100.")

    def sell_stock(self, amount):
        if (amount < 1):
            print("Error: Cannot sell less than 1 stock.")
            return
        elif (amount < self.__quantity or amount == self.__quantity):
            self.__quantity -= amount
            return True
        else:
            return False
        
    def get_vat(self):
        return 17.5

    def __str__(self):
        return f"Stock code: {self.get_stock_code()}, Stock name: {self.get_stock_name()}, Stock description: {self.get_stock_description()}, Quantity: {self.get_quantity()}, " \
            f"Price without VAT: £{self.get_price_without_vat()}, Price with VAT: £{self.get_price_with_vat()}"


class NavSys(StockItem):
    def __init__(self, code, quantity, price, brand):
        super().__init__(code, quantity, price)
        self.__brand = brand

    # setters
    def set_brand(self, brand):
        self.__brand = brand

    # getters
    def get_brand(self):
        return self.__brand

    def get_stock_name(self):
        return "Navigation system"

    def get_stock_description(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        return f"{super().__str__()}, Brand: {self.get_brand()}"


class SoundSys(StockItem):
    def __init__(self, stockCode, quantity, price, brand, voltage):
        super().__init__(stockCode, quantity, price)
        self.__brand = brand
        self.__voltage = voltage

    # setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_voltage(self, voltage):
        self.__voltage = voltage

    # getters
    def get_brand(self):
        return self.__brand

    def get_voltage(self):
        return self.__voltage

    def get_stock_name(self):
        return "Sound system"

    def get_stock_description(self):
        return "Hi-Fi speaker system"

    def __str__(self):
        return f"{super().__str__()}, Brand: {self.get_brand()}, Voltage: {self.get_voltage()}"


class DashCam(StockItem):
    def __init__(self, stockCode, quantity, price, brand, pixels):
        super().__init__(stockCode, quantity, price)
        self.__brand = brand
        self.__pixels = pixels

    # setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_pixels(self, pixels):
        self.__pixels = pixels

    # getters
    def get_brand(self):
        return self.__brand

    def get_pixels(self):
        return self.__pixels

    def get_stock_name(self):
        return "Dash camera"

    def get_stock_description(self):
        return "HD front and rear dash cam"

    def __str__(self):
        return f"{super().__str__()}, Brand: {self.get_brand()}, Pixels: {self.get_pixels()}"


class BeltPad(StockItem):
    def __init__(self, stockCode, quantity, price, brand, colour):
        super().__init__(stockCode, quantity, price)
        self.__brand = brand
        self.__colour = colour

    # setters
    def set_brand(self, brand):
        self.__brand = brand

    def set_colour(self, colour):
        self.__colour = colour

    # getters
    def get_brand(self):
        return self.__brand

    def get_colour(self):
        return self.__colour

    def get_stock_name(self):
        return "Seatbelt pad"

    def get_stock_description(self):
        return "Extra comfort seatbelt pad"

    def __str__(self):
        return f"{super().__str__()}, Brand: {self.get_brand()}, Colour: {self.get_colour()}"

object_array = []
# simple interactive user interface loop
user_active = True
while (user_active):
    user_input = str(input("Type '1' to create a new object, '2' to view or edit an object or 'exit' to exit the program.\n"))
    if (user_input == 'exit'):
        user_active = False
    elif (user_input == '1'):
        user_input = str(input("Type '1' to create NavSys object, '2' to create SoundSys object, '3' to create DashCam object, '4' to create BeltPad object or 'exit' to exit the program.\n"))
        if (user_input == 'exit'):
            user_active = False
        elif (user_input == '1'):
            # creates NavSys object
            code = str(input("Enter the stock code you would like: "))
            quantity = int(input("Enter the quantity you would like: "))
            price = float(input("Enter the price you would like: "))
            brand = str(input("Enter the brand you would like: "))
            object_array.append(NavSys(code, quantity, price, brand))
            print("Created NavSys object.")
        elif (user_input == '2'):
            # creates SoundSys object
            code = str(input("Enter the stock code you would like: "))
            quantity = int(input("Enter the quantity you would like: "))
            price = float(input("Enter the price you would like: "))
            brand = str(input("Enter the brand you would like: "))
            voltage = int(input("Enter the voltage you would like: "))
            object_array.append(SoundSys(code, quantity, price, brand, voltage))
            print("Created SoundSys object.")
        elif (user_input == '3'):
            # creates DashCam object
            code = str(input("Enter the stock code you would like: "))
            quantity = int(input("Enter the quantity you would like: "))
            price = float(input("Enter the price you would like: "))
            brand = str(input("Enter the brand you would like: "))
            pixels = int(input("Enter the pixels you would like: "))
            object_array.append(DashCam(code, quantity, price, brand, pixels))
            print("Created DashCam object.")
        elif (user_input == '4'):
            # creates BeltPad object
            code = str(input("Enter the stock code you would like: "))
            quantity = int(input("Enter the quantity you would like: "))
            price = float(input("Enter the price you would like: "))
            brand = str(input("Enter the brand you would like: "))
            colour = str(input("Enter the colour you would like: "))
            object_array.append(BeltPad(code, quantity, price, brand, colour))
            print("Created BeltPad object.")
        else: 
            print("Invalid input, program ended.")
            user_input = 'exit'
    elif (user_input == '2'):
        if (len(object_array) < 1):
            print("You have no objects to edit.")
        else:
            user_input = str(input("Type '1' to print item information, '2' to add stock, '3' to sell stock, '4' to change the price or 'exit' to exit the program.\n"))
            # loop through objects in object array
            for item in (object_array):
                if (user_input == 'exit'):
                    user_active = False
                elif (user_input == '1'):
                    print(str(item))
                elif (user_input == '2'):
                    amount = int(input(f"Enter the amount of units to be added for {item.get_stock_name()}: "))
                    item.increase_stock(amount)
                elif (user_input == '3'):
                    amount = int(input(f"Enter the amount of units to be sold for {item.get_stock_name()}: "))
                    item.sell_stock(amount)
                elif (user_input == '4'):
                    inp = str(input(f"Enter the price you would like to set for {item.get_stock_name()} (Enter 'n' to keep the current price): "))
                    if (inp == 'n'):
                        pass
                    else:
                        amount = float(inp)
                        item.set_price(amount)
                else: 
                    print("Invalid input, program ended.")
                    user_input = 'exit'
    else:
        print("Invalid input, program ended.")
        user_input = 'exit'

    if (user_input != 'exit'):
        user_input = str(input("Continue? (y/n)\n")).lower()
        if (user_input == 'y'):
            user_active = True
        elif (user_input == 'n'):
            user_active = False
        else:
            user_active = False
            print("Invalid input, program ended.")