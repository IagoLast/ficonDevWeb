import database

"""
 Dish Operations
"""

def create_dish(name, price, image=None, description=None, dish_type=None):
    database.new_dish(name,price,image,description,dish_type)

def get_dishes():
    return database.get_dishes()

def get_dishes_ordered_by(field,order):
    return database.get_dishes_ordered_by(field,order)

def get_dishes_by_type(dish_type):
    return database.get_dishes_by_type(dish_type)

def get_dish_by_id(id):
    return database.get_dish_by_id(id)

def get_dish_by_name(name):
    return database.get_dish_by_name(name)

def remove_dish(id):
    database.remove_dish_by_id(id)

"""
    Menu Operations

 """

def create_menu(name=None, price=None, dishes=None, description=None):
    database.new_menu(name,price,dishes,description)

def get_menus():
    return database.get_menus()

def get_menu_by_id(id):
    return database.get_menu_by_id(id)

def get_menu_by_name(name):
    return database.get_dish_by_name(name)

def remove_menu_by_id(id):
    database.remove_menu_by_id(id)

"""
Reservation Operations
"""

def create_reservation(name=None,assistants_number=None,date=None):
    database.new_reservation(name,assistants_number,date)

def get_reservation_by_name(name):
    return database.get_next_reservation_from_reserver(name)

def get_reservation_by_id(id):
    return database.get_reservation_by_id(id)
"""
User Operations
"""

def create_user(name,password):
    database.new_user(name,password)

def get_users():
    return database.get_users()

def remove_user_by_name(name):
    database.remove_user_by_name(name)