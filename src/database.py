import pymongo
import bson.objectid
from datetime import datetime
from werkzeug.security import generate_password_hash


connection = pymongo.MongoClient()
db = connection.test
dishes = db.dishes
menus = db.menus
reservations = db.reservations
users = db.users

"""
 Dish Operations

"""


def new_dish(name=None, price=None, image=None, description=None, dish_type=None):
    """
    Adds a new dish to the dish database collection
    :param name: name of the dish
    :param price: price of the dish
    :param image: url of the image of the dish
    :param description: description of the dish
    :param dish_type: type of dish [appetizer,meat,fish,dessert]
    """
    dish = { 'name' : name,
           'price' : price,
           'url' : image,
           'description' : description,
           'type' : dish_type
           }
    dishes.insert(dish)
    print 'Added a new dish'


def get_dishes():
    """
    Obtains all the dishes of the dishes collection

    :return: a list with all the dishes in the collection
    """
    dish_list = []
    for dish in dishes.find():
        dish_list.append(dish)
    return dish_list


def get_dishes_by_type(dish_type=None):
    """
    returns a list with all the dishes of a :dish_type: type

    :param dish_type: type of the dishes to look for
    :return: a list with all the dishes of :dish_type: type
    """
    dish_list = []
    for dish in dishes.find({'type': dish_type}):
        dish_list.append(dish)
    return dish_list


def get_dish_by_id(id=None):
    """

    :param id: id of the dish to retrieve from the database
    :return: a dictionary that represents the dish with id :id:
    """
    return dishes.find_one({'_id': bson.objectid.ObjectId(id)})


def get_dish_by_name(name=None):
    """

    :param name: name of the dish to retrieve
    :return:  a dictionary that represents the dish with name :name: (name is not Unique)
    """
    return dishes.find_one({'name': name})


def remove_dish_by_id(id=None):
    """
    Deletes the dish with id :id: from the dishes collection
    :param id: id of the dish to delete
    """
    dishes.remove({'_id' : bson.objectid.ObjectId(id)})


"""
Menu operations
"""


def new_menu(name=None, price=None, dishes=None, description=None):

    """
    Adds a new menu to the menus collection

    :param name: name of the new menu
    :param price: price of the new menu
    :param dishes: a list with the dishes which forms the new menu
    :param description: description of the new menu
    """
    menu = {
           'name' : name,
           'price' : price,
           'dishes' : dishes,
           'description' : description
           }
    menus.insert(menu)
    print "Added a new menu"


def get_menus():
    """
    Retrieves all the menus from the menus collection

    :return: a list with all the menus of the menus collection
    """
    menu_list =[]
    for menu in menus.find():
        menu_list.append(menu)
    return menu_list


def get_menu_by_id(id=None):
    """
    Retrieves the menu with id :id: from the menus collection
    :param id: if of the menu to be retrieved
    :return: a dictionary that represents the menu with the given id
    """
    return menus.find_one({'_id' : id})


def get_menu_by_name(name=None):

    return menus.find_one({'name': name})

def remove_menu_by_id(id=None):
    menus.remove({'_id' : bson.objectid.ObjectId(id)})


"""
Reservation Operations
"""


def new_reservation(name=None,assistants_number=None,date=None,):
    reservation= {
        'reserved_by' : name,
        'assistants_number' : assistants_number,
        'date' : date,
    }
    reservations.insert(reservation)
    print 'Added a new reservation'

def get_reservations_by_user(name=None):
    reservation_list = []
    for reservation in reservations.find({'reserved_by' : name}):
        reservation_list.append(reservation)

    return reservations

def get_reservation_by_id(id=None):
    return reservations.find_one({'_id': bson.objectid.ObjectId(id())})

def get_next_reservation_from_name(name=None):
    current_time=datetime.now()
    reservation_list = []
    for reservation in reservations.find({'reserved_by':name , 'date' : {'$gte': current_time}}).sort({'date': pymongo.ASCENDING}).limit(1):
        reservation_list.append(reservation)
    return reservation_list

"""
User Operations
"""

def new_user(name=None,password=None):

    hashed_password = generate_password_hash(password)
    user = {
        '_id' : name,
        'hashed_password' : hashed_password
    }
    users.insert(user)

def find_user(id=None):
    return users.find_one({'_id' : id})

def get_users():
    user_list = []
    for user in users.find():
        user_list.append(user)
    return user_list

def remove_user_by_name(name=None):
    users.remove({'_id' : name})


"""
Debuging: db cleanup function
"""
def delete_database():
    db.dishes.remove()
    db.menus.remove()
    db.reservations.remove()
    db.users.remove()