class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{} menu available from {} to {}'.format(self.name,
                                                        self.start_time,
                                                        self.end_time)

    def calculate_bill(self, purchased_items):
        sum_of_items = 0
        for item in purchased_items:
            if item in self.items:
                sum_of_items += self.items[item]
        return sum_of_items


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if menu.start_time <= time and \
               menu.end_time >= time:
                available.append(menu.name)
        return available


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


items = {'pancakes': 7.50,
         'waffles': 9.00,
         'burger': 11.00,
         'home fries': 4.50,
         'coffee': 1.50,
         'espresso': 3.00,
         'tea': 1.00,
         'mimosa': 10.50,
         'orange juice': 3.50}

eb_items = {'salumeria plate': 8.00,
            'salad and breadsticks (serves 2, no refills)': 14.00,
            'pizza with quattro formaggi': 9.00,
            'duck ragu': 17.50,
            'mushroom ravioli (vegan)': 13.50,
            'coffee': 1.50,
            'espresso': 3.00,
            }

d_items = {'crostini with eggplant caponata': 13.00,
           'ceaser salad': 16.00,
           'pizza with quattro formaggi': 11.00,
           'duck ragu': 19.50,
           'mushroom ravioli (vegan)': 13.50,
           'coffee': 2.00,
           'espresso': 3.00,
           }

k_items = {'chicken nuggets': 6.50,
           'fusilli with wild mushrooms': 12.00,
           'apple juice': 3.00
           }

brunch = Menu('brunch', items, 11.00, 16.00)
early_bird = Menu('early_bird', eb_items, 15.00, 18.00)
dinner = Menu('dinner', d_items, 17.00, 23.00)
kids = Menu('kids', k_items, 11.00, 21.00)

print(brunch)
print(early_bird)
print(dinner)
print(kids)

purchased = ['pancakes', 'home fries', 'coffee']
cost = brunch.calculate_bill(purchased)
print('Cost of brunch purchased: ', cost)

cost_eb = early_bird.calculate_bill(['mushroom ravioli (vegan)', 'salumeria plate'])
print('Cost of early bird purchased: ', cost_eb)

flagship_store = Franchise("1232 West End Road", [brunch, dinner, kids, early_bird])
new_installment = Franchise("12 East Mulberry Street", [brunch, dinner, kids, early_bird])
print('You can choose from the following menus at 12 pm: ', new_installment.available_menus(12.00))
print('You can choose from the following menus at 5 pm: ', new_installment.available_menus(17.00))

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepas_business = Business("Take a' Arepa", arepas_place)
print(arepas_place)









