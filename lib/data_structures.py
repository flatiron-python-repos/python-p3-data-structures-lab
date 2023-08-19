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
    return [c.get("name") for c in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [c for c in spicy_foods if c["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print('{} ({}) | Heat Level: {}'.format(i.get("name"), i.get("cuisine"), i.get("heat_level")*"🌶"))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i.get("cuisine") == cuisine:
            return i

def print_spiciest_foods(spicy_foods):
    spicies = get_spiciest_foods(spicy_foods)
    for i in spicies:
        print('{} ({}) | Heat Level: {}'.format(i.get("name"), i.get("cuisine"), i.get("heat_level")*"🌶"))



def get_average_heat_level(spicy_foods):
    all_heats = [heat.get("heat_level") for heat in spicy_foods]
    return sum(all_heats) / len(all_heats)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



# get_names(spicy_foods)
# get_spiciest_foods(spicy_foods)
# print_spicy_foods(spicy_foods)
# get_spicy_food_by_cuisine(spicy_foods, "American")
# print_spiciest_foods(spicy_foods)
# get_average_heat_level(spicy_foods)
spicy_food =    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
create_spicy_food(spicy_foods, spicy_food)