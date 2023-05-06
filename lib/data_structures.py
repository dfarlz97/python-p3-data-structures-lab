spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = list()
    for food in spicy_foods:
        food_names.append(food['name'])
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_list = list()
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food['name'], f"({food['cuisine']})", '|', 'Heat Level:', food['heat_level'] * '🌶')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == 'Thai':
            return spicy_foods[0]
        elif cuisine == 'American':
            return spicy_foods[1]
        elif cuisine == 'Sichuan':
            return spicy_foods[2]
        else:
            return None 

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(food['name'], f"({food['cuisine']})", '|', 'Heat Level:', food['heat_level'] * '🌶')

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
